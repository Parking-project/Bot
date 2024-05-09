class Place:
    place_code: str

    def __init__(self, **kwargs):
        self.place_code = kwargs["place_code"]
