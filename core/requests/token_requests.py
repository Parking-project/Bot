from .base_requests import send_get_request, send_post_request

class TokenController:
    @classmethod
    def login(cls, login: str, password: str):
        tokens = send_post_request(
            "/token/login",
            json={
                "login": login,
                "password": password
            }
        ).json()["tokens"]
        return tokens["access"], tokens["refresh"]
    
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
    def check(cls, token):
        return send_get_request(
            "/token/check",
            json={},
            token=token
        )
    
    @classmethod
    def logout(cls, token):
        return send_get_request(
            "/token/logout",
            json={},
            token=token
        )
