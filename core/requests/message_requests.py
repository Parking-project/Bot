from .base_requests import send_post_request
from core.domain.entity import Message, ApiResponse

class MessageController:
    @classmethod
    def post(cls, text, group_id, message_id, answer_tg_id, token):
        response_json = send_post_request(
            "/message/post_chat",
            json={
                "text": text,
                "chat_id": group_id,
                "message_id": message_id,
                "message_bot_id": answer_tg_id
            },
            token=token
        ).json()

        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        # message_data = Message(**response_json["data"])
        return ApiResponse(response_json["data"])
