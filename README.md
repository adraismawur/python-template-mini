❗❗ Replace this readme with a description of your project as soon as possible ❗❗

# python-template-mini
Hi! This is a minimal template for Python projects. 
The main purpose of the template is to help you to organize your code in a nice way. 
However, it is not intended to teach you how to write good code. 
That part is up to you :)

The code included in this repository is in itself a small tutorial on how to structure your python code.  

### Python templates

<!-- <span style="font-size: 12pt; font-weight: bold;"> -->
|        | link | Focus                             |
|:------:|:----:|-----------------------------------|
| 🐍     | [Mini](https://github.com/adraismawur/python-template-mini) | File and code structure           |
| 🐍🐍   | [Midi](https://github.com/adraismawur/python-template-midi) | Requirements and packaging        |
| 🐍🐍🐍 | [Maxi](https://github.com/adraismawur/python-template-maxi) | Testing, Automatic formatting and checks   |
<!-- </span> -->


### Table of contents:

- [Quick start](#quick-start)
- [What is included in this repository?](#what-is-included-in-this-repository)
- [Why should I use this?](#why-should-i-use-this)

## Quick start:

### Prerequisites

❗ This template assumes you have installed and are somewhat familiar with:

- [Git (https://git-scm.com/)](https://git-scm.com/)  
    You should know how to add (stage) files, remove (unstage) files, commit, push and pull
- Python version 3  
    Any version marked 3.x.x is okay.
    If you are not sure what version of python is installed, run ```python --version``` in a terminal window.

### Set up the repository (local only)

❕Choose this if you are just starting out, or if you do not want to create a page on Github for your code.

1. On this GitHub page, click the **Code** dropdown button in the top-right
2. Click Download ZIP
3. Extract the files somewhere in a new directory
4. Open a shell in the directory where you have extracted the files
5. Edit the readme file to describe your project
6. Run `git add .` to stage all files
7. Run `Git commit -m "initial commit"` to make your first commit

### Set up a remote repository (on GitHub)

❕Choose this if you want to ensure your code is always saved online, or if you want to share your code.

1. Create a new repository of your own by pressing the green button in the top right named "use this template" -> Create a new repository.
   Or [click here](https://github.com/new?template_name=python-template-mini&template_owner=adraismawur)
2. Give your repository a nice name and description
3. Choose whether you want the repository to be public (anyone can see your code), or private.
4. Press "Create repository"

You will be taken to your own github repository page after a few seconds.
From here, you can make edits directly to your files, but it is more practical to download your repository to your local device. (cloning)

1. On your github repository page, click the green button with the text "Code" in the top-right
2. Copy the URL that starts with ```git@github.com:```
3. On your device, open a terminal and navigate to a folder where you want your project to be stored
4. Use the command ```git clone [git url from step 2]```

Your repository will now appear in the folder you navigated to in step 3

### Start coding!

Generally, it is recommended to have the starting point of your code in a file with the name `main.py` inside a folder with the name `your_project_name`.
In there, the `main()` function calls all other functions from separate folders (called modules).

Things to consider while you do so:

✅ Commit early, commit often  
✅ Aim for ~300 lines of code max for a python file  
✅ You do not have to use the template/ subfolder if you have only a few functions/files  
✅ Have fun!  


## Why should I use this?

It's difficult to write code. 
It can be even more difficult to write code that is easy to read and maintain. 
This template is designed to help you structure your python code in a way that is common for a lot of well-maintained Python projects, while not forcing any of the more difficult aspects of code mainenance on you. 

## What is included in this repository?

- A [README](#a-readme-file) file
- A (copyleft) [license](#a-license)
- A basic [folder structure](#folder-structure)
- A .gitignore file

### A README file

❕ A README is the first point many people will go to to understand your project, and to figure out how to set up or install your program.

You can put nearly anything you want in a README, but generally it is expected that the README file describes what your project is about and how you run your application.

Refer to [The markdown guide](https://www.markdownguide.org/basic-syntax) to see what you can do in `README.md` files. 
Or take a look at the `README.md` file in this repository!

Some of the elements that you definitely should consider including (if applicable) are:

- The name of your project
- What does your project do
- Minimal information on how to run it
- Small examples showcasing your project's main features
- Minimal information on how to install the software

### A license

You do not *need* a license. 
But if you do not include a license, you are the sole holder of rights to your code (standard copyright), and it is not allowed to contribute and share your code with other people without your permission.

If you want, you can choose a different license on https://choosealicense.com/. 
A popular and permissive open sources license is the [MIT License](https://opensource.org/license/mit/)

### Folder structure

You do not need this exact folder structure, but for larger projects it is highly recommended that you subdivide your code into submodules (subdirectories). 
It takes people very long to read through an entire file to find the specific code they are interested in editing, so collating your code by category into different files and functions is important.

If you are working with just a few functions, it is also OK to have a few python files in the root directory without any subdirectories.

### .gitignore

When writing code, it is common that you create large, temporary or otherwise unimportant files that you do not want to add to your repository.

Instead of having to select what you want to add or do not want to add to a commit, you can use this file to specify what files you want to ignore when making changes to your code.
Git ignores any file that matches a line written in the .gitignore file.

The asterisk (*) can be used as a wildcard to include any random text.
The double asterisk (**) is used to search recursively through folders, meaning it will go through all folders and subfolders based on a path.

The .gitignore file that is included in this directory was automatically generated by GitHub to include all common files generated in python projects.
Feel free to play around with this file, or replace it with your own needs if necessary.
