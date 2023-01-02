# Inventory 

The Inventory program will read the data if an inventory from a text file and will allow the user to enter, view, extract, update and search the inventory of a shoe store. 

## Table of Contents
- [Inventory](#inventory)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Contributing](#contributing)
  * [License](#license)
  * [And a table of contents](#and-a-table-of-contents)
  * [On the right](#on-the-right)

## Installation

Install visual studio

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
    * Per the guidelines linked above, ensure that you install the latest stable version of Microsoft’s Python extension available from https://marketplace.visualstudio.com/items?itemName=ms-python.python so that you get tooltips and other useful tooling that help you as your program.

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
