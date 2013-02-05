# -*- coding: utf-8 -*-

import requests

def get(request_url, params=None):

    if params is not None:
        response = requests.get(request_url, params=params)
    else:
        response = requests.get(request_url)
    return response.json()
    # try:
    #     response = requests.get(request_url)
    #     if response.code == '200':
    #         return response.content
    #     else:
    #         print "Something was not OK not code 200"
    # except:
    #     print "Something went on on the request GET"

def post(request_url, param_dict=None):
    pass