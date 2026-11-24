from rest_framework import status
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(
        self,
        status_code=status.HTTP_200_OK,
        message=None,
        data=None,
        meta=None,
    ):
        body = {"status_code": status_code}

        if message is not None:
            body["message"] = message

        if data is not None:
            body["data"] = data

        if meta is not None:
            body["meta"] = meta

        super().__init__(data=body, status=status_code)