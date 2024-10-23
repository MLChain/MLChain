from flask_restful import Resource

from configs import mlchain_config
from controllers.service_api import api


class IndexApi(Resource):
    def get(self):
        return {
            "welcome": "Mlchain OpenAPI",
            "api_version": "v1",
            "server_version": mlchain_config.CURRENT_VERSION,
        }


api.add_resource(IndexApi, "/")
