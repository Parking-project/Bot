from .base_requests import send_get_request
from core.domain.entity import ApiResponse, ApiMessage, TokenBlocList

class TokenBlocListController:
    CONTROLLER = "/token_bloc_list"
    
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
            token_list = [TokenBlocList(**k) for k in response.json()["data"]]
            return ApiResponse(token_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
