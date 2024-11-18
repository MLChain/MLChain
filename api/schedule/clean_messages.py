import datetime
import time

import click
from werkzeug.exceptions import NotFound

import app
from configs import mlchain_config
from extensions.ext_database import db
from extensions.ext_redis import redis_client
from models.model import (
    App,
    Message,
    MessageAgentThought,
    MessageAnnotation,
    MessageChain,
    MessageFeedback,
    MessageFile,
)
from models.web import SavedMessage
from services.feature_service import FeatureService


@app.celery.task(queue="dataset")
def clean_messages():
    click.echo(click.style("Start clean messages.", fg="green"))
    start_at = time.perf_counter()
    plan_sandbox_clean_message_day = datetime.datetime.now() - datetime.timedelta(
        days=mlchain_config.PLAN_SANDBOX_CLEAN_MESSAGE_DAY_SETTING
    )
    page = 1
    while True:
        try:
            # Main query with join and filter
            messages = (
                db.session.query(Message)
                .filter(Message.created_at < plan_sandbox_clean_message_day)
                .order_by(Message.created_at.desc())
                .paginate(page=page, per_page=100)
            )

        except NotFound:
            break
        if messages.items is None or len(messages.items) == 0:
            break
        for message in messages.items:
            app = App.query.filter_by(id=message.app_id).first()
            features_cache_key = f"features:{app.tenant_id}"
            plan_cache = redis_client.get(features_cache_key)
            if plan_cache is None:
                features = FeatureService.get_features(app.tenant_id)
                redis_client.setex(features_cache_key, 600, features.billing.subscription.plan)
                plan = features.billing.subscription.plan
            else:
                plan = plan_cache.decode()
            if plan == "sandbox":
                # clean related message
                db.session.query(MessageFeedback).filter(MessageFeedback.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(MessageAnnotation).filter(MessageAnnotation.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(MessageChain).filter(MessageChain.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(MessageAgentThought).filter(MessageAgentThought.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(MessageFile).filter(MessageFile.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(SavedMessage).filter(SavedMessage.message_id == message.id).delete(
                    synchronize_session=False
                )
                db.session.query(Message).filter(Message.id == message.id).delete()
                db.session.commit()
    end_at = time.perf_counter()
    click.echo(click.style("Cleaned unused dataset from db success latency: {}".format(end_at - start_at), fg="green"))
