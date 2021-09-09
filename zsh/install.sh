#!/bin/bash
ln -s "$(pwd)/zshrc" "$HOME/.zshrc"
ln -s "$(pwd)/zprofile" "$HOME/.zprofile"
ln -s "$(pwd)/p10k.zsh" "$HOME/.p10k.zsh"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k
