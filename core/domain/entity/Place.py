class Place:
    ID: str
    place_code: str

    def __init__(self, **kwargs):
        self.ID = kwargs["ID"]
        self.place_code = kwargs["place_code"]
