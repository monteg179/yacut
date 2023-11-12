from http import HTTPStatus


class APIError(Exception):

    def __init__(self, message: str, status: HTTPStatus = HTTPStatus.BAD_REQUEST) -> None:
        super().__init__()
        self.message = message
        self.status = status

    def to_dict(self) -> dict[str, str]:
        return dict(message=self.message)


class APIRequestError(APIError):
    pass
