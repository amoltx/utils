import sys
import datetime
import argparse

def timestamp_stdin_block_to_file(output_filename):
    """
    Reads all lines from standard input, writes a single timestamp,
    and then writes all the original input lines to the specified output file.

    Args:
        output_filename (str): The name of the file to write the output to.
    """
    try:
        print("Reading all lines from stdin...")
        print("Press Ctrl+D (Linux/macOS) or Ctrl+Z then Enter (Windows) when done.")

        # Read all lines from standard input into a list.
        # Each element in 'lines' will include its trailing newline character.
        lines = sys.stdin.readlines()

        print(f"Finished reading stdin. Writing timestamp and content to '{output_filename}'...")

        # Open the specified output file in write mode ('w').
        # Use a 'with' statement to ensure the file is automatically closed.
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            # Get the current timestamp (after reading is complete).
            now = datetime.datetime.now()
            # Format the timestamp (e.g., "2025-04-14 14:05:30.123456").
            timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")

            # Write the timestamp header to the file.
            outfile.write(f"--- Logged at: {timestamp_str} ---\n")
            outfile.write("\n") # Add a blank line for separation

            # Write all the original lines read from stdin to the file.
            # writelines efficiently writes a list of strings.
            outfile.writelines(lines)

        print(f"Finished writing to '{output_filename}'.")

    except IOError as e:
        print(f"Error: Could not open or write to file '{output_filename}'. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Set up argument parser to get the output filename from the command line.
    parser = argparse.ArgumentParser(
        description="Reads all stdin, writes a timestamp, then writes stdin content to a file."
    )
    parser.add_argument(
        "output_file",
        nargs='?', # Makes the argument optional
        default="timestamped_block_output.log", # Default filename if none is provided
        help="The path to the output file where the timestamp and content will be written."
    )

    # Parse the command-line arguments.
    args = parser.parse_args()

    # Call the main function with the provided or default output filename.
    timestamp_stdin_block_to_file(args.output_file)
