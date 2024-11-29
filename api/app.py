import os
import sys

python_version = sys.version_info
if not ((3, 11) <= python_version < (3, 13)):
    print(f"Python 3.11 or 3.12 is required, current version is {python_version.major}.{python_version.minor}")
    raise SystemExit(1)

from configs import mlchain_config

if not mlchain_config.DEBUG:
    from gevent import monkey

    monkey.patch_all()

    import grpc.experimental.gevent

    grpc.experimental.gevent.init_gevent()

import json
import threading
import time
import warnings

from flask import Response

from app_factory import create_app

# DO NOT REMOVE BELOW
from events import event_handlers  # noqa: F401
from extensions.ext_database import db

# TODO: Find a way to avoid importing models here
from models import account, dataset, model, source, task, tool, tools, web  # noqa: F401

# DO NOT REMOVE ABOVE


warnings.simplefilter("ignore", ResourceWarning)

os.environ["TZ"] = "UTC"
# windows platform not support tzset
if hasattr(time, "tzset"):
    time.tzset()


# create app
app = create_app()
celery = app.extensions["celery"]

if mlchain_config.TESTING:
    print("App is running in TESTING mode")


@app.after_request
def after_request(response):
    """Add Version headers to the response."""
    response.headers.add("X-Version", mlchain_config.CURRENT_VERSION)
    response.headers.add("X-Env", mlchain_config.DEPLOY_ENV)
    return response


@app.route("/health")
def health():
    return Response(
        json.dumps({"pid": os.getpid(), "status": "ok", "version": mlchain_config.CURRENT_VERSION}),
        status=200,
        content_type="application/json",
    )


@app.route("/threads")
def threads():
    num_threads = threading.active_count()
    threads = threading.enumerate()

    thread_list = []
    for thread in threads:
        thread_name = thread.name
        thread_id = thread.ident
        is_alive = thread.is_alive()

        thread_list.append(
            {
                "name": thread_name,
                "id": thread_id,
                "is_alive": is_alive,
            }
        )

    return {
        "pid": os.getpid(),
        "thread_num": num_threads,
        "threads": thread_list,
    }


@app.route("/db-pool-stat")
def pool_stat():
    engine = db.engine
    return {
        "pid": os.getpid(),
        "pool_size": engine.pool.size(),
        "checked_in_connections": engine.pool.checkedin(),
        "checked_out_connections": engine.pool.checkedout(),
        "overflow_connections": engine.pool.overflow(),
        "connection_timeout": engine.pool.timeout(),
        "recycle_time": db.engine.pool._recycle,
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
