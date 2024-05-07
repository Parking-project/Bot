from .base_requests import send_get_request
from core.domain.entity import Place, ApiResponse

class PlaceController:
    CONTROLLER = "/place"
    
    @classmethod
    def get_prefix(cls, prefix, page_index, token):
        response_json = send_get_request(
            cls.CONTROLLER + "/get_prefix",
            json={
                "place_prefix": prefix,
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        place_list = [Place(**k) for k in response_json["data"]]
        return ApiResponse(place_list)
    
    @classmethod
    def get_code(cls, place_code, token):
        response_json = send_get_request(
            cls.CONTROLLER + "/get_code",
            json={
                "place_code": place_code
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        place = Place(**response_json["data"])
        return ApiResponse(place)
    
    @classmethod
    def get_code(cls, hours, token):
        response_json = send_get_request(
            cls.CONTROLLER + "/get_free",
            json={
                "hours": hours
            },
            token=token
        ).json()
        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        place_list = [Place(**k) for k in response_json["data"]]
        return ApiResponse(place_list)
