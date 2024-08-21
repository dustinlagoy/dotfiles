#!/bin/bash
# Get list of directories
directories=$(ls -d */)
for directory in $directories
do
    if [[ $directory == "graphical/" ]]
    then
        read -p "install graphical configs? (y/N): " gui
        if [[ "$gui" != [Yy]* ]]
        then
            continue
        fi
    fi
    # Run the install for each
    cd $directory
    ./install.sh
    cd ..
done
