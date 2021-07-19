> 🚨 This package is no longer under development. If you wish to take over this project, please [get in touch](https://github.com/idleberg/discussion/discussions/2)!
> 
> # Inno Setup for Sublime Text

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/Inno%20Setup.svg?style=flat-square)](https://packagecontrol.io/packages/Inno%20Setup)
[![GitHub](https://img.shields.io/github/release/idleberg/sublime-innosetup.svg?style=flat-square)](https://github.com/idleberg/sublime-innosetup/releases)
[![Travis](https://img.shields.io/travis/idleberg/sublime-innosetup.svg?style=flat-square)](https://travis-ci.org/idleberg/sublime-innosetup)

[Inno Setup](http://www.jrsoftware.org/isinfo.php) syntax definitions, completions and build system for [Sublime Text](http://www.sublimetext.com/).

**Note**: This package is compatible with Sublime Text 3 ([Build 3103](http://www.sublimetext.com/blog/articles/sublime-text-3-build-3103) or higher). Click [here](https://github.com/idleberg/sublime-innosetup/tree/subl2) for a Sublime Text 2 version of this package.

![Screenshot](https://raw.githubusercontent.com/idleberg/sublime-innosetup/master/screenshot.png)

*Screenshot of Inno Setup in Sublime Text with [Hopscotch](https://github.com/idleberg/Hopscotch) color scheme*

## Installation

### Package Control

1. Make sure you already have [Package Control](https://packagecontrol.io/) installed
2. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Type *“Inno Setup”* and press <kbd>Enter</kbd>

### Using Git

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/sublime-innosetup.git 'Inno Setup'`

### Manual installation

1. Download the latest [stable release](https://github.com/idleberg/sublime-innosetup/releases)
2. Unzip the archive to your Sublime Text `Packages` directory

## Usage

### Completions

Auto-completion will always list all available flags for a command, the first flag displayed is always the default.

### Building

Building requires a properly installed Inno Setup, and to build on macOS/Linux you need [Wine](https://www.winehq.org/). You can build your script using the default <kbd>Super</kbd>+<kbd>b</kbd> shortcut or from selecting the build option in the Tools menu. Output files will be placed in the same folder as your input.

#### Windows

Make sure that Inno Setup is installed properly and that `ISCC.exe` is in your PATH [environment variable](http://superuser.com/a/284351/195953) (it *isn't* by default!) Use the *Legacy Windows* build variant if you can't run PowerShell 3.0 (or higher) scripts.

#### macOS / Linux

With Wine and Inno Setup properly installed, use the default shortcut <kbd>Super</kbd>+<kbd>b</kbd> to build your script.

### Linter

You can install a separate [linting package](https://packagecontrol.io/packages/SublimeLinter-contrib-iscc) to highlight errors in your InnoSetup script.

## License

This work is licensed under the [The MIT License](LICENSE).
