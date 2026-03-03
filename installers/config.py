import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 临时目录
tmp_dir = Path("/tmp")

# miniconda
miniconda_installer_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_installer_path = tmp_dir / "miniconda_installer.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
zsh_plugins = {
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
}

# starship
starship_installer_url = "https://starship.rs/install.sh"
starship_installer_path = tmp_dir / "starship_install.sh"

# neovim
neovim_glibc_min_version = "2.34"
neovim_arch = "x86_64" if arch in ["x86_64", "amd64"] else arch
neovim_arch = "arm64" if arch in ["aarch64", "arm64"] else arch
neovim_appimage_url = f"https://gh-proxy.org/https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-{neovim_arch}.appimage"
neovim_appimage_path = "/opt/nvim/nvim.appimage"
