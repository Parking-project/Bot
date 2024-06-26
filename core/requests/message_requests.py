from .base_requests import send_post_request
from core.domain.entity import ApiResponse, ApiMessage

class MessageController:
    CONTROLLER = "/message"

    CHAT_ID = "chat_id"
    MESSAGE_BOT_ID = "message_bot_id"
    MESSAGE_ID = "message_id"
    
    @classmethod
    def post(cls, text, group_id, message_id, answer_tg_id, token):
        
        response = send_post_request(
            cls.CONTROLLER + "/post",
            json={
                "text": text,
                cls.CHAT_ID: group_id,
                cls.MESSAGE_ID: message_id,
                cls.MESSAGE_BOT_ID: answer_tg_id
            },
            token=token
        )

        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)
