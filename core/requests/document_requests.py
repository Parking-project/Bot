from .base_requests import send_post_request
from core.domain.entity import Message, ApiResponse

class DocumentController:
    @classmethod
    def post(cls, page_index, token):
        response_json = send_post_request(
            "/message/post",
            json={
                "page_index": page_index,
                "page_size": 10
            },
            token=token
        ).json()

        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        message_data = Message(**response_json["data"])
        return ApiResponse(message_data)
