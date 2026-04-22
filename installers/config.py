import tempfile
import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 临时目录
tmp_dir = tempfile.mkdtemp(prefix="dotfiles-")
tmp_dir = Path(tmp_dir)

# clash
mihomo_arch = "amd64" if arch in ["x86_64", "amd64"] else arch
mihomo_arch = "arm64" if arch in ["aarch64", "arm64"] else arch
mihomo_url = f"https://github.com/MetaCubeX/mihomo/releases/download/v1.19.24/mihomo-linux-{mihomo_arch}-v3-v1.19.24.gz"
mihomo_bin = Path("/usr/local/bin/mihomo")
clash_config_dir = Path.home() / ".config" / "mihomo" / "configs"

# miniconda
miniconda_installer_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_installer_path = tmp_dir / "miniconda_installer.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
zsh_plugins = {
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
}

