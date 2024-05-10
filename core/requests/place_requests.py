from .base_requests import send_get_request
from core.domain.entity import ApiResponse, ApiMessage, Place

class PlaceController:
    CONTROLLER = "/place"
    
    @classmethod
    def get_free_id(cls, reserve_id: str, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_free_id",
            json={
                "reserve_id": reserve_id,
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
        if response.status_code < 300:
            place_list = [Place(**k) for k in response.json()["data"]]
            return ApiResponse(place_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
    
    @classmethod
    def get_free_period(cls, reserve_begin: int, reserve_end: int, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_free_period",
            json={
                "reserve_begin": reserve_begin,
                "reserve_end": reserve_end
            },
            token=token
        )
        if response.status_code < 300:
            place_list = [Place(**k) for k in response.json()["data"]]
            return ApiResponse(place_list)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
    