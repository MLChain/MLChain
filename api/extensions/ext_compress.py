from flask import Flask

from configs import mlchain_config


def init_app(app: Flask):
    if mlchain_config.API_COMPRESSION_ENABLED:
        from flask_compress import Compress

        compress = Compress()
        compress.init_app(app)
