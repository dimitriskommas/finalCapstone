# Inventory 

The Inventory program will read the data of a shoe store inventory from a text file and will allow the user to enter, view, extract, update and search it. 

## Table of Contents

- [Inventory](#inventory)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Install Visual Studio](#install-visual-studio)
    - [Install python-tabulate](#install-python-tabulate)
  - [Usage](#usage)
  - [License](#license)

## Installation

### Install Visual Studio

Please read the following instructions in full before following them:
1. Visit https://code.visualstudio.com/

2. Download the version of VS Code that matches your operating system (OS). Alternatively, you can follow the instructions stated at the following links for the corresponding operating system families:
    * macOS: https://code.visualstudio.com/docs/setup/mac
    * Linux: https://code.visualstudio.com/docs/setup/linux
    * Windows: https://code.visualstudio.com/docs/setup/windows
    
3. Unix-like operating systems such as macOS and Linux often come with a pre-installed version of Python. It is generally discouraged to use the distributions of Python that are shipped with macOS as they may either be outdated or have customisations that might give you issues further down the line. Please follow the guidelines at: https://code.visualstudio.com/docs/python/python-tutorial.
    * Ensure that if you are on Windows or macOS, you have installed the latest stable version of Python using the prescribed means on the link above.
    * Ensure that if you are on Linux and the prepackaged Python version is not the latest stable version, you get a package provider for your operating system that uses the latest stable version. Being behind by 1 or 2 minor versions is fine on operating systems such as Fedora. However, on operating systems such as Ubuntu, we strongly recommend that you use a PPA (Personal Package Archive) such as: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa.
    * For all operating systems, ensure that your environment paths are up-to-date with regards to your installation.
    * Per the guidelines linked above, ensure that you install the latest stable version of Microsoft???s Python extension available from https://marketplace.visualstudio.com/items?itemName=ms-python.python so that you get tooltips and other useful tooling that help you as your program.

### Install python-tabulate

You will also need to install the tabulate python library.

To install it, open the command line and run:

```bash
pip install tabulate
```

The command line utility will be installed as tabulate to bin on Linux (e.g. /usr/bin); or as tabulate.exe to Scripts in your Python installation on Windows (e.g. C:\Python39\Scripts\tabulate.exe).

## Usage

After you clone the repository you should be able to open it with Visual Studio.

Press the Run and Debug button from the left-hand side menu or press F5 when the inventory.py tab is open.
C:\Users\DimKo\OneDrive\??????????????\Software Engineer Bootcamp\T32\Images

![image](https://user-images.githubusercontent.com/18433880/210266247-926c5645-9956-401b-aec9-8bf7880a16c3.png)

Then a meesage will be printed in the terminal with several options for the user.

![image](https://user-images.githubusercontent.com/18433880/210267465-7102b884-a447-4620-90f4-14d76ed94712.png)

Then depending the option the user wants to use, they will have to type it.

For example, if they needs to check the total value of each product, they have to type value and press enter.

![image](https://user-images.githubusercontent.com/18433880/210267404-1a3fb90f-5920-4ced-8172-0f28517aa1ac.png)

If the user types the wrong option, an error message will be printed and they will be asked to try again.

![image](https://user-images.githubusercontent.com/18433880/210267648-907269d0-a9e8-4cfa-b0be-3ee155967c78.png)

## License

Dimitrios Kommas 
