from urllib.request import Request
from fastapi import FastAPI, Response, Request

import path_loader
from auth import Auth
from model import LoginRequest

app = FastAPI()


@app.post("/auth/generate-token")
def generate_access_token(request_data: LoginRequest):
    auth = Auth()
    access_token = auth.create_access_token(
        request_data.user_id,
        request_data.user_role,
        request_data.secret_key,
    )
    return Response(access_token, 200)


@app.post("/auth/validate-token")
def validate_access_token(request: Request):
    auth_header = request.headers.get("authorization")
    auth = Auth()
    valid_token = auth.is_token_valid(auth_header)
    if valid_token:
        return Response(None, 204)
    else:
        return Response(None, 401)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
