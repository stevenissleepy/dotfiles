# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# bash history config
HISTSIZE=1000
HISTFILESIZE=2000
HISTCONTROL=ignoreboth # ignores duplicate lines and lines starting with space
shopt -s histappend # append to history, don't overwrite it

# check window size
shopt -s checkwinsize

# make less more friendly for non-text input files
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# enable programmable completion features
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# source dotfiles
[[ -f ~/.aliases ]] && source ~/.aliases
[[ -f ~/.path ]] && source ~/.path
[[ -f ~/.unique_config ]] && source ~/.unique_config

# starship
eval "$(starship init bash)"

# conda
if command -v conda &> /dev/null; then
    __conda_setup="$("$home/tools/anaconda3/bin/conda" 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "$HOME/tools/anaconda3/etc/profile.d/conda.sh" ]; then
            . "$HOME/tools/anaconda3/etc/profile.d/conda.sh"
        else
            export PATH="$HOME/tools/anaconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
fi
