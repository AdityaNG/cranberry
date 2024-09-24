import os


class Settings:

    VNC_PORT: int = int(os.getenv("VNC_PORT", default="5900"))
    VNC_HOST: str = str(os.getenv("VNC_HOST", default="localhost"))

    SSH_PORT: int = int(os.getenv("SSH_PORT", default="2222"))
    SSH_HOST: str = str(os.getenv("SSH_HOST", default="localhost"))
    SSH_USERNAME: str = str(os.getenv("SSH_USERNAME", default="ubuntu"))
    SSH_PASSWORD: str = str(os.getenv("SSH_PASSWORD", default="ubuntu"))

    INSTALL_PATH: str = os.path.dirname(os.path.abspath(__file__))


settings = Settings()
