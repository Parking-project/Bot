from .base_requests import send_get_request

class AuthController:
    @classmethod
    def get(cls, page_index, token):
        return send_get_request(
            "/auth/get",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        )
