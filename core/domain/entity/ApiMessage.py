class ApiMessage:
    message: str

    def __init__(self, **kwargs):
        if kwargs.get("data"):
            self.message = kwargs["data"]
        else:
            self.message = kwargs["message"]