import logging

from jsonschema import validate

from register_3_step.requests import Client
from register_3_step.models import ResponseModel

logger = logging.getLogger("api")


class SwaggerStore:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = '/register'
    POST_AUTH_USER = '/auth'
    POST_USER_INFO = '/user_info/'
    _STORE = '/store/'
    POST_STORE_ITEM = '/item/'
    GET_ALL_ITEMS = '/items'

    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def auth_user(self, body: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_AUTH_USER}", json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def add_user_info(self, user_id, body: dict, schema: dict, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_USER_INFO}{user_id}",
                                              headers={"Authorization": f"JWT {token}"}, json=body)

        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def add_new_store(self, store, body, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("POST", f"{self.url}{self._STORE}{store}",
                                              headers={"Authorization": f"JWT {token}"},
                                              json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_store(self, store, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("GET", f"{self.url}{self._STORE}{store}",
                                              headers={"Authorization": f"JWT {token}"})
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def post_item(self, name_item, body: dict, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_STORE_ITEM}{name_item}",
                                              headers={"Authorization": f"JWT {token}"}, json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_all_items(self, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("GET", f"{self.url}{self.GET_ALL_ITEMS}",
                                              headers={"Authorization": f"JWT {token}"})
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
