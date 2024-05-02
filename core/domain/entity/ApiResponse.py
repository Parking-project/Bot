class ApiResponse:
    is_exception: bool

    def __init__(self, data, is_exception=False):
        self.data = data
        self.is_exception = is_exception

    def IsException(self):
        return self.is_exception