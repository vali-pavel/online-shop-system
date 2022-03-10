from dataclasses import dataclass
from dotenv import load_dotenv
import os, jwt

load_dotenv()

ALGORITHM = os.environ["ALGORITHM"]


@dataclass
class Auth:
    @staticmethod
    def create_access_token(
        user_id: int,
        role: int,
        secret_key: str,
    ) -> str:
        to_encode = {
            "sub": user_id,
            "role": role,
        }

        encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def is_token_valid(access_token: str) -> bool:
        SECRET_KEY = os.environ["SECRET_KEY"]
        try:
            jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            return True
        except:
            return False
