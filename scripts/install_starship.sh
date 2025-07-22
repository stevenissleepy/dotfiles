#!/usr/bin/env bash
set -e

source "$(dirname "$0")/env.sh"

curl -sS https://starship.rs/install.sh | sh -s -- -y
stow -d "$DOTFILES_DIR" -t "$HOME" starship