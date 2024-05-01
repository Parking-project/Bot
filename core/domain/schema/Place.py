class Place:
    ID: str
    place_is_valid: bool
    place_code: str

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.auth_date = kwargs["auth_date"]
        self.user_id = kwargs["user_id"]
