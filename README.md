# Code Counter

---

This is project is a python script that was written to help you count you lines of code

You no longer have to wonder how many lines of code you've written and try to count it with you hands

Ensure to read my documentation on how to use this script

---

## How To Use

- Ensure you have python installed
- After cloning the project just run the app
- You will be prompted to enter the file path to the directory you want to count
- You will be prompted to provide the a list of folders you don't want the script to search
- You will be prompted to provide a list of files you don't want the script to count
- After all the prompts the script will begin to count your every file and go through every folder that has been permitted

---

# Note

In the situation where the scripts starts counting and comes across a foreign file (A file it cannot count), such a file would be skipped and it will be counted as a BAD FILE

![Bad File Scenario](https://i.ibb.co/Hnz68hw/bad-files.png)

---

## Accessibility

```python
    # you can remove or add folder names to this list that you do not want the script to search
    ignoreFolders = ['.vscode', 'node_modules']

    # You can remove or add to this list file you want the script to count
    ignoreFiles = ['.env', '.gitignore', 'package-lock.json', 'package.json', '.eslintcache', 'README.md', 'todo.todo']

```

---

## License and Usage

© Mephors Ogechukwu [coddedContent](https://github.com/codedcontent "check out my other projects")

You may use the script to count lines of your code as you see fit
