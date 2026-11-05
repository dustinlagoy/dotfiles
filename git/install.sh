#!/bin/bash
../link.sh "$(pwd)/gitconfig" "$HOME/.gitconfig"
DELTA_VERSION=0.20.1
curl -sL https://github.com/dandavison/delta/releases/download/${DELTA_VERSION}/delta-${DELTA_VERSION}-x86_64-unknown-linux-gnu.tar.gz \
  | tar -xz -f - -C ~/.local/bin --strip-components=1 delta-${DELTA_VERSION}-x86_64-unknown-linux-gnu/delta
