#!/bin/bash
../link.sh "$(pwd)/gpg-agent.conf" "$HOME/.gnupg/gpg-agent.conf"
mkdir -p "$HOME/.local/bin"
../link.sh "$(pwd)/pinentry.sh" "$HOME/.local/bin/pinentry.sh"
