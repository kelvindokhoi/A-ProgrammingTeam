import cv2
import svgwrite
import numpy as np
import os
from scipy.interpolate import splprep, splev

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def remove_near_duplicates(points, tolerance=1.0):
    """Remove points that are too close to each other."""
    if len(points) < 2:
        return points
    unique_points = [points[0]]
    for p in points[1:]:
        if np.linalg.norm(p - unique_points[-1]) > tolerance:
            unique_points.append(p)
    return np.array(unique_points)

def clamp_svg_size(width, height, max_size=8192):
    """Clamp SVG width and height to a maximum value to avoid svgwrite errors."""
    scale_factor = min(max_size / width, max_size / height, 1.0)
    return int(width * scale_factor), int(height * scale_factor), scale_factor

def image_to_svg(image_path, svg_path, scale=4.0, simplify_tolerance=5.0, resolution_factor=10.0, max_svg_size=8192):
    """
    Convert an image to an SVG file with higher resolution, but clamp output size
    to ensure compatibility with svgwrite and SVG viewers.
    """
    try:
        # Load image and upscale for higher detail
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Failed to load image: {image_path}")

        # Resize the image to increase resolution
        height, width = img.shape[:2]
        new_width = int(width * resolution_factor)
        new_height = int(height * resolution_factor)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise (adjust kernel size for larger image)
        blur_kernel_size = (5, 5) if resolution_factor <= 2 else (7, 7)
        blurred = cv2.GaussianBlur(gray, blur_kernel_size, 0)
        
        # Use adaptive thresholding to better separate character from background
        thresh_block_size = 11 if resolution_factor <= 2 else 15
        thresh = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, thresh_block_size, 2
        )

        # Apply morphological operations to clean up the thresholded image
        kernel_size = (3, 3) if resolution_factor <= 2 else (5, 5)
        kernel = np.ones(kernel_size, np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

        # Find contours from the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # Calculate SVG output size and clamp if necessary
        svg_width = int(new_width * scale)
        svg_height = int(new_height * scale)
        orig_svg_width, orig_svg_height = svg_width, svg_height
        svg_width, svg_height, clamp_factor = clamp_svg_size(svg_width, svg_height, max_svg_size)
        # print(f"SVG dimensions: width={svg_width}, height={svg_height} (original: {orig_svg_width}x{orig_svg_height}, clamp factor: {clamp_factor:.4f})")
        dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(f"{svg_width}px", f"{svg_height}px"))
        dwg.viewbox(0, 0, svg_width, svg_height)

        # Process each contour
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # Adjust area filter for resized image
            if area < 1000 * (resolution_factor**2) or area > (new_width * new_height * 0.2):
                continue

            # Simplify contour to reduce points
            cnt = cv2.approxPolyDP(cnt, simplify_tolerance, closed=True)
            points = cnt.squeeze()
            if len(points.shape) != 2 or len(points) < 4:
                continue

            # Remove near-duplicate points (adjust tolerance for higher resolution)
            points = remove_near_duplicates(points, tolerance=1.0 * resolution_factor)
            if len(points) < 4:
                continue

            # Ensure the first and last points are not identical
            if np.all(points[0] == points[-1]):
                points = points[:-1]

            # Manually handle periodicity by appending the first point
            if len(points) >= 4:
                points = np.vstack((points, points[0]))

            # Smooth contour using spline interpolation with more points
            smooth_points = points
            if len(points) >= 4:
                try:
                    tck, u = splprep([points[:, 0], points[:, 1]], s=simplify_tolerance, k=3)
                    u_fine = np.linspace(0, 1, len(points) * 5)
                    x_smooth, y_smooth = splev(u_fine, tck)
                    smooth_points = np.vstack((x_smooth, y_smooth)).T
                except Exception as e:
                    print(f"Warning: Spline interpolation failed for contour: {e}")

            # Apply clamp factor to all coordinates to fit actual SVG size
            scaled_points = smooth_points * scale * clamp_factor

            # Start building SVG path
            path_data = []
            first_point = scaled_points[0]
            path_data.append(f"M {first_point[0]:.2f},{first_point[1]:.2f}")

            # Use linear segments for the path
            for i in range(1, len(scaled_points)):
                p1 = scaled_points[i]
                path_data.append(f"L {p1[0]:.2f},{p1[1]:.2f}")
            
            # Close the path
            path_data.append("Z")

            # Create path with data, no fill (outline only)
            dwg.add(dwg.path(
                d=" ".join(path_data),
                fill='none',
                stroke='black',
                stroke_width=0.5,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))

        # Save the SVG file
        dwg.save()
        print(svg_path)

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

if __name__ == "__main__":
    try:
        with open('info.txt', 'r') as f:
            image_name = f.readline().strip()
        
        input_image = os.path.join('image', image_name)
        output_svg = os.path.join('svg', f"{os.path.splitext(image_name)[0]}.svg")
        
        # Ensure output directory exists
        os.makedirs('svg', exist_ok=True)
        
        if not os.path.exists(input_image):
            print(f"Image file '{input_image}' not found.")
        else:
            # You may tune scale, simplify_tolerance, resolution_factor
            image_to_svg(input_image, output_svg, scale=4.0, simplify_tolerance=5.0, resolution_factor=2.0, max_svg_size=8192)
    
    except FileNotFoundError:
        print("Error: info.txt not found.")
    except Exception as e:
        print(f"Error: {str(e)}")