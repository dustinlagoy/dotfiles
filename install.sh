#!/bin/bash
# Get list of directories
directories=$(ls -d */)
for directory in $directories
do
    # Run the install for each
    cd $directory
    ./install.sh
    cd ..
done
