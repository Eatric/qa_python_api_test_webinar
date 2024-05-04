import allure

import booking_api


class TestDeleteBooking:

    @allure.title("Проверка удаления бронирования с авторизацией через админа")
    def test_success_delete_booking(self, default_booking):
        delete_response = booking_api.BookingApi.delete_booking(default_booking.json()["bookingid"])

        assert delete_response.status_code == 201
