from .base_requests import send_get_request, send_post_request
from core.domain.entity import ApiResponse, ApiMessage, Reserve, ReserveAction

class ReserveController:
    CONTROLLER = "/reserve"

    @classmethod
    def get_state(cls, state, is_actual: bool, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_state",
            json={
                "reserve_state": state,
                "is_actual": is_actual,
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
        if response.status_code < 300:
            reserve_list = [Reserve(**k) for k in response.json()["data"]]
            return ApiResponse(reserve_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)

    @classmethod
    def get_approve(cls, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_state",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
        if response.status_code < 300:
            reserve_list = [Reserve(**k) for k in response.json()["data"]]
            return ApiResponse(reserve_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)

    @classmethod
    def get_process(cls, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_process",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
        if response.status_code < 300:
            reserve_list = [Reserve(**k) for k in response.json()["data"]]
            return ApiResponse(reserve_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)

    @classmethod
    def post(cls, chat_id: int, message_id: int, hours: float, token):
        response = send_post_request(
            cls.CONTROLLER + "/post_hour",
            json={
                "hours": hours,
                "chat_id": chat_id,
                "message_id": message_id
            },
            token=token
        )
        if response.status_code < 300:
            reserve_action: ReserveAction = ReserveAction(**response.json())
            return ApiResponse(reserve_action)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)

    @classmethod
    def approve(cls, reserve_id: str, token: str):
        response = send_post_request(
            cls.CONTROLLER + "/approve",
            json={
                "reserve_id": reserve_id
            },
            token=token
        )
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)
    
    @classmethod
    def delete(cls, reserve_id: str, token: str):
        response = send_post_request(
            cls.CONTROLLER + "/delete",
            json={
                "reserve_id": reserve_id
            },
            token=token
        )
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)

    @classmethod
    def delete_index(cls, reserve_index: str, token: str):
        response = send_post_request(
            cls.CONTROLLER + "/delete_index",
            json={
                "reserve_index": reserve_index
            },
            token=token
        )
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)