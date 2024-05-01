from .base_requests import send_get_request

class PlaceController:
    @classmethod
    def get_prefix(cls, prefix, page_index, token):
        return send_get_request(
            "/place/get_prefix",
            json={
                "place_prefix": prefix,
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
    
    @classmethod
    def get_code(cls, place_code, token):
        return send_get_request(
            "/place/get_code",
            json={
                "place_code": place_code
            },
            token=token
        )
    
    @classmethod
    def get_code(cls, hours, token):
        return send_get_request(
            "/place/get_free",
            json={
                "hours": hours
            },
            token=token
        )
