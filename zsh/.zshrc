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
ZSH_THEME=""
eval "$(starship init zsh)"
export STARSHIP_CONFIG="$HOME/.config/starship/robbyrussell.toml"

# plugins 
source $HOME/.zsh/catppuccin_mocha-zsh-syntax-highlighting.zsh
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

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
