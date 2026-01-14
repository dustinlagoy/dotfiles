#!/bin/bash
../link.sh "$(pwd)/zshrc" "$HOME/.zshrc"
../link.sh "$(pwd)/starship.toml" "$HOME/.config/starship.toml"
mkdir -p "$HOME/.config/zellij"
../link.sh "$(pwd)/zellij.kdl" "$HOME/.config/zellij/config.kdl"
curl -sS https://starship.rs/install.sh | sh -s -- -b $HOME/.local/bin --yes >/dev/null
mkdir -p ~/.local/bin
arch="x86_64"
curl -sL https://github.com/zellij-org/zellij/releases/latest/download/zellij-$arch-unknown-linux-musl.tar.gz | tar -xzf - -C ~/.local/bin
curl -sL https://github.com/junegunn/fzf/releases/download/v0.57.0/fzf-0.57.0-linux_amd64.tar.gz | tar -xz -f - -C ~/.local/bin
