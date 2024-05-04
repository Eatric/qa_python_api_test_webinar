import allure
import pytest

import booking_api
from helper import BookingFactory


@allure.step("Создание шаблонного букинга")
@pytest.fixture(scope='function')
def default_booking():
    booking_response = booking_api.BookingApi.create_booking(BookingFactory.booking_body_with_random_name_and_price())

    return booking_response
