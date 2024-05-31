import sender_stand_request


def put_new_order():
    order_response = sender_stand_request.post_new_order(order_body)
    order_response = sender_stand_request.put_new_order
    assert order_response.status_code == 200

git add имя_файла