#!/usr/bin/env bash
set -e

source "$(dirname "$0")/env.sh"

stow -d "$DOTFILES_DIR" -t "$HOME" vim