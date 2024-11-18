from datetime import timedelta

import pytz
from celery import Celery, Task
from celery.schedules import crontab
from flask import Flask

from configs import mlchain_config


def init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    broker_transport_options = {}

    if mlchain_config.CELERY_USE_SENTINEL:
        broker_transport_options = {
            "master_name": mlchain_config.CELERY_SENTINEL_MASTER_NAME,
            "sentinel_kwargs": {
                "socket_timeout": mlchain_config.CELERY_SENTINEL_SOCKET_TIMEOUT,
            },
        }

    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        broker=mlchain_config.CELERY_BROKER_URL,
        backend=mlchain_config.CELERY_BACKEND,
        task_ignore_result=True,
    )

    # Add SSL options to the Celery configuration
    ssl_options = {
        "ssl_cert_reqs": None,
        "ssl_ca_certs": None,
        "ssl_certfile": None,
        "ssl_keyfile": None,
    }

    celery_app.conf.update(
        result_backend=mlchain_config.CELERY_RESULT_BACKEND,
        broker_transport_options=broker_transport_options,
        broker_connection_retry_on_startup=True,
        worker_log_format=mlchain_config.LOG_FORMAT,
        worker_task_log_format=mlchain_config.LOG_FORMAT,
        worker_hijack_root_logger=False,
        timezone=pytz.timezone(mlchain_config.LOG_TZ),
    )

    if mlchain_config.BROKER_USE_SSL:
        celery_app.conf.update(
            broker_use_ssl=ssl_options,  # Add the SSL options to the broker configuration
        )

    if mlchain_config.LOG_FILE:
        celery_app.conf.update(
            worker_logfile=mlchain_config.LOG_FILE,
        )

    celery_app.set_default()
    app.extensions["celery"] = celery_app

    imports = [
        "schedule.clean_embedding_cache_task",
        "schedule.clean_unused_datasets_task",
        "schedule.create_tidb_serverless_task",
        "schedule.update_tidb_serverless_status_task",
        "schedule.clean_messages",
    ]
    day = mlchain_config.CELERY_BEAT_SCHEDULER_TIME
    beat_schedule = {
        "clean_embedding_cache_task": {
            "task": "schedule.clean_embedding_cache_task.clean_embedding_cache_task",
            "schedule": timedelta(days=day),
        },
        "clean_unused_datasets_task": {
            "task": "schedule.clean_unused_datasets_task.clean_unused_datasets_task",
            "schedule": timedelta(days=day),
        },
        "create_tidb_serverless_task": {
            "task": "schedule.create_tidb_serverless_task.create_tidb_serverless_task",
            "schedule": crontab(minute="0", hour="*"),
        },
        "update_tidb_serverless_status_task": {
            "task": "schedule.update_tidb_serverless_status_task.update_tidb_serverless_status_task",
            "schedule": crontab(minute="30", hour="*"),
        },
        "clean_messages": {
            "task": "schedule.clean_messages.clean_messages",
            "schedule": timedelta(days=day),
        },
    }
    celery_app.conf.update(beat_schedule=beat_schedule, imports=imports)

    return celery_app
