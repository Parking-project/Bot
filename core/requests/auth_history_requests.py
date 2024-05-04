from .base_requests import send_get_request
from core.domain.entity import AuthHistory, ApiResponse

class AuthHistoryController:
    @classmethod
    def get(cls, page_index, token):
        response_json = send_get_request(
            "/auth/get",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()

        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        auth_list = [AuthHistory(**k) for k in response_json["data"]]
        return ApiResponse(auth_list)
