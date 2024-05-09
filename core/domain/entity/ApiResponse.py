from .ApiMessage import ApiMessage

class ApiResponse:
    exception: bool

    def __init__(self, data, exception=False):
        self.data = data
        self.exception = exception
        if exception:
            print("\n\n\nData = ", data, "\n\n\n")

    def is_exception(self):
        return self.exception
    
    def get_data(self):
        return self.data
    
    def get_exception(self) -> ApiMessage:
        return self.data