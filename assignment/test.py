import subprocess
import os
print(os.getcwd())


test_files = {
    './data/test_argument_file.csv': './data/test_argument_file.csv',
    './data/test_argument_file_2.csv': './data/test_argument_file.csv',
    './data/test_argument_file_3': './data/test_argument_file.csv',
    './data/html_argument_file.html': './data/test_argument_file.csv',
    './data/empty_argument_file.csv': './data/test_argument_file.csv',
    './data/unreadable.txt': './data/test_argument_file.csv',
}

# Options to test with each file
options = ['-a', '-m', '-l', '-v', '-x', 'a', '-a -m']


# Function to run the command and print the output
def run_test(option, file_name):
    command = ["python", "locale.py", option, file_name]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, text=True)
    print(f"Output for option '{option}' and file '{file_name}':")
    print(result.stdout)
    print("\n--- End of Output ---\n")


# Run tests
for option in options:
    for file_name in test_files.keys():
        # Load the content from the file
        with open(file_name, 'r') as f:
            file_content = f.read()
        #print(f"Loaded content for file '{file_name}':\n{file_content}\n")

        # Run the test with the loaded content
        run_test(option, file_name)