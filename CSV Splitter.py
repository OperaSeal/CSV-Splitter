import csv
import os

try:
    path = r"C:\Users\HHoover\Downloads"
    files = os.listdir(path)
    # Filter to keep only .csv files and get their full paths
    csv_files = [f for f in files if f.endswith('.csv')]
    paths = [os.path.join(path, f) for f in csv_files]
except Exception as e:
    print(f"Error accessing directory: {e}")
    input("Press Enter to exit...")
    exit()

# Check if there are any CSV files
if not paths:
    print("No CSV files found in the current directory.")
else:
    # Find the most recently modified CSV file
    recent = max(paths, key=os.path.getmtime)

    # Specify the output file name and path
    output_file = r"C:\Users\HHoover\Downloads\result.csv"  # Change this path if needed

    # Read the recent CSV file and write the selected columns to a new file
    try:
        with open(recent, "r", newline='', encoding='utf-8') as source:  # Specify encoding here
            rdr = csv.reader(source)
            with open(output_file, "w", newline='', encoding='utf-8') as result:  # Specify output file
                wtr = csv.writer(result)
                for r in rdr:
                    # Write columns 1 (0), 2 (1), 4 (3), and 9 (8) to the result
                    try:
                        wtr.writerow((r[0], r[1], r[3], r[8]))  # Indexing is zero-based
                    except IndexError:
                        print(f"Row skipped due to insufficient columns: {r}")
    except Exception as e:
        print(f"Error processing file {recent}: {e}")

    print(f"The most recently modified CSV file is: {recent}")
    print(f"Results saved to: {output_file}")

input("Press Enter to continue...")