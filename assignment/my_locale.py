# Disclaimer: During development, the name of the script was changed to my_locale.py
# locale.py is already a standard python library.

"""
    Author: Nicolas Huber
    GitHub: https://github.com/NicolasHuber
    Date: 15.04.2024
"""

"""
Fundamental note: your program is not expected to verify that file argument_file complies with the above specifications.
It will only be tested with _compliant_ files. 

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

# IMPORTS
import sys
import os


class File:
    def __init__(self, path: str, content: list[list[str]]):
        self.path = path
        self.content = content


# CONSTANTS
CHARMAP_STR = 'charmap'
LOCALE_STR = 'locale'

NO_CHARMAP_STR = 'No charmaps available'
NO_LOCALE_STR = 'No locales available'

NO_CHARMAP_AND_NO_LOCALE_STR = 'No locales or charmaps in this language'

SUCCESSFUL_EXIT_CODE = 0
UNSUCCESSFUL_EXIT_CODE = 1


# Function to read the file and parse its contents
def read_file(file_path: str) -> File | None:
    #   Exists
    #   is a file
    #   is readable

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f'Error: The file "{file_path}" does not exist.')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)

    # Check if the file_path is indeed a file
    if not os.path.isfile(file_path):
        print(f'Error: "{file_path}" is not a file.')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)

    # Check if file in file_path is readable
    # https://docs.python.org/3/library/os.html
    # https://docs.python.org/3/library/os.html#os.R_OK
    if not os.access(file_path, os.R_OK):
        print(f'Error: "{file_path}" is not readable.')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)


    # Open the file and read its contents
    try:
        with open(file_path, 'r') as file:
            parsed_data = []
            for line in file:
                # Strip whitespace from the ends and check if the line is not empty
                clean_line = line.strip()
                # Very important: Remove empty lines from content
                if clean_line:
                    # Split the line by commas and add to the list of parsed data
                    parsed_data.append(clean_line.split(','))
            return File(file_path, parsed_data)
    except IOError:
        # Handle the error if the file cannot be read
        print(f'Error: The file "{file_path}" cannot be read.')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)


# Function to print version information: author, studid and submission date
def version_info() -> list[str]:
    return [
        'Name: Huber',
        'Surname: Nicolas',
        'Student ID: 25061944',
        'Date of Completion: Friday 17 May 2024'
    ]


# Main function to process command-line arguments
def main() -> None:
    global language

    # python locale.py option argument_file
    # name of the python script that is executed: sys.argv[0], '0th argument'
    # option = sys.argv[1], 'first argument'
    # argument file = sys.argv[2], 'second argument'

    # In the following, triple quotes ''' are used for multi-line strings
    # ==> we can include line breaks in the strings without using escape characters '\n'

    # Basic sanity checks on minimum arguments
    # We need at least 2 arguments, that means

    if len(sys.argv) < 3:
        print(f'''Incorrect usage.\nCorrect usage: {sys.argv[0]} -option [language] argument_file''')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)

    # Extract option from CLI
    option = sys.argv[1]

    # Further checks based on option

    # Handle the -v option first since it's a common case and simpel to check
    if option == '-v':
        if len(sys.argv) != 3:
            print(f'''Incorrect usage for version info.\nCorrect usage: {sys.argv[0]} -v argument_file''')
            sys.exit(UNSUCCESSFUL_EXIT_CODE)
        file_path = sys.argv[2]
        # Load the data from the file
        read_file(file_path)
        for line in version_info():
            print(line)
        return

    # Handle -l for language-specific information with a requirement for 4 arguments

    # Distinguish 2 cases
    elif option == '-l':
        # Case1: specific language <language> is given
        if len(sys.argv) != 4:
            print(f'''Incorrect usage for language info.\nCorrect usage: {sys.argv[0]} -l <language> argument_file''')
            sys.exit(UNSUCCESSFUL_EXIT_CODE)
        language = sys.argv[2]
        file_path = sys.argv[3]
    else:
        # Case1: specific language <language> is not given
        if len(sys.argv) != 3:
            print(f'''Incorrect usage.\nCorrect usage: {sys.argv[0]} -option argument_file''')
            sys.exit(UNSUCCESSFUL_EXIT_CODE)
        file_path = sys.argv[2]

    # Load the data from the file
    file = read_file(file_path)

    # Execute the appropriate option
    if option == '-a':
        # Init Output
        locales = []
        if not file.content:
            print(NO_LOCALE_STR)
            sys.exit(SUCCESSFUL_EXIT_CODE)
        else:
            for row in file.content:
                if row[0] == LOCALE_STR:
                    # Store locale names in the list
                    locales.append(row[2])

            if locales:
                print('Available locales:')
                # Join all locales with newline and print once
                print('\n'.join(locales))
                sys.exit(SUCCESSFUL_EXIT_CODE)
            else:
                print(NO_LOCALE_STR)
                sys.exit(SUCCESSFUL_EXIT_CODE)
    elif option == '-m':
        # Init Output
        charmaps = []
        if file.content == '':
            print(NO_CHARMAP_STR)
            sys.exit(SUCCESSFUL_EXIT_CODE)
        else:
            for row in file.content:
                if row[0] == CHARMAP_STR:
                    # Store charmap names in the list
                    charmaps.append(row[2])
            if charmaps:
                # Print header
                print('Available charmaps:')
                # Join all charmaps with newline and print once
                print('\n'.join(charmaps))
                sys.exit(SUCCESSFUL_EXIT_CODE)
            else:
                print(NO_CHARMAP_STR)
                sys.exit(SUCCESSFUL_EXIT_CODE)

    elif option == '-l':
        # Init Output
        l_counter = 0
        c_counter = 0
        if file.content == '':
            print('NO_LOCALE_STR')
            sys.exit(SUCCESSFUL_EXIT_CODE)
        else:

            for row in file.content:
                if row[1] == language:
                    if row[0] == LOCALE_STR:
                        l_counter += 1
                    elif row[0] == CHARMAP_STR:
                        c_counter += 1
                    else:
                        pass  # this would be a bug

            if (l_counter == 0) and (c_counter == 0):
                print(NO_CHARMAP_AND_NO_LOCALE_STR)
                sys.exit(SUCCESSFUL_EXIT_CODE)
            else:
                print(f'Language {language}:')
                print(f'Total number of locales: {l_counter}')
                print(f'Total number of charmaps: {c_counter}')
                sys.exit(SUCCESSFUL_EXIT_CODE)

    else:
        print(f'''Error: Invalid option {option}''')
        sys.exit(UNSUCCESSFUL_EXIT_CODE)


if __name__ == '__main__':
    main()
