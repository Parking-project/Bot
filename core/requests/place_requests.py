from .base_requests import send_get_request
from core.domain.entity import ApiResponse, ApiMessage, Place

class PlaceController:
    CONTROLLER = "/place"
    
    @classmethod
    def get_free(cls, hours: int, page_index: int, token: str):
        response = send_get_request(
            cls.CONTROLLER + "/get_free",
            json={
                "hours": hours,
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
    def get_prefix(cls, prefix, page_index, token):
        response = send_get_request(
            cls.CONTROLLER + "/get_prefix",
            json={
                "place_prefix": prefix,
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
    