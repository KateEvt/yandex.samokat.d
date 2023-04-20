import requests
import data
import configuration


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def get_order_by_track():
    post_new_order_response = post_new_order(data.order_body)
    order_track = post_new_order_response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params={"t": order_track})


order_response = post_new_order(data.order_body)
print(order_response.status_code)
print(order_response.json())

track_response = get_order_by_track()
print(track_response.status_code)
print(track_response.json())

