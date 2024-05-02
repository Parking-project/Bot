class TokenBlocList:
    ID: str
    token_jti: str
    token_create: int

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.token_jti = kwargs["token_jti"]
        self.token_create = kwargs["token_create"]
