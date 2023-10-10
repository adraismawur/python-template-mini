***!!Replace this readme with a description of your project as soon as possible!!***

# python-template-1
Hi! This is a minimal template for Python projects. 
The main purpose of the template is to help you to organize your code in a nice way. 
However, it is not intended to teach you how to write good code. 
That part is up to you :)

The code included in this repository is in itself a small tutorial on how to structure your python code.  


### Table of contents:

- [Quick start](#quick-start)
- [What is included in this repository?](#what-is-included-in-this-repository)
- [Why should I use this?](#why-should-i-use-this)

## Quick start:

### Prerequisites

- A package/environment manager (e.g. [MiniConda](https://docs.conda.io/en/latest/miniconda.html))
- Git

### Download the files

1. On this GitHub page, click the **Code** dropdown button in the top-right
2. Click Download ZIP
3. Extract the files somewhere in a new directory

### Set up the repository (local only)

1. Open a shell in the directory where you have extracted the files
2. Create a [virtual environment](#why-do-i-need-an-environment-manager) using an environment manager.
   One convenient program is [MiniConda](https://docs.conda.io/en/latest/miniconda.html)
3. Assuming that you have (Mini)Conda installed, create a virtual environment: `conda create --name your_project_name python=3.11`
4. Enter the newly created environment with `conda activate your_project_name`.
   The prefix of the command prompt should switch to `(your_project_name)` to show the change in environment.
   If you need to leave the environment, do `conda deactivate`
5. Run `git init` to initialize the git repository
6. Edit the `pyproject.toml` file to add metadata on your project
7. Install your project in the virtual environment using `pip install -e .`.
   This will also install all packages/dependencies you may have listed in your `requirements.txt` file.
8. Run `pre-commit install` (installed by the previous command) to set up pre-commit
9. Edit the readme file to describe your project
10. Run `git add .` to stage all files
11. Run `Git commit -m "initial commit"` to make your first commit

This process ensures that the history of your repository is clean, and not tied to this GitHub repository in any way.

### Set up a remote repository (on GitHub)

1. Create a new repository of your own by going through the plus icon in the top right -> new repository.
   Or [click here](https://github.com/new)
2. Give your repository a nice name and description
3. Under the section "**Initialize this repository with**", do not add anything.
4. You are now presented with a few steps you can take. You can follow those under the section "**…or push an existing repository from the command line**":
```bash
git remote add origin git@github.com:[your_username]/[your_repository].git
git branch -M main
git push -u origin main
```

### Start coding!

Generally, it is recommended to have the starting point of your code in a file with the name `main.py` inside a folder with the name `your_project_name`.
In there, the `main()` function calls all other functions from separate folders (called modules).

Things to consider while you do so:
- Commit early, commit often
- Aim for ~300 lines of code max for a python file
- You do not have to use the template/ subfolder if you have only a few functions/files
- Have fun!


## Why should I use this?

It's difficult to write code. 
It can be even more difficult to write code that is easy to read and maintain. 
This template is designed to help you structure your python code in a way that is common for a lot of well-maintained Python projects, while not forcing any of the more difficult aspects of code mainenance on you. 

### An environment manager

Almost every Python program you write uses external modules/packages (e.g. Pandas, Numpy). 
These external programs are under constant development and come in different versions. 
Different programs may use different versions of the same module/package. 
For example Project_A uses pandas v1.8.0, while Project_B uses pandas v2.1.0. 
However, having multiple versions of the same program installed on your computer may lead to errors and general confusion.

This problem is solved with virtual environments: these represent "folders" in which specific versions of programs can be installed. 
For example, Project_A would have pandas v1.8.0 installed in its virtual environment, while Project_B would have pandas v2.1.0.

Virtual environments can also be easily removed after they are not needed anymore (including all the packages that they contain). 
This allows to keep your computer (the so-called base environment) clean.
Several environment managers are available. 
One example is Conda (or its lightweight version, MiniConda), which is widely used. 
More information on virtual environments can be found [here](https://realpython.com/python-virtual-environments-a-primer/).


## What is included in this repository?

- A [README](#a-readme-file) file
- A (copyleft) [license](#a-license)
- A basic [folder structure](#folder-structure)
- A [requirements.txt](#requirementstxt-file) file with essential packages
- [Pre-commit](#pre-commit), using:
  - [Black](#black)

### A README file

A README is the first point many people will go to to understand your project, and to figure out how to set up or install your program.

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

### `requirements.txt` file

A requirements file makes it easy for people to automatically install the same dependencies you used to develop and run your application. 
You can also fix your requirements to specific version numbers to ensure that people can use the exact same dependencies and re-produce your work.

### pre-commit

[pre-commit](https://pre-commit.com/), a Git [hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) added to this repository ensures a basic level of code style and prevents some minor issues. 
As the name implies, scripts configured in the hook will be run before attempting to commit changes to your (local) repository.
Since you (hopefully) commit early and often, pre-commit ensures that your code remains nicely stylized and readable.

Here, the only script pre-configured for pre-commit is Black.

### Black

[Black](https://github.com/psf/black) is a code formatter. 
Any code base that uses it will have a style that is the same no matter who wrote the code. 
A consistent code style makes it easier to read, maintain and expand on code.

#### Why does Black use spaces instead of tabs?

Pretty much all of Black's choices come from adhering to the [PEP8 Style guide](https://peps.python.org/pep-0008/).

Wherever it does not, the authors have made their own decisions and are just applying them consistently.

#### Why does Black limit lines to 88 characters?

PEP8 [recommends 79](https://peps.python.org/pep-0008/#maximum-line-length), but Black extends it to reduce average lines of code.

Additional context: 79 is a historical choice (small monitors could commonly support about 80 characters) as well as a practical one; Using a small character limit ensures that you can put multiple files next to each other on common screen sizes, which really helps in comparing files.


