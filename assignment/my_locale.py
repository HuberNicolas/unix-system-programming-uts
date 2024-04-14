import sys
import os

"""
Requirements for the locale.py program:

1. Program Name:
   - Must be named locale.py.

2. Invocation Command:
   - Command format: python locale.py option argument_file
   - 'option' refers to one of the predefined command options.
   - 'argument_file' refers to the file name containing data, format specified below.

3. File Format (argument_file):
   - Consists of lines with three comma-separated fields: type, language, filename.
   - 'type' must be "locale" or "charmap".
   - 'language' and 'filename' include letters, digits, underscores, and dots.

4. Option -a:
   - List filenames of all locales.
   - Output "Available locales:" followed by filenames or "No locales available" if none.

5. Option -m:
   - List filenames of all charmaps.
   - Output "Available charmaps:" followed by filenames.

6. Option -l [language]:
   - Provide details of locales and charmaps for a specified language.
   - Output specifics on counts of locales and charmaps or a message if none exist.

7. Option -v:
   - Print author's details. Note: argument_file is still required but not used.

8. Exclusive Options:
   - Only one option can be used at a time.

9. Error Handling:
   - Specific messages for incorrect syntax or command usage. Examples include missing file arguments or incorrect options.

"""


# Function to read the file and parse its contents
def read_file(file_path):
    # Check if argument_file
    #   exists
    #   is a file
    #   is readable

    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip().split(',') for line in data if line.strip()]


# Function to list available locales
def list_locales(data):
    locales = [entry[2] for entry in data if entry[0] == 'locale']
    return locales if locales else ['No locales available']


# Function to list available charmaps
def list_charmaps(data):
    charmaps = [entry[2] for entry in data if entry[0] == 'charmap']
    return charmaps if charmaps else ['No charmaps available']


# Function to list information about a specific language
def language_info(data, language):
    locales = [entry for entry in data if entry[0] == 'locale' and entry[1] == language]
    charmaps = [entry for entry in data if entry[0] == 'charmap' and entry[1] == language]
    if not locales and not charmaps:
        return [f'No locales or charmaps in this language']
    return [
        f'Language {language}:',
        f'Total number of locales: {len(locales)}',
        f'Total number of charmaps: {len(charmaps)}'
    ]


# Function to print version information
def version_info():
    return [
        'Nicolas Huber',
        25061944,
        'Friday 17 May 2024'
    ]


# Main function to process command-line arguments
def main():
    # Basic sanity checks on minimum arguments
    if len(sys.argv) < 3:
        print('Incorrect usage.\nCorrect usage: {} -option [language] argument_file'.format(sys.argv[0]))
        sys.exit(1)

    option = sys.argv[1]

    # Handle the -v option first since it's a common case and simple to check
    if option == '-v':
        if len(sys.argv) != 3:
            print("""Incorrect usage for version info. Correct usage: {} -v argument_file""".format(sys.argv[0]))
            sys.exit(1)
        file_path = sys.argv[2]
        if not os.path.isfile(file_path):
            print("""Error: The file {} does not exist or is not readable.""".format(file_path))
            sys.exit(1)
        for line in version_info():
            print(line)
        return

    # Handle -l for language-specific information with a requirement for 4 arguments
    elif option == '-l':
        if len(sys.argv) != 4:
            print("""Incorrect usage for language info. Correct usage: {} -l <language> argument_file""".format(
                sys.argv[0]))
            sys.exit(1)
        language = sys.argv[2]
        file_path = sys.argv[3]
    else:
        if len(sys.argv) != 3:
            print("""Incorrect usage. Correct usage: {} -option argument_file""".format(sys.argv[0]))
            sys.exit(1)
        file_path = sys.argv[2]

    # Check if the file exists and is readable
    if not os.path.isfile(file_path):
        print("""Error: The file {} does not exist or is not readable.""".format(file_path))
        sys.exit(1)

    # Load the data from the file
    data = read_file(file_path)

    # Execute the appropriate option
    if option == '-a':
        for locale in list_locales(data):
            print(locale)
    elif option == '-m':
        for charmap in list_charmaps(data):
            print(charmap)
    elif option == '-l':
        for line in language_info(data, language):
            print(line)
    else:
        print("""Error: Invalid option {}""".format(option))
        sys.exit(1)


if __name__ == '__main__':
    main()
# type: ignore
