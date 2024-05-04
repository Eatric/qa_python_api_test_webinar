import random

import allure
from faker import Faker

import data


class ChangeTestDataHelper:

    @staticmethod
    def modify_create_booking_body(key, value):
        body = data.TestDataCreateBooking.CREATE_BOOKING_BODY.copy()
        body[key] = value

        return body


class BookingFactory:
    @staticmethod
    @allure.step("Генерация body для создания букинга")
    def booking_body_with_random_name_and_price():
        fake = Faker()

        return {
            "firstname": fake.name(),
            "lastname": fake.last_name(),
            "totalprice": random.randint(0, 999),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
