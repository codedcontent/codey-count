import os
import pathlib

# An example of what the file path should look like
# Ensure the the slash '/' is forward and not backward '\'
# folderPath = 'C:/Users/.../filepath/'

folderPath = input('Provide the path to the folder to count from: ')

# The ignoreFolders contains folder name that you might want to ignore
ignoreFolders = ['.vscode', 'node_modules']

# The ignoreFoldersInput is your input
ignoreFoldersInput = input(' Provide a list a folders you don\'t wish to count from : ')
ignoreFolders.extend(ignoreFoldersInput.split(','))

# The ignoreFiles contains folder name that you might want to ignore
ignoreFiles = ['.env', '.gitignore', 'package-lock.json', 'package.json', '.eslintcache', 'README.md', 'todo.todo']

# The ignoreFilesInput is your input
ignoreFilesInput = input(' Provide a list a files you don\'t wish to count : ')
ignoreFiles.extend(ignoreFilesInput.split(','))


# The main function
def main():
    # List all the contents of the folder
    content = os.listdir(folderPath)

    # use a for loop to traverse all the folder contents
    for i in content:

        # If the content is a file
        if os.path.isfile(os.path.join(folderPath, i)) and i not in ignoreFiles:
            # count the lines of code in the file
            count_lines_of_code(os.path.join(folderPath, i))

        elif os.path.isdir(os.path.join(folderPath, i)) and i not in ignoreFolders:
            # traverse through the folders and search again
            traverse_folder(os.path.join(folderPath, i))


# Global variable to keep track of the lines of code
main_counter = 0

# Global variable to keep track of bad files
bad_files = []


# Function to count the lines of code for a file
def count_lines_of_code(file):
    # get the main counter
    global main_counter

    file_path = os.path.join(folderPath, file)

    # The counter to work within a loop
    sub_counter = 0
    try:
        with open(file_path) as f:
            # read the files content and count each line
            sub_counter = sum(1 for _ in f)
            # Increment the main counter
            main_counter += sub_counter
    except:
        print('Could not count this file', file.name, 'in ', file)
        bad_files.append((file, file.name))


    print(f'lines of code in {file.name} = {sub_counter}, total = {main_counter}')


def traverse_folder(folder):
    # Set the path of the folder to the new path
    new_path = folder

    # Using the pathLib module to work with folder directories
    directory = pathlib.Path(new_path)
    for file in directory.iterdir():
        if os.path.isfile(file) and file.name not in ignoreFiles:
            count_lines_of_code(file)
        elif os.path.isdir(file) and file.name not in ignoreFolders:
            # Call the traverse_folder function to continue traversing folders of folders
            traverse_folder(file)


# Start the program
if __name__ == '__main__':
    main()
    # Give summary
    print('\n\n\n')
    print(f'Counted a total of {main_counter} lines, encountered {len(bad_files)} BAD FILES')
    print('\n BAD FILES, are files that cannot be counted e.g binary files such as images or videos')

