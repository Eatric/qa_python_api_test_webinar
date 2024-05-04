class TestDataCreateBooking:
    CREATE_BOOKING_BODY = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


class TestDataAuth:
    AUTH_USER_BODY = {
        "username": "admin",
        "password": "password123"
    }
