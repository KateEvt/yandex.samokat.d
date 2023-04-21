import sender_stand_request


def test_track_positive_assert():
    track_response = sender_stand_request.get_order_by_track()
    assert track_response.status_code == 200
