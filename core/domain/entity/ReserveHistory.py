class ReserveHistory:
    ID: str
    reserve_id: str
    reserve_state: int

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.reserve_id = kwargs["reserve_id"]
        self.reserve_state = kwargs["reserve_state"]
