from .base_requests import send_get_request, send_post_request

class TokenController:
    @classmethod
    def login(cls, login: str, password: str):
        return send_post_request(
            "/token/login",
            json={
                "login": login,
                "password": password
            }
        )
    
    @classmethod
    def register(cls, login: str, password: str, display_name: str):
        return send_post_request(
            "/token/register",
            json={
                "login": login,
                "password": password,
                "display_name": display_name
            }
        )
    
    @classmethod
    def refresh(cls, refresh_token: str):
        return send_get_request(
            "/token/refresh",
            json={}, 
            token=refresh_token
        )
    
    @classmethod
    def check(cls, access, refresh):
        response = send_get_request(
            "/token/check",
            json={},
            token=access
        )
        if response.status_code == 200:
            return access, refresh
        response = cls.refresh(refresh_token=refresh)
        if response.status_code == 200:
            return response.json()["access"], refresh
        return None, None
    
    @classmethod
    def logout(cls, token):
        return send_get_request(
            "/token/logout",
            data={},
            token=token
        )
