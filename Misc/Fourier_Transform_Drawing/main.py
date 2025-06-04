import subprocess
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from svgpathtools import svg2paths, Path
import os

# parameters
directly_from_svg = True
svg_dir = os.path.join('svg', "heart-unlock-svgrepo-com.svg")
dft_simpson_level = 50 # Now represents the number of FFT coefficients to use
sample_size =500 + 1 #points must be odd to ensure parse_svg_path works correctly
num_path = 0
upside_down = False # Set to True to flip the image vertically

# --- STEP 1: Parse SVG path ---
def parse_svg_path(svg_file, num_samples=1001, flip_y=False):
    print(f"Parsing SVG file: {svg_file}")
    paths, attributes = svg2paths(svg_file)
    
    # Collect all raw points from all subpaths for overall centering
    all_raw_points_for_centering = []
    # Store original path index and subpath index for sine wave application later
    path_info = [] 

    for idx, path in enumerate(paths):
        if len(path) == 0:
            continue
        subpaths = path.continuous_subpaths()
        for sub_idx, subpath in enumerate(subpaths):
            if len(subpath) == 0:
                continue
            points = [subpath.point(t) for t in np.linspace(0, 1, num_samples)]
            all_raw_points_for_centering.extend(points)
            path_info.append({
                'original_path_idx': idx,
                'subpath_idx': sub_idx,
                'points': points, # Store raw points for later
                'attributes': attributes[idx] # Store original attributes
            })

    if not all_raw_points_for_centering:
        raise ValueError("No valid points found in SVG for centering.")

    # Calculate overall center for all points
    all_reals = [p.real for p in all_raw_points_for_centering]
    all_imags = [p.imag for p in all_raw_points_for_centering]
    
    overall_cx = sum(all_reals) / len(all_reals)
    overall_cy = sum(all_imags) / len(all_imags)

    final_path_points = []
    sine_wave_applied_path_idx = -1 # To track which path gets the sine wave

    for i, p_info in enumerate(path_info):
        raw_points = p_info['points']
        
        centered_points = []
        for p in raw_points:
            y_coord = -(p.imag - overall_cy) 
            if flip_y:
                y_coord = -y_coord 
            centered_points.append(complex(p.real - overall_cx, y_coord))
        
        # Check if this subpath comes from an original path with a 'fill' attribute
        # For the given SVG, the inner heart is the second <path> element (index 1) and has a fill.
        # We assume its first subpath is the one we want to modify.
        # This is still a heuristic and might need adjustment for other SVGs.
        if p_info['original_path_idx'] == 1 and 'fill' in p_info['attributes'] and p_info['attributes']['fill'] != 'none' and sine_wave_applied_path_idx == -1:
            # Apply sine wave modification to the outline of this path
            inner_path_points_to_modify = np.array(centered_points)
            x_coords = np.array([p.real for p in inner_path_points_to_modify])
            y_coords = np.array([p.imag for p in inner_path_points_to_modify])

            min_x, max_x = np.min(x_coords), np.max(x_coords)
            min_y, max_y = np.min(y_coords), np.max(y_coords)
            
            # Use arc length to normalize phase for sine wave
            segment_lengths = np.sqrt(np.diff(x_coords)**2 + np.diff(y_coords)**2)
            path_lengths = np.insert(np.cumsum(segment_lengths), 0, 0)
            total_length = path_lengths[-1] if len(path_lengths) > 0 else 1
            
            num_sine_points = num_samples
            sine_wave_amplitude = (max_y - min_y) * 0.05 # Smaller amplitude for outline effect
            sine_wave_frequency = 10 # More cycles for a wiggly outline
            
            modified_points = []
            for j, p in enumerate(inner_path_points_to_modify):
                t_normalized = (path_lengths[j] / total_length) if total_length > 0 else 0
                
                # Perturb the points *along the normal* or radial direction for a better outline effect.
                # For simplicity here, we'll perturb the y-coordinate.
                # A more advanced approach would calculate the local normal vector.
                sine_perturbation = sine_wave_amplitude * np.sin(2 * np.pi * sine_wave_frequency * t_normalized)
                
                modified_points.append(complex(p.real, p.imag + sine_perturbation))
            
            final_path_points.append(np.array(modified_points))
            sine_wave_applied_path_idx = i # Mark that we've applied it
        else:
            final_path_points.append(np.array(centered_points))

    if not final_path_points:
        raise ValueError("No valid paths found in SVG.")
    print(f"Parsed {len(final_path_points)} paths with {num_samples} points each")
    return final_path_points

# --- STEP 2: Compute FFT Coefficients ---
def compute_fft_coefficients(points, num_coefficients):
    N = len(points)
    # Compute the FFT
    fft_vals = np.fft.fft(points) / N 

    # Get frequencies corresponding to FFT output
    freqs = np.fft.fftfreq(N, d=1/N) 

    # Shift zero frequency to the center and create (frequency, coefficient) pairs
    shifted_freqs = np.fft.fftshift(freqs)
    shifted_fft_vals = np.fft.fftshift(fft_vals)

    # Combine frequencies and coefficients
    all_coefficients = list(zip(shifted_freqs, shifted_fft_vals))

    # Sort coefficients by magnitude and take the top `num_coefficients`
    sorted_coefficients = sorted(all_coefficients, key=lambda x: abs(x[1]), reverse=True)
    
    selected_coefficients = sorted_coefficients[:num_coefficients]
    
    return selected_coefficients


# --- STEP 3: Epicycles ---
def epicycles(DFT, t):
    x, y = 0, 0
    points = [(x, y)]
    for freq, Cn in DFT:
        radius = np.abs(Cn)
        phase = np.angle(Cn)
        
        x += radius * np.cos(2 * np.pi * freq * t + phase)
        y += radius * np.sin(2 * np.pi * freq * t + phase)
        
        points.append((x, y))
    return points

