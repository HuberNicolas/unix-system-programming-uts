
import sys
import os

# Function to read the file and parse its contents
def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
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
        return [f'No locales or charmaps in this language {language}']
    return [
        f'Language {language}:',
        f'Total number of locales: {len(locales)}',
        f'Total number of charmaps: {len(charmaps)}'
    ]

# Function to print version information
def version_info():
    # Placeholder for user's personal information
    return ['Your Name, Student ID, Friday 17 May 2024']

# Main function to process command-line arguments
def main():
    if len(sys.argv) not in [3, 4]:
        print(f'Incorrect usage.
Correct usage: {sys.argv[0]} option argument_file')
        sys.exit(1)

    option = sys.argv[1]
    file_path = sys.argv[2]

    if not os.path.isfile(file_path):
        print(f'Error: The file {file_path} does not exist or is not readable.')
        sys.exit(1)

    data = read_file(file_path)

    if option == '-a':
        for locale in list_locales(data):
            print(locale)
    elif option == '-m':
        for charmap in list_charmaps(data):
            print(charmap)
    elif option == '-l' and len(sys.argv) == 4:
        language = sys.argv[3]
        for line in language_info(data, language):
            print(line)
    elif option == '-v':
        for line in version_info():
            print(line)
    else:
        print(f'Error: Invalid option {option}')
        sys.exit(1)

if __name__ == '__main__':
    main()

def list_locales(argument_file):
    with open(argument_file, 'r') as file:
        locales = [line.strip().split(',')[2] for line in file if line.startswith('locale')]

    if locales:
        print("Available locales:")
        for locale in locales:
            print(locale)
    else:
        print("No locales available")

# Extend the main function to include the '-a' option
def main():
    if len(sys.argv) != 3:
        print("Usage: python locale.py option argument_file")
        sys.exit(1)

    option = sys.argv[1]
    argument_file = sys.argv[2]

    if check_file(argument_file):
        if option == '-a':
            list_locales(argument_file)
        
def list_charmaps(argument_file):
    with open(argument_file, 'r') as file:
        charmaps = [line.strip().split(',')[2] for line in file if line.startswith('charmap')]

    if charmaps:
        print("Available charmaps:")
        for charmap in charmaps:
            print(charmap)
    else:
        print("No charmaps available")

# Extend the main function to include the '-m' option
def main():
    if len(sys.argv) != 3:
        print("Usage: python locale.py option argument_file")
        sys.exit(1)

    option = sys.argv[1]
    argument_file = sys.argv[2]

    if check_file(argument_file):
        if option == '-a':
            list_locales(argument_file)
        elif option == '-m':
            list_charmaps(argument_file)
        # TODO: Implement other options (-l, -v)
        else:
            print("Invalid option")
            sys.exit(1)

if __name__ == "__main__":
    main()
# TODO: Implement other options (-l, -v)
        else:
            print("Invalid option")
            sys.exit(1)

if __name__ == "__main__":
    main()

def list_charmaps(argument_file):
    with open(argument_file, 'r') as file:
        charmaps = [line.strip().split(',')[2] for line in file if line.startswith('charmap')]

    if charmaps:
        print("Available charmaps:")
        for charmap in charmaps:
            print(charmap)
    else:
        print("No charmaps available")

# Updating the main function to include the '-m' option
def main():
    if len(sys.argv) != 3:
        print("Usage: python locale.py option argument_file")
        sys.exit(1)

    option = sys.argv[1]
    argument_file = sys.argv[2]

    if check_file(argument_file):
        if option == '-a':
            list_locales(argument_file)
        elif option == '-m':
            list_charmaps(argument_file)
        # TODO: Implement other options (-l, -v)
        else:
            print("Invalid option")
            sys.exit(1)

if __name__ == "__main__":
    main()

# Updating the main function to include error handling for incorrect syntax
def main():
    # Checking the number of arguments
    if len(sys.argv) < 3:
        print("Error: Missing arguments.")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Error: Too many arguments.")
        sys.exit(1)

    option = sys.argv[1]
    argument_file = sys.argv[2]

    # Valid options list
    valid_options = ['-a', '-m', '-l', '-v']

    if check_file(argument_file):
        if option in valid_options:
            if option == '-a':
                list_locales(argument_file)
            elif option == '-m':
                list_charmaps(argument_file)
            # TODO: Implement options '-l' and '-v'
        else:
            print(f"Error: Invalid option {option}.")
            sys.exit(1)

if __name__ == "__main__":
    main()
