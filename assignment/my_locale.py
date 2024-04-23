# Disclaimer: During development, the name of the script was changed to my_locale.py
# locale.py is already a standard python library.

'''
    Author: Nicolas Hube
    Github: https://github.com/NicolasHuber
    Date: 15.04.2024
'''

'''
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

'''

# IMPORTS
import sys
import os
import typing


class File:
    def __init__(self, path: str, content: list[list[str]]):
        self.path = path
        self.content = content


class Locale:
    def __init__(self, locales: File | list[str] | str = None):
        if locales is None:
            self.locales = []
        if isinstance(locales, str):
            self.locales = [locales]
        if isinstance(locales, File):
            self.locales = locales.content
        else:
            self.locales = locales

    def add_locale(self, locale):
        self.locales.append(locale)

    def print_locale(self):
        if not self.locales:
            print("No locales available")
        else:
            for locale in self.locales:
                print(locale)


class Charmap:
    def __init__(self, charmaps=None):
        if charmaps is None:
            self.charmaps = []
        elif isinstance(charmaps, str):
            self.charmaps = [charmaps]
        elif isinstance(charmaps, File):
            self.charmaps = charmaps.content
        else:
            self.charmaps = charmaps

    def add_charmap(self, charmap: str):
        self.charmaps.append(charmap)

    def print_charmap(self):
        if not self.charmaps:
            print('No charmaps available')
        else:
            for charmap in self.charmaps:
                print(charmap)


# CONSTANTS
# TODO: Create Const class
CHARMAP_STR = 'charmap'
LOCALE_STR = 'locale'


# Function to read the file and parse its contents
def read_file(file_path: str) -> File | None:
    #   Exists
    #   is a file
    #   is readable

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f'Error: The file "{file_path}" does not exist.')
        return None

    # Check if the file_path is indeed a file
    if not os.path.isfile(file_path):
        print(f'Error: "{file_path}" is not a file.')
        return None

    # Open the file and read its contents
    try:
        with open(file_path, 'r') as file:
            parsed_data = []
            for line in file:
                # Strip whitespace from the ends and check if the line is not empty
                clean_line = line.strip()
                if clean_line:
                    # Split the line by commas and add to the list of parsed data
                    parsed_data.append(clean_line.split(','))
            return File(file_path, parsed_data)
    except IOError:
        # Handle the error if the file cannot be read
        print(f'Error: The file "{file_path}" cannot be read.')
        return None


# Function to list information about a specific language
def language_info(file: File, language: str) -> list[str] | None:
    # Seems a bit overkill to add another class for language, already
    # a bit overengineered
    # Initialize empty lists to store locale and charmap entries
    locales = []
    charmaps = []

    # Iterate through each row in the data
    for row in file.content:
        # Check if the row is a locale and matches the specified language
        if row[0] == LOCALE_STR and row[1] == language:
            locales.append(row)  # Add the entire row to the locales list

        # Check if the row is a charmap and matches the specified language
        elif row[0] == CHARMAP_STR and row[1] == language:
            charmaps.append(row)  # Add the entire row to the charmaps list

    # Check there are not locals and charmaps for speficied language
    if not locales and not charmaps:
        return [f'No locales and charmaps in this language']
    else:
        return [
            f'Language {language}:',
            f'Total number of locales: {len(locales)}',
            f'Total number of charmaps: {len(charmaps)}'
        ]


# Function to print version information: author, studid and submission date
def version_info() -> list[str]:
    return [
        'Nicolas Huber',
        25061944,
        'Friday 17 May 2024'
    ]


# Main function to process command-line arguments
def main() -> None:
    global language

    # python locale.py option argument_file
    # name of the python script that is executed: sys.argv[0], '0th argument'
    # option = sys.argv[1], 'first argument'
    # argument file = sys.argv[2], 'secon argument'

    # In the following, triple quotes ''' are used for multi-line strings
    # ==> we can include line breaks in the strings without using escape characters '\n'

    # Basic sanity checks on minimum arguments
    # We need at least 2 arguments, that means

    if len(sys.argv) < 3:
        print(f'''Incorrect usage.\nCorrect usage: {sys.argv[0]} -option [language] argument_file''')
        sys.exit(1)

    # Extract option from CLI
    option = sys.argv[1]

    # Futher checks based on option

    # Handle the -v option first since its a common case and simpel to check
    if option == '-v':
        if len(sys.argv) != 3:
            print(f'''Incorrect usage for version info. Correct usage: {sys.argv[0]} -v argument_file''')
            sys.exit(1)
        file_path = sys.argv[2]
        if not os.path.isfile(file_path):
            print(f'''Error: The file {file_path} does not exist or is not readable.''')
            sys.exit(1)
        for line in version_info():
            print(line)
        return

    # Handle -l for language-specific information with a requireent for 4 arguments

    # Distinguish 2 cases
    elif option == '-l':
        # Case1: specific language <language> is given
        if len(sys.argv) != 4:
            print(f"""Incorrect usage for language info. Correct usage: {sys.argv[0]} -l <language> argument_file""")
            sys.exit(1)
        language = sys.argv[2]
        file_path = sys.argv[3]
    else:
        # Case1: specific language <language> is not given
        if len(sys.argv) != 3:
            print(f'''Incorrect usage. Correct usage: {sys.argv[0]} -option argument_file''')
            sys.exit(1)
        file_path = sys.argv[2]

    # Check if the file exists and is readable
    if not os.path.isfile(file_path):
        print(f'''Error: The file {file_path} does not exist or is not readable.''')
        sys.exit(1)

    # Load the data from the file
    file = read_file(file_path)

    # Execute the appropriate option
    if option == '-a':
        locales = Locale(file)
        locales.print_locale()
    elif option == '-m':
        charmaps = Charmap(file)
        charmaps.print_charmap()
    elif option == '-l':
        for line in language_info(file, language):
            print(line)
    else:
        print(f'''Error: Invalid option {option}''')
        sys.exit(1)


if __name__ == '__main__':
    main()
# type: ignore
