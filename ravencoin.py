#!/usr/bin/python3

from .api_request import ApiReq

BASE_API = 'https://ravencoin.network/api/addr/{wallet}'


class RvnWallet():
    def __init__(self, wallet):
        self.__wallet = wallet
        self.__balance = 0.0
        self.__last_error = None

    def update(self):
        api = ApiReq()
        cust_url = BASE_API.replace('{wallet}', self.__wallet)
        data_json = api.api_request(cust_url)
        self.__last_error = api.last_error
        if data_json is not None:
            self.__balance = float(data_json['balance'])
            return True

        if self.__last_error is None:
            self.__last_error = 'Can\'t retrieve json result'
        return None

    @property
    def wallet(self):
        return self.__wallet

    @property
    def balance(self):
        return self.__balance

    @property
    def last_error(self):
        return self.__last_error
