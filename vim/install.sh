#!/bin/bash
curl -sfLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
../link.sh "$(pwd)/vimrc" "$HOME/.vimrc"
../link.sh "$(pwd)/vimprofile" "$HOME/.vimprofile"
