import configuration
import requests
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)
def get_new_order_token():
    response = post_new_order(data.order_body)
    return response.json().get("authToken")
def put_new_order():
    authtoken_correct = data.headers.copy()
    return requests.postconfiguration.URL_SERVICE + configuration.ORDER_NUMBER + get_new_order_token()