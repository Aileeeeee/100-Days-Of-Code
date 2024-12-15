'''
Write a function that prompts the reader for an integer n and reads the first n lines of the
stocks.csv file. Include a creative way to handle cases where n is greater than the number of
lines available in the file.
'''
    
# Define function to read a specified number of lines from a CSV file
def read_csv(csv_file, n):
    if n < 1:
        print('Enter a positive integer for n')
        return []
    try:
        # Open the specified CSV file in read mode
        with open(csv_file, mode='r') as file:
            # Read all lines from the file into a list
            

        # Check if the requested number of lines exceeds the available lines
        if n > len(lines):
            # Raise an error if the requested lines are more than available
            raise IndexError(f'Requested for {n} lines, only {len(lines)} is available.')

    except FileNotFoundError:
        # Handle the case where the specified file does not exist
        print(f'The file {csv_file} was not found.')

    # Return the first n lines from the file, adjusting for zero-based indexing
    return lines[:n + 1]