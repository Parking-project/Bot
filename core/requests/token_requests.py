from .base_requests import send_get_request, send_post_request
from core.domain.entity import ApiResponse, ApiMessage, User

class TokenController:
    CONTROLLER = "/token"
    
    @classmethod
    def login(cls, login: str, password: str):
        response = send_post_request(
            cls.CONTROLLER + "/login",
            json={
                "login": login,
                "password": password
            }
        )
        if response.status_code < 300:
            data = User(**response.json())
            return ApiResponse(data)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
    
    @classmethod
    def register(cls, login: str, password: str, display_name: str):
        response = send_post_request(
            cls.CONTROLLER + "/register",
            json={
                "login": login,
                "password": password,
                "display_name": display_name
            }
        )
        if response.status_code < 300:
            data = User(**response.json())
            return ApiResponse(data)
        
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
        
    @classmethod
    def check_token(cls, access, refresh):
        if access is not None:
            response = send_get_request(
                cls.CONTROLLER + "/check_token",
                json={},
                token=access
            )
            if response.status_code < 300:
                user = User(**{
                    "tokens":{
                        "access": access,
                        "refresh": refresh,
                    },
                    "role": response.json()["role"]
                })
                return ApiResponse(user)
            
        response = send_get_request(
            "/token/refresh",
            json={}, 
            token=refresh
        )
        if response.status_code < 300:
            access = response.json()["access"]
            response = send_get_request(
                cls.CONTROLLER + "/check_token",
                json={},
                token=access
            )
            if response.status_code < 300:
                user = User(**{
                    "tokens":{
                        "access": access,
                        "refresh": refresh,
                    },
                    "role": response.json()["role"]
                })
                return ApiResponse(user)
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, True)
    
    @classmethod
    def check_connect(cls):
        response = send_get_request(
            cls.CONTROLLER + "/check_connection",
            json={},
        )
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)
    
    @classmethod
    def logout(cls, token):
        response = send_get_request(
            cls.CONTROLLER + "/logout",
            json={},
            token=token
        )
        message: ApiMessage = ApiMessage(**response.json())
        return ApiResponse(message, response.status_code > 300)
