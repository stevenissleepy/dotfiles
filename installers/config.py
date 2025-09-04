import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 工作目录
tmp_dir = Path("/tmp")

# miniconda
miniconda_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"
