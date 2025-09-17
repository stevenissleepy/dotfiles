import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 工作目录
tmp_dir = Path("/tmp")

# miniconda
miniconda_url = (
    f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
)
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
zshrc_path = Path.home() / ".zshrc"
zsh_alias_path = Path.home() / ".zsh_aliases"
zsh_path_path = Path.home() / ".zsh_path"

omz_url = "https://gitee.com/mirrors/oh-my-zsh.git"
omz_installer_url = "https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh"
omz_installer_path = tmp_dir / "omz_install.sh"
omz_path = Path.home() / ".oh-my-zsh"
omz_plugins_path = omz_path / "custom" / "plugins"
omz_plugins_urls = {
    "zsh-autosuggestions": "https://gitee.com/mirrors/zsh-autosuggestions.git",
    "zsh-syntax-highlighting": "https://gitee.com/mirrors/zsh-syntax-highlighting.git",
    "zsh-vi-mode": "https://gitee.com/mirrors_jeffreytse/zsh-vi-mode.git",
}