# --- Run image processing and load SVG ---
if not directly_from_svg:
    try:
        print("Running img_to_svg.py...")
        result = subprocess.run(['python', 'img_to_svg.py'], capture_output=True, text=True, check=True)
        svg_path = result.stdout.strip().splitlines()[-1]
        print(f"Generated SVG path: {svg_path}")
        if not os.path.exists(svg_path):
            raise FileNotFoundError(f"SVG file not found: {svg_path}")
    except subprocess.CalledProcessError as e:
        print("Error running img_to_svg.py:", e.stderr)
        exit(1)
else:
    svg_path = svg_dir

# --- Load and process points ---
all_path_list = parse_svg_path(svg_path, num_samples=sample_size, flip_y=upside_down)
path_points_list = [all_path_list[num_path]] if num_path != 0 else all_path_list
print(f"Number of paths detected: {len(path_points_list)}")

# Compute FFT for each path
FFT_list = [compute_fft_coefficients(points, num_coefficients=dft_simpson_level) for points in path_points_list]
print(f"Computed FFT for {len(FFT_list)} paths")

# Save FFT coefficients to DFT.txt
# This part assumes you only want to save the first path's FFT coefficients
if FFT_list:
    freq_list = [element[0] for element in FFT_list[0]]
    real_coeffs = [element[1].real for element in FFT_list[0]]
    imag_coeffs = [element[1].imag for element in FFT_list[0]]
    open('DFT.txt','w').write('\n'.join([str(freq_list), str(real_coeffs), str(imag_coeffs)]))
    print(f'FFT Coefficients saved to DFT.txt')
else:
    print("No FFT coefficients to save as FFT_list is empty.")


# --- STEP 4: Animation Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('black')
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.tick_params(colors='white')
ax.spines[:].set_color('white')

# Compute bounds across all paths
all_real = []
all_imag = []
for points in path_points_list:
    all_real.extend([p.real for p in points])
    all_imag.extend([p.imag for p in points])
min_x, max_x = min(all_real), max(all_real)
min_y, max_y = min(all_imag), max(all_imag)
x_range, y_range = max_x - min_x, max_y - min_y
x_pad, y_pad = x_range * 0.1, y_range * 0.1
ax.set_xlim(min_x - x_pad, max_x + x_pad)
ax.set_ylim(min_y - y_pad, max_y + y_pad)

ax.axhline(0, color='white', lw=0.5, alpha=0.5)
ax.axvline(0, color='white', lw=0.5, alpha=0.5)

# Precompute circle points
theta = np.linspace(0, 2 * np.pi, 100)

# Initialize epicycles for each path
max_n = max(len(fft_coeffs) for fft_coeffs in FFT_list) 
lines, circles, vectors = [], [], []
for _ in range(len(FFT_list)): 
    path_lines = []
    path_circles = []
    path_vectors = []
    for _ in range(max_n):
        line, = ax.plot([], [], 'cyan', lw=1, alpha=0.8)
        circle, = ax.plot([], [], 'white', lw=0.5, alpha=0.3)
        vector, = ax.plot([], [], 'yellow', lw=0.5, alpha=0.8)
        path_lines.append(line)
        path_circles.append(circle)
        path_vectors.append(vector)
    lines.append(path_lines)
    circles.append(path_circles)
    vectors.append(path_vectors)

# Traced paths (one per SVG path)
traced_paths = [[] for _ in FFT_list] 
path_line_artists = [ax.plot([], [], 'red', lw=1.5)[0] for _ in FFT_list] 

def init():
    for path_lines, path_circles, path_vectors in zip(lines, circles, vectors):
        for line, circle, vector in zip(path_lines, path_circles, path_vectors):
            line.set_data([], [])
            circle.set_data([], [])
            vector.set_data([], [])
    for path_line_artist in path_line_artists:
        path_line_artist.set_data([], [])
    return [item for sublist in (lines + circles + vectors) for item in sublist] + path_line_artists

speed_factor = 3
frames = 500

def animate(frame):
    t = (frame * speed_factor) / frames
    t %= 1

    all_artists = []
    for idx in range(len(FFT_list)): 
        DFT = FFT_list[idx] 
        current_path_lines = lines[idx]
        current_path_circles = circles[idx]
        current_path_vectors = vectors[idx]
        traced_path = traced_paths[idx]
        current_path_line_artist = path_line_artists[idx]

        # Compute epicycles for this path
        pts = epicycles(DFT, t)
        for i in range(len(DFT)):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            current_path_lines[i].set_data([x0, x1], [y0, y1])
            radius = np.abs(DFT[i][1]) 
            cx = x0 + radius * np.cos(theta)
            cy = y0 + radius * np.sin(theta)
            current_path_circles[i].set_data(cx, cy)
            current_path_vectors[i].set_data([x0, x1], [y0, y1])

        # Update traced path
        traced_path.append(pts[-1])
        x_path = [p[0] for p in traced_path]
        y_path = [p[1] for p in traced_path]
        current_path_line_artist.set_data(x_path, y_path)

        all_artists.extend(current_path_lines + current_path_circles + current_path_vectors + [current_path_line_artist])

    return all_artists

ani = FuncAnimation(
    fig, animate, frames=frames, init_func=init,
    interval=20, blit=False
)

print("Starting animation (close the window to save)...")
plt.show()

# --- SAVE THE GIF (after animation closes) ---
gif_output_path = "fourier_drawing.gif"
print(f"Saving animation to {gif_output_path}...")
ani.save(gif_output_path, writer='pillow', fps=50) 
print("Animation ended and GIF saved.")