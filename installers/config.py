import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 临时目录
tmp_dir = Path("/tmp")

# miniconda
miniconda_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
omz_installer_url = "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
omz_installer_path = tmp_dir / "omz_install.sh"
omz_path = Path.home() / ".oh-my-zsh"
omz_plugins_path = omz_path / "custom" / "plugins"
omz_plugins_urls = {
    "zsh-autosuggestions": "https://gitee.com/mirrors/zsh-autosuggestions.git",
    "zsh-syntax-highlighting": "https://gitee.com/mirrors/zsh-syntax-highlighting.git",
    "zsh-vi-mode": "https://gitee.com/mirrors_jeffreytse/zsh-vi-mode.git",
}

# starship
starship_installer_url = "https://starship.rs/install.sh"
starship_installer_path = tmp_dir / "starship_install.sh"

# neovim
neovim_arch = "x86_64" if arch in ["x86_64", "amd64"] else arch
neovim_arch = "arm64" if arch in ["aarch64", "arm64"] else arch
neovim_appimage_url = f"https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-{neovim_arch}.appimage"
neovim_appimage_path = "/opt/nvim/nvim.appimage"
