class User:
    access: str
    refresh: str
    role: str

    def __init__(self, **kwargs) -> None:
        self.access = kwargs["tokens"]["access"]
        self.refresh = kwargs["tokens"]["refresh"]
        self.role = kwargs["role"]
