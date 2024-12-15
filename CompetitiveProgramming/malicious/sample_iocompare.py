def write_to_file(output_data, filename="out.txt"):
    with open(filename, "w") as f:
        f.write(output_data)

def read_from_file(filename="in.txt"):
    with open(filename, "r") as f:
        return f.read()

def compare_output(output_data, sample_output_file="sample_output.txt"):
    with open(sample_output_file, "r") as f:
        sample_output = f.read()
    return output_data == sample_output

# Example usage:
input_data = read_from_file()
# Process the input_data to generate output_data
# ... (your code here) ...
output_data = "This is the output data"

write_to_file(output_data)

if compare_output(output_data):
  print("Output matches sample output.")
else:
  print("Output differs from sample output.")