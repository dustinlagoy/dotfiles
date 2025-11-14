#!/bin/bash
../link.sh "$(pwd)/zshrc" "$HOME/.zshrc"
../link.sh "$(pwd)/zprofile" "$HOME/.zprofile"
../link.sh "$(pwd)/p10k.zsh" "$HOME/.p10k.zsh"
mkdir -p "$HOME/.config/zellij"
../link.sh "$(pwd)/zellij.kdl" "$HOME/.config/zellij/config.kdl"
if [ -d ~/.powerlevel10k ]
then
  (cd ~/.powerlevel10k; git fetch --quiet --depth=1; git reset --quiet --hard origin/master)
else
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k
fi
mkdir -p ~/.local/bin
arch="x86_64"
curl -sL https://github.com/zellij-org/zellij/releases/latest/download/zellij-$arch-unknown-linux-musl.tar.gz | tar -xzf - -C ~/.local/bin
curl -sL https://github.com/junegunn/fzf/releases/download/v0.57.0/fzf-0.57.0-linux_amd64.tar.gz | tar -xz -f - -C ~/.local/bin
