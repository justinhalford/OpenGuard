def is_valid_permutation(nums):
    # Check if the list contains a permutation of numbers 1 to 7
    return sorted(nums) == list(range(1, 8))

def filter_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line by commas and strip spaces, then convert to integers
            try:
                numbers = [int(num.strip()) for num in line.split(',')]
            except ValueError:
                # If conversion fails, skip this line (e.g., non-numeric values)
                continue

            if is_valid_permutation(numbers):
                outfile.write(line)

# Example usage
input_file_path = 'gpt3.5_run10.txt'  # Replace with your input file path
output_file_path = 'gpt3_5_run10.txt' # Replace with your desired output file path
filter_file(input_file_path, output_file_path)
