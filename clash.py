import os
import shutil
import subprocess
from pathlib import Path

CLASH_URL = "https://gitee.com/stevenissleepy/kexueshangwang"
CLASH_PATH = Path.home() / "tools" / "clash"


def install_clash():
    """
    安装 clash
    """
    clash_url = CLASH_URL
    clash_path = CLASH_PATH

    # Clone the repository if it doesn't exist
    if not clash_path.exists():
        clash_path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", clash_url, str(clash_path)], check=True)

    # Copy .env file if it exists
    env_src = Path.cwd() / ".env"
    env_dst = clash_path / ".env"
    if env_src.exists():
        shutil.copy(env_src, env_dst)


def clash_start():
    """
    启动 clash 服务
    """
    clash_path = CLASH_PATH
    start_script = clash_path / "start.sh"
    subprocess.run(["sudo", "bash", str(start_script)], check=True)


def proxy_on():
    """
    开启代理
    """
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    os.environ["no_proxy"] = "127.0.0.1,localhost"
    os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
    os.environ["NO_PROXY"] = "127.0.0.1,localhost"


def clash_off():
    """
    关闭代理
    """
    os.environ.pop("http_proxy", None)
    os.environ.pop("https_proxy", None)
    os.environ.pop("no_proxy", None)
    os.environ.pop("HTTP_PROXY", None)
    os.environ.pop("HTTPS_PROXY", None)
    os.environ.pop("NO_PROXY", None)
