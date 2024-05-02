class AuthHistory:
    ID: str
    auth_date: int
    user_id: str

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.auth_date = kwargs["auth_date"]
        self.user_id = kwargs["user_id"]
