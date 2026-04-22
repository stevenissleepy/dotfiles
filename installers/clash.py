import os
import shutil
import subprocess

from .config import tmp_dir, mihomo_url, mihomo_bin, clash_config_dir


class ClashInstaller:

    @staticmethod
    def install():
        """
        安装 clash
        """
        if shutil.which("mihomo") is not None:
            return

        archive_path = tmp_dir / "mihomo.gz"
        binary_path = tmp_dir / "mihomo"

        # 清理旧文件
        subprocess.run(["sudo", "rm", "-rf", str(archive_path)], check=True)
        subprocess.run(["sudo", "rm", "-rf", str(binary_path)], check=True)

        # 安装 mihomo
        subprocess.run(["curl", "-fsSL", mihomo_url, "-o", str(archive_path)], check=True)
        with binary_path.open("wb") as binary_file:
            subprocess.run(["gunzip", "-c", str(archive_path)], check=True, stdout=binary_file)
        subprocess.run(["sudo", "install", "-m", "755", str(binary_path), str(mihomo_bin)], check=True)

    @staticmethod
    def start(clash_url):
        clash_config_path = clash_config_dir / "config.yaml"
        clash_log_path = tmp_dir / "clash.log"
        subprocess.run(["mkdir", "-p", str(clash_config_dir)], check=True)
        subprocess.run(["sudo", "fuser", "-s", "-k", "7890/tcp"], check=False)
        subprocess.run(["curl", "-fsSL", clash_url, "-o", str(clash_config_path)], check=True)

        # mihomo 是常驻进程，这里后台拉起，避免阻塞安装流程。
        with clash_log_path.open("ab") as log_file:
            subprocess.Popen(
                ["mihomo", "-f", str(clash_config_path)],
                stdout=log_file,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )

    @staticmethod
    def stop():
        subprocess.run(["sudo", "fuser", "-s", "-k", "7890/tcp"], check=False)

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
