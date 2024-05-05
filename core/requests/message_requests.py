from .base_requests import send_post_request
from core.domain.entity import Message, ApiResponse

class MessageController:
    CHAT_ID = "chat_id"
    MESSAGE_BOT_ID = "message_bot_id"
    MESSAGE_ID = "message_id"
    
    @classmethod
    def post(cls, text, group_id, message_id, answer_tg_id, token):
        response_json = send_post_request(
            "/message/post",
            json={
                "text": text,
                cls.CHAT_ID: group_id,
                cls.MESSAGE_ID: message_id,
                cls.MESSAGE_BOT_ID: answer_tg_id
            },
            token=token
        ).json()

        if response_json.get("data") is None:
            return ApiResponse(response_json["message"], True)
        # message_data = Message(**response_json["data"])
        return ApiResponse(response_json)
