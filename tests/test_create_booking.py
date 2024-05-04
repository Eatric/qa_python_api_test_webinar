import allure
import pytest

import data
import helper
from booking_api import BookingApi


class TestCreateBooking:
    @allure.title("Проверка успешности создания бронирования")
    @allure.description("Создание шаблонного бронирования, проверка статуса ответа и тела ответа")
    def test_success_create_booking(self):
        created_booking_request = BookingApi.create_booking(data.TestDataCreateBooking.CREATE_BOOKING_BODY)

        assert (created_booking_request.status_code == 200 and
                created_booking_request.json()["booking"] == data.TestDataCreateBooking.CREATE_BOOKING_BODY)

    @allure.title("Проверка ошибки при создании бронирования с пустым именем")
    @allure.description("Создание бронирования с пустым именем")
    def test_empty_name_create_booking(self):
        body = helper.ChangeTestDataHelper.modify_create_booking_body("firstname", "")

        created_booking_request = BookingApi.create_booking(body)

        assert created_booking_request.status_code == 400

    @allure.title("Проверка успешного создания бронирования с ценой > 0")
    @pytest.mark.parametrize("totalprice", [
        pytest.param(999999),
        pytest.param(1)
    ])
    def test_success_create_booking_with_different_totalprice(self, totalprice):
        body = helper.ChangeTestDataHelper.modify_create_booking_body("totalprice", totalprice)

        created_booking_request = BookingApi.create_booking(body)

        assert (created_booking_request.status_code == 200 and
                created_booking_request.json()["booking"]["totalprice"] == totalprice)

    @allure.title("Проверка ошибки при создании бронирования с неверной ценой")
    @pytest.mark.parametrize("totalprice", [
        pytest.param(0),
        pytest.param(-1),
        pytest.param(-999999)
    ])
    def test_failed_create_booking_with_different_totalprice(self, totalprice):
        body = helper.ChangeTestDataHelper.modify_create_booking_body("totalprice", totalprice)

        created_booking_request = BookingApi.create_booking(body)

        assert created_booking_request.status_code == 400

    @allure.title("Создание бронирования, проверка что в ответе есть bookingId")
    def test_success_create_booking_return_bookingid(self):
        body = helper.ChangeTestDataHelper.modify_create_booking_body("firstname", "Kamil")

        created_booking_request = BookingApi.create_booking(body)

        booking_id = created_booking_request.json()["bookingid"]

        assert created_booking_request.status_code == 200 and booking_id is not None and booking_id > 0

    @allure.title("Нельзя создать второе такое же бронирование")
    def test_failed_second_create_booking_return_bookingid(self):
        body = helper.ChangeTestDataHelper.modify_create_booking_body("firstname", "Kamil")

        created_booking_request = BookingApi.create_booking(body)
        second_booking_request = BookingApi.create_booking(body)

        assert second_booking_request.status_code == 400