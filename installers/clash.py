import os
import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import (
    tmp_dir,
    mihomo_url,
    mihomo_bin_dir,
    mihomo_config_dir,
    mihomo_service_dir,
    mihomo_service_content,
)


class ClashInstaller:

    @staticmethod
    def install():
        """
        安装 clash
        """
        # 安装 mihomo 内核
        if shutil.which("mihomo") is None:
            Installer.info("Installing clash kernel (mihomo)...")
            archive_path = tmp_dir / "mihomo.gz"
            mihomo_bin = mihomo_bin_dir / "mihomo"
            mihomo_bin_tmp = tmp_dir / "mihomo"

            subprocess.run(["sudo", "rm", "-rf", str(archive_path)], check=True)
            subprocess.run(["sudo", "rm", "-rf", str(mihomo_bin_tmp)], check=True)
            subprocess.run(["curl", "-fL", mihomo_url, "-o", str(archive_path)], check=True)
            with mihomo_bin_tmp.open("wb") as binary_file:
                subprocess.run(["gunzip", "-c", str(archive_path)], check=True, stdout=binary_file)
            subprocess.run(["sudo", "install", "-m", "755", str(mihomo_bin_tmp), str(mihomo_bin)], check=True)

        # 创建 mihomo service
        srv_file = mihomo_service_dir / "mihomo.service"
        srv_file_tmp = tmp_dir / "mihomo.service"
        Installer.info("Creating clash service...")
        with Path(srv_file_tmp).open("w", encoding="utf-8") as file:
            file.write(mihomo_service_content)
        subprocess.run(["sudo", "mkdir", "-p", str(mihomo_service_dir)], check=True)
        subprocess.run(["sudo", "install", "-m", "644", str(srv_file_tmp), str(srv_file)], check=True)

    @staticmethod
    def start(clash_url):
        """
        启动 mihomo service
        """
        Installer.info("Starting clash service...")
        config_file = mihomo_config_dir / "config.yaml"
        config_file_tmp = tmp_dir / "config.yaml"
        subprocess.run(["curl", "-fsSL", clash_url, "-o", str(config_file_tmp)], check=True)
        subprocess.run(["sudo", "mkdir", "-p", str(mihomo_config_dir)], check=True)
        subprocess.run(["sudo", "install", "-m", "644", str(config_file_tmp), str(config_file)], check=True)
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "mihomo.service"], check=True)

    @staticmethod
    def stop():
        subprocess.run(["sudo", "systemctl", "stop", "mihomo.service"], check=True)

    @staticmethod
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

    @staticmethod
    def proxy_off():
        """
        关闭代理
        """
        os.environ.pop("http_proxy", None)
        os.environ.pop("https_proxy", None)
        os.environ.pop("no_proxy", None)
        os.environ.pop("HTTP_PROXY", None)
        os.environ.pop("HTTPS_PROXY", None)
        os.environ.pop("NO_PROXY", None)
