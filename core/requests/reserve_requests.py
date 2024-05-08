from .base_requests import send_get_request, send_post_request, send_put_request
from core.domain.entity import Reserve, ApiResponse

class ReserveController:
    CONTROLLER = "/reserve"

    @classmethod
    def get_state(cls, state, is_actual: bool, page_index: int, token: str):
        response_json = send_get_request(
            cls.CONTROLLER + "/get_state",
            json={
                "reserve_state": state,
                "is_actual": is_actual,
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        reserve_list = [Reserve(**k) for k in response_json["data"]]
        return ApiResponse(reserve_list)

    @classmethod
    def get_process(cls, page_index: int, token: str):
        response_json = send_get_request(
            cls.CONTROLLER + "/get_process",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        reserve_list = [Reserve(**k) for k in response_json["data"]]
        return ApiResponse(reserve_list)

    @classmethod
    def post(cls, chat_id: int, message_id: int, hours: float, token):
        response_json = send_post_request(
            cls.CONTROLLER + "/post_hour",
            json={
                "hours": hours,
                "chat_id": chat_id,
                "message_id": message_id
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["data"])

    @classmethod
    def approve(cls, reserve_id: str, token: str):
        response_json = send_post_request(
            cls.CONTROLLER + "/approve",
            json={
                "reserve_id": reserve_id
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["data"])
    
    @classmethod
    def delete(cls, reserve_id: str, token: str):
        response_json = send_post_request(
            cls.CONTROLLER + "/delete",
            json={
                "reserve_id": reserve_id
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["data"])

    @classmethod
    def delete_index(cls, reserve_index: str, token: str):
        response_json = send_post_request(
            cls.CONTROLLER + "/delete_index",
            json={
                "reserve_index": reserve_index
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["data"])