from flask import Flask

from configs import mlchain_config


def init_app(app: Flask):
    if mlchain_config.RESPECT_XFORWARD_HEADERS_ENABLED:
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.wsgi_app = ProxyFix(app.wsgi_app)
