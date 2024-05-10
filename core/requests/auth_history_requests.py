from .base_requests import send_get_request
from core.domain.entity import ApiResponse, ApiMessage, AuthHistory

class AuthHistoryController:
    CONTROLLER = "/auth"
    
    @classmethod
    def get(cls, page_index, token):
        response = send_get_request(
            cls.CONTROLLER + "/get",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )

        if response.status_code < 300:
            reserve_history_list = [AuthHistory(**k) for k in response.json()["data"]]
            return ApiResponse(reserve_history_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
