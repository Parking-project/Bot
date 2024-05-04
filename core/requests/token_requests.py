from .base_requests import send_get_request, send_post_request
from core.domain.entity import ApiResponse
from aiogram.fsm.context import FSMContext

class TokenController:
    @classmethod
    def login(cls, login: str, password: str):
        response_json = send_post_request(
            "/token/login",
            json={
                "login": login,
                "password": password
            }
        ).json()
        if response_json.get("tokens") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["tokens"])
    
    @classmethod
    def register(cls, login: str, password: str, display_name: str):
        response_json = send_post_request(
            "/token/register",
            json={
                "login": login,
                "password": password,
                "display_name": display_name
            }
        ).json()
        if response_json.get("tokens") is None:
            return ApiResponse(response_json["message"], True)
        return ApiResponse(response_json["tokens"])
        
    @classmethod
    def check(cls, access, refresh):
        response = send_get_request(
            "/token/check",
            json={},
            token=access
        )
        if response.status_code == 200:
            return ApiResponse(
                {
                    "access": access,
                    "refresh": refresh,
                }
            )
        response = send_get_request(
            "/token/refresh",
            json={}, 
            token=refresh
        )
        if response.status_code == 200:
            access = response.json()["access"]
            return ApiResponse(
                {
                    "access": access,
                    "refresh": refresh,
                }
            )
        return ApiResponse(response.json()["message"], True)
    
    @classmethod
    def logout(cls, token):
        send_get_request(
            "/token/logout",
            json={},
            token=token
        )
