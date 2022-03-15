from fastapi import Response, Request
from starlette.middleware.base import BaseHTTPMiddleware
import requests

import constants


class AuthMiddleware(BaseHTTPMiddleware):
    @staticmethod
    async def dispatch(request: Request, call_next):
        if request.method == "OPTIONS":
            return Response(None, 204)

        auth = request.headers.get("authorization")

        if auth is None:
            return Response("Unauthorized request", 401)

        is_token_valid = requests.post(
            f"{constants.AUTH_API_URL}/validate-token",
            headers={"authorization": auth},
        )

        if is_token_valid == False:
            return Response("Unauthorized request", 401)

        return await call_next(request)
