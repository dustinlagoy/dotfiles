#!/bin/bash
ln -s "$(pwd)/gpg-agent.conf" "$HOME/.gnupg/"
mkdir -p "$HOME/.local/bin"
ln -s "$(pwd)/pinentry.sh" "$HOME/.local/bin/"
