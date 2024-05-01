class TokenBlocList:
    ID: str
    token_jti: str
    token_create: int

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.auth_date = kwargs["auth_date"]
        self.user_id = kwargs["user_id"]
