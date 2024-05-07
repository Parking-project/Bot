from .base_requests import send_get_request
from core.domain.entity import ReserveHistory, ApiResponse

class ReserveHistoryController:
    CONTROLLER = "/reserve_history"
    
    @classmethod
    def get(cls, page_index, token):
        response_json = send_get_request(
            cls.CONTROLLER + "/get",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        reserve_history_list = [ReserveHistory(**k) for k in response_json["data"]]
        return ApiResponse(reserve_history_list)
