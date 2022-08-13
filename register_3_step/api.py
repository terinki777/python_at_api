# api.py
import logging
from jsonschema import validate

from register_3_step.requests import Client
from register_3_step.models import ResponseModel

logger = logging.getLogger("api")


class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = '/register'

    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class Auth:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = '/auth'

    def auth_user(self, body: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class UserInfo:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_USER_INFO = '/user_info/'

    def user_info(self, user_id, body: dict, headers):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        authorization = {"Authorization": f"JWT {headers}"}
        response = self.client.custom_request("POST", f"{self.url}{self.POST_USER_INFO}{user_id}",
                                              json=body, headers=authorization)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class StoreMagazine:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    _STORE = '/store/'

    def add_new_store(self, store, body, headers):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        authorization = {"Authorization": f"JWT {headers}"}
        response = self.client.custom_request("POST", f"{self.url}{self._STORE}{store}",
                                              json=body, headers=authorization)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_store(self, store, headers):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        authorization = {"Authorization": f"JWT {headers}"}
        response = self.client.custom_request("GET", f"{self.url}{self._STORE}{store}",
                                              headers=authorization)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class StoreItem:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_STORE_ITEM = '/item/'
    GET_ALL_ITEMS = '/items'

    def post_item(self, name_item, body: dict, headers):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        authorization = {"Authorization": f"JWT {headers}"}
        response = self.client.custom_request("POST", f"{self.url}{self.POST_STORE_ITEM}{name_item }",
                                              json=body, headers=authorization)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_all_items(self, headers):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        authorization = {"Authorization": f"JWT {headers}"}
        response = self.client.custom_request("GET", f"{self.url}{self.GET_ALL_ITEMS}", headers=authorization)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
