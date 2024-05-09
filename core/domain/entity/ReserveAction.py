class ReserveAction:
    message_id: int
    reserve_id: str

    def __init__(self, **kwargs):
        self.message_id = kwargs["data"]["message_id"]
        self.reserve_id = kwargs["data"]["reserve_id"]
