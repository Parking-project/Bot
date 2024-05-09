from .base_requests import send_post_request
from core.domain.entity import ApiResponse, ApiMessage

class DocumentController:
    CONTROLLER = "/document"

    @classmethod
    def post(cls, file_id: str,
             file_unique_id: str, file_size: int,
             file_url: str, file_mime: str, token: str):
        
        response = send_post_request(
            cls.CONTROLLER + "/post",
            json={
                "document_file_id": file_id,
                "document_file_unique_id": file_unique_id,
                "document_file_size": file_size,
                "document_file_url": file_url,
                "document_file_mime": file_mime
            },
            token=token
        )

        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)
