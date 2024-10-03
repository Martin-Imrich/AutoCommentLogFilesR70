#!/bin/sh
#colors
RED="\e[31m"
GREEN="\e[32m"
ENDCOLOR="\e[0m"

#==============================================================================================
Help() {
    echo -e "Build IPC package\n"
    echo -e "buildPackage.sh -[h||c|p|m|b|a|A] [-s <sufix>]"
    echo -e "options:"
    echo -e "   $GREEN-h$ENDCOLOR: help message"
    echo -e "   no option: make"
    echo -e "   $GREEN-c$ENDCOLOR: make clear && make"
    echo -e "   $GREEN-p$ENDCOLOR: create app package"
    echo -e "   $GREEN-m$ENDCOLOR: copy package to WIP"
    echo -e "   $GREEN-i$ENDCOLOR: install copied packages"
    echo -e "   $GREEN-A$ENDCOLOR: install all packages (AllPacks.sh)"
    echo -e "   $GREEN-b$ENDCOLOR: build complete IPC package"
    echo -e "   $GREEN-a$ENDCOLOR: all steps (without -A)"
    echo -e "   $GREEN-s$ENDCOLOR: sufix MC-R6-YYMMDD_sufix (not implemented yet)"
}
#==============================================================================================

make_clear='N'
create_app_package='N'
move_app_package='N'
install_packages='N'
install_all_packages='N'
build_IPC_package='N'

while getopts "hcpmiAbas:" option; do
    case $option in
        h) # display help
            Help
            exit;;
        c) # make clear
            make_clear="Y";;
        p) # create app package
            create_app_package="Y";;
        m) # copy packages to WIP
            create_app_package="Y"
            move_app_package="Y";;
        i) # install packages copied packages in WIP
            create_app_package="Y"
            move_app_package="Y"
            install_packages="Y";;
        A) # clear already installed binaries and install all packages
            install_all_packages="Y";;
        b) # build package without make clear
            create_app_package="Y"
            move_app_package="Y"
            install_packages="Y"
            build_IPC_package="Y";;
        a) # all steps
            make_clear="Y"
            create_app_package="Y"
            move_app_package="Y"
            install_packages="Y"
            build_IPC_package="Y";;
        s) # sufix
            sufix=${OPTARG}
            ;;
        \?) #invalid option
            echo -e "$RED ERROR - Invalid option$ENDCOLOR"
            exit 1;;
    esac
done

# directiories
PROJECT_DIR=${PWD}
MCR7_DIR=$(dirname "$PROJECT_DIR")
RPACKS_DIR=$MCR7_DIR/RPacks

if test $install_all_packages == "Y"; then
    cd $RPACKS_DIR
    echo -e "\n\n$GREEN============ Install ALL packages ============$ENDCOLOR\n"
    sh AllPacks.sh
    if test ! $? == 0; then
        echo -e "$RED Error installing ALL packages $ENDCOLOR"
        exit 1
    fi
    cd $PROJECT_DIR
fi

# Make clean
if test $make_clear == "Y"; then
    echo -e "\n$GREEN============ Make clean ============$ENDCOLOR\n"
    make clean
    if test ! $? == 0; then
        echo -e "\n$RED ERROR: Make clean. Exiting $ENDCOLOR"
        exit 1
    fi
fi

# Build binary
echo -e "\n$GREEN============ Make ============$ENDCOLOR\n"
make
if test ! $? == 0; then
    echo -e "\n$RED ERROR: Make. Exiting $ENDCOLOR"
    exit 1
fi

# Build package
if test $create_app_package == "Y"; then
    projectName=${PWD##*/}
    echo -e "\n\n$GREEN============ Create package $projectName ============$ENDCOLOR\n"
    sh CreateInst-dev.sh
fi

# Create list of packages to copy from ./dist
if test $move_app_package == "Y"; then
    PACKAGE_DIR=$PROJECT_DIR/dist
    packageList=$(ls $PROJECT_DIR/dist)

    # Copy packages to RPacks/install
    if test ! -d $RPACKS_DIR; then
        echo -e "$RED $RPACKS_DIR does not exists $ENDCOLOR"
        exit 1
    fi
    RPACKS_INSTALL_DIR=$RPACKS_DIR/install
    echo -e "\n\n$GREEN============ Copy packages to $RPACKS_INSTALL_DIR ============$ENDCOLOR\n"
    for package in $packageList
    do
        echo Copy $package to $RPACKS_INSTALL_DIR
        cp $PACKAGE_DIR/$package $RPACKS_INSTALL_DIR
    done
fi

# Install copied package in RPacks
if test $install_packages == "Y"; then
    cd $RPACKS_DIR
    echo -e "\n\n$GREEN============ Install packages ============$ENDCOLOR\n"
    for package in $packageList
    do
        sh install/$package
        if test ! $? == 0; then
            echo -e "$RED Error installing $package package $ENDCOLOR"
            exit 1
        fi
    done
fi

# Build complete package for IPC
if test $build_IPC_package == "Y"; then
    echo -e "\n\n$GREEN============ Create final package ============$ENDCOLOR\n"
    sh inst-make-pck.sh -pMC-R6
fi