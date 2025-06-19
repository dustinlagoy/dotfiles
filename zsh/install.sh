#!/bin/bash
../link.sh "$(pwd)/zshrc" "$HOME/.zshrc"
../link.sh "$(pwd)/zprofile" "$HOME/.zprofile"
../link.sh "$(pwd)/p10k.zsh" "$HOME/.p10k.zsh"
if [ -d ~/.powerlevel10k ]
then
  (cd ~/.powerlevel10k; git fetch --quiet --depth=1; git reset --quiet --hard origin/master)
else
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k
fi
mkdir -p ~/.local/bin
curl -sL https://github.com/junegunn/fzf/releases/download/v0.57.0/fzf-0.57.0-linux_amd64.tar.gz | tar -xz -f - -C ~/.local/bin
