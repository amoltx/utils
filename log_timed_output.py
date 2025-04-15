import sys
import datetime
import argparse

def timestamp_stdin_to_file(output_filename):
    """
    Reads lines from standard input, prepends a timestamp to each line,
    and writes the result to the specified output file.

    Args:
        output_filename (str): The name of the file to write the output to.
    """
    try:
        # Open the specified output file in write mode ('w').
        # Use a 'with' statement to ensure the file is automatically closed.
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            print(f"Reading from stdin and writing timestamped lines to '{output_filename}'...")
            print("Press Ctrl+D (Linux/macOS) or Ctrl+Z then Enter (Windows) to stop.")

            # Iterate through each line coming from standard input.
            for line in sys.stdin:
                # Get the current timestamp.
                now = datetime.datetime.now()
                # Format the timestamp (e.g., "2025-04-14 14:05:30.123456").
                timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")

                # Prepend the timestamp and a space to the original line.
                # The 'line' variable already includes the newline character.
                output_line = f"[{timestamp_str}] {line}"

                # Write the timestamped line to the output file.
                outfile.write(output_line)
                # Optionally, flush the buffer to ensure immediate writing.
                outfile.flush()

        print(f"\nFinished writing to '{output_filename}'.")

    except IOError as e:
        print(f"Error: Could not open or write to file '{output_filename}'. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Set up argument parser to get the output filename from the command line.
    parser = argparse.ArgumentParser(
        description="""Reads from stdin, prepends timestamps, and writes to a file.\n
        Example: echo -e "hello\nworld" | python3 log_timed_output.py
        """
    )
    parser.add_argument(
        "output_file",
        nargs='?', # Makes the argument optional
        default="timestamped_output.log", # Default filename if none is provided
        help="The path to the output file where timestamped lines will be written."
    )

    # Parse the command-line arguments.
    args = parser.parse_args()

    # Call the main function with the provided or default output filename.
    timestamp_stdin_to_file(args.output_file)

