# zsh history
HISTFILE=$HOME/.zsh_history
HISTSIZE=50000
SAVEHIST=10000

setopt extended_history
setopt hist_expire_dups_first
setopt hist_ignore_dups
setopt hist_ignore_space
setopt hist_verify
setopt share_history

# editor
if command -v nvim &> /dev/null; then
    export VISUAL='nvim'
else
    export VISUAL='vim'
fi

# source dotfiles
[[ -f ~/.aliases ]] && source ~/.aliases
[[ -f ~/.path ]] && source ~/.path
[[ -f ~/.unique_config ]] && source ~/.unique_config

# Starship
eval "$(starship init zsh)"
export STARSHIP_CONFIG="$HOME/.config/starship/robbyrussell.toml"

# plugins 
source $HOME/.zsh/catppuccin_mocha-zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# tools
eval "$(zoxide init zsh --cmd j)" # zoxide

# conda
export PATH="$PATH:$HOME/tools/miniconda3/bin"
if command -v conda &> /dev/null; then
    __conda_setup="$("$home/tools/miniconda3/bin/conda" 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "$HOME/tools/miniconda3/etc/profile.d/conda.sh" ]; then
            . "$HOME/tools/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="$HOME/tools/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
fi
