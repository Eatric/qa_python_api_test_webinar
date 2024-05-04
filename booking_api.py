import allure
import requests

import data
import urls


class BookingApi:
    @staticmethod
    @allure.step("Авторизация в сервисе букинга")
    def auth():
        return requests.post(urls.BASE_URL + urls.AUTH_ENDPOINT, json=data.TestDataAuth.AUTH_USER_BODY).json()["token"]

    @staticmethod
    @allure.step("Отправка запроса на создание бронирования")
    def  create_booking(body):
        return requests.post(urls.BASE_URL + urls.CREATE_BOOKING_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление бронирования")
    def delete_booking(bookind_id):
        return requests.delete(urls.BASE_URL + urls.DELETE_BOOKING_ENDPOINT + str(bookind_id), headers={
            "Cookie": "token=" + str(BookingApi.auth())
        })
