from fastapi import APIRouter, Response, Request

from auth import Auth
from . import schemas

router = APIRouter()


@router.post("/auth/generate-token")
def generate_access_token(request_data: schemas.LoginRequest):
    auth = Auth()
    access_token = auth.create_access_token(
        request_data.user_id,
        request_data.user_role,
        request_data.secret_key,
    )
    return Response(access_token, 200)


@router.post("/auth/validate-token")
def validate_access_token(request: Request):
    auth_header = request.headers.get("authorization")
    auth = Auth()
    valid_token = auth.is_token_valid(auth_header)
    if valid_token:
        return Response(None, 204)
    else:
        return Response(None, 401)
