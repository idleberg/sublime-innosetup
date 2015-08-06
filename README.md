# Inno Setup for Sublime Text

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![GitHub tag](https://img.shields.io/github/tag/idleberg/InnoSetup-Sublime-Text.svg?style=flat-square)](https://github.com/idleberg/InnoSetup-Sublime-Text/tags)
[![Travis](https://img.shields.io/travis/idleberg/InnoSetup-Sublime-Text.svg?style=flat-square)](https://travis-ci.org/idleberg/InnoSetup-Sublime-Text)

[Inno Setup](http://www.jrsoftware.org/isinfo.php) syntax definitions, completions and build system for [Sublime Text](http://www.sublimetext.com/).

![Screenshot](https://raw.githubusercontent.com/idleberg/InnoSetup-Sublime-Text/master/screenshot.png)

*Screenshot of Inno Setup in Sublime Text with [Hopscotch](https://github.com/idleberg/Hopscotch) color scheme*

## Installation

### Package Control

1. Make sure you already have [Package Control](http://wbond.net/sublime_packages/package_control/) installed
2. Choose *Install Package* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Select *Inno Setup* and press <kbd>Enter</kbd>

### GitHub

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/InnoSetup-Sublime-Text.git 'Inno Setup'`

## Usage

### Completions

Auto-completion will always list all available flags for a command, the first flag displayed is always the default.

### Building

Building requires a properly installed Inno Setup, and to build on Unix you need [Wine](https://www.winehq.org/). You can build your script using the default <kbd>Super</kbd>+<kbd>b</kbd> shortcut or from selecting the build option in the Tools menu. Output files will be placed in the same folder as your input.

#### Windows

Should the build system be unable to locate the compiler, you should probably re-install Inno Setup to make sure required registry keys are created. Alternatively, you can specify the install location in the environment variable `%INNO_HOME%`.

#### Unix

On Unix systems, you might have to make the build script executable:

```bash
# cd to Sublime Text/Packages/Inno Setup
chmod +x inno-build.sh
```

Use the default shortcut <kbd>Super</kbd>+<kbd>b</kbd> to build scripts.

## License

The MIT License (MIT)

Copyright (c) 2013 Jan T. Sott

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/InnoSetup-Sublime-Text) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`