from .base_requests import send_post_request
from core.domain.entity import ApiResponse

class DocumentController:
    @classmethod
    def post(cls, file_id: str,
             file_unique_id: str, file_size: int,
             file_url: str, file_mime: str, token: str):
        
        response_json = send_post_request(
            "/document/post",
            json={
                "document_file_id": file_id,
                "document_file_unique_id": file_unique_id,
                "document_file_size": file_size,
                "document_file_url": file_url,
                "document_file_mime": file_mime
            },
            token=token
        ).json()

        if response_json.get("data") is None:
            print("\n\n\n", response_json["message"], "\n\n\n")
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["data"])
