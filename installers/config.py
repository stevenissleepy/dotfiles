import tempfile
import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 临时目录
tmp_dir = tempfile.mkdtemp(prefix="dotfiles-")
tmp_dir = Path(tmp_dir)

# miniconda
miniconda_installer_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_installer_path = tmp_dir / "miniconda_installer.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
zsh_plugins = {
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
}

