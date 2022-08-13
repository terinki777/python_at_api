import random

from register_3_step.api import Register
from register_3_step.api import Auth
from register_3_step.api import UserInfo
from register_3_step.api import StoreMagazine
from register_3_step.models import RegisterUser
from register_3_step.api import StoreItem
from schemas.registration import valid_schema

URL = "https://stores-tests-api.herokuapp.com"


class TestRegistration:
    def test_registration(self):
        body = RegisterUser.random()
        response = Register(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')


class TestAuth:
    def test_auth(self):
        body = RegisterUser.random()
        response_reg = Register(url=URL).register_user(body=body, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body)
        assert response_auth.status == 200
        assert response_auth.response.get('access_token')


class TestUserInfo:
    def test_user_info(self):
        body = RegisterUser.random()
        response_reg = Register(url=URL).register_user(body=body, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body)
        access_token = response_auth.response.get('access_token')
        uuid = response_reg.response.get('uuid')
        body_user_info = RegisterUser.random_user_info()
        response_user_info = UserInfo(url=URL).user_info(user_id=uuid, body=body_user_info, headers=access_token)
        assert response_user_info.status == 200


class TestStoreMagazine:
    def test_add_new_store(self):
        random_store = random.randrange(9999999)
        body_reg = RegisterUser.random()
        body_store = RegisterUser.random_product()
        response_reg = Register(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = StoreMagazine(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        assert response_store.status == 201

    def test_get_store(self):
        random_store = random.randrange(9999999)
        body_reg = RegisterUser.random()
        body_store = RegisterUser.random_product()
        response_reg = Register(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = StoreMagazine(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        response_get_store = StoreMagazine(url=URL).get_store(store=random_store, headers=access_token)
        assert response_get_store.status == 200


class TestStoreItem:
    def test_post_item(self):
        random_store = random.randrange(9999999)
        random_name_item = RegisterUser.random_item()
        body_reg = RegisterUser.random()
        body_store = RegisterUser.random_product()
        response_reg = Register(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = StoreMagazine(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        uuid = response_store.response.get('uuid')
        body_item = RegisterUser.random_store_item(uuid)
        response_item = StoreItem(url=URL).post_item(name_item=random_name_item, body=body_item, headers=access_token)
        assert response_item.status == 201

    def test_get_all_items(self):
        random_store = random.randrange(9999999)
        body_reg = RegisterUser.random()
        body_store = RegisterUser.random_product()
        response_reg = Register(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = Auth(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = StoreMagazine(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        uuid = response_store.response.get('uuid')
        for i in range(3):
            random_name_item = RegisterUser.random_item()
            body_item = RegisterUser.random_store_item(uuid)
            response_item = StoreItem(url=URL).post_item(name_item=random_name_item, body=body_item,
                                                         headers=access_token)
        response_get_all_items = StoreItem(url=URL).get_all_items(headers=access_token)
        assert response_get_all_items.status == 200
