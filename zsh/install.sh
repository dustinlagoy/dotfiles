#!/bin/bash
ln -s "$(pwd)/zshrc" "$HOME/.zshrc"
ln -s "$(pwd)/zprofile" "$HOME/.zprofile"
ln -s "$(pwd)/p10k.zsh" "$HOME/.p10k.zsh"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k
curl -sL https://github.com/junegunn/fzf/releases/download/v0.57.0/fzf-0.57.0-linux_amd64.tar.gz | tar -xz -f - -C ~/.local/bin
