# Project Title

WIP - Work In Progress

## Description

Tool for building a sw package for Rotor-auto.

## Getting Started

### Important
Scripts for QNX needs LF line ending. Using CR-LF makes the final package buildable, but not installable on QNX system. Git has option **core.autocrlf** to download repository with different line endings.

#### Show git configuration
> git config --list --show-origin
* prints all git configurations with configuration files
#### Check **core.autocrlf** option
* **core.autocrlf** must be set to **input** ([more info here](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/))
* if the value is changed, repository must be cloned again

### Dependencies

Add to System variables:
* TO-DO: ./package_build folder is moved to to its separate repostory
* From ./package_build folder copy ./QNX650 and ./UTIL folders to C:/APPL/ directory.
* Add these two folders into your -> Environment, System variables, Path, in this order:
    * C:\APPL\UTIL
    * C:\APPL\QNX650\host\win32\x86\usr\bin

Create RPacks symbolic link:
* Enter a directory where wip project folder is located.
* Run commands in terminal (Command Prompt) as administrator:
    >mklink /d RPacks WIP
    * symbolic link created for RPacks <<===>> WIP

### Build a package

* Open the ./RPacks/ symbolic link to ./WIP/ folder
* Doubleclick on ./AllPacks-and-CreatePackage.bat to start a process of building a package.
* All files including CMC, section device files, etc are built into this package.
* Package is created e.g. MC-R6-240613.pck.

### Contribute

Section:
* add a .bin files related to section into ./SWDL/ folder
* modify properties of these files in ./SWDL/SWDLINFO.txt file

## Help

Any advise for common problems or issues.

## Authors

Contributors names and contact info

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details