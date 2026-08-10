#!/bin/bash
read -p "install full system configs? (y/N): " answer
if [[ "$answer" != [Yy]* ]]
then
    exit 0
fi
# Get list of directories
directories=$(ls -d */)
for directory in $directories
do
    # Run the install for each
    (cd $directory; ./install.sh) || echo "error running install.sh in $directory"
done
