class Reserve:
    ID: str
    reserve_begin: int
    reserve_end: int

    place_code: str

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.reserve_begin = kwargs["reserve_begin"]
        self.reserve_end = kwargs["reserve_end"]
        if kwargs.get("place_code") is None:
            self.place_code = "----"
        else:
            self.place_code = kwargs["place_code"]
