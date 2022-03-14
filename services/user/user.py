from typing import Union
from dataclasses import dataclass
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os, requests

from api.schemas import User, UserLogin
from api import db_manager
from core.security import verify_password
import constants

load_dotenv()


@dataclass
class User:
    db: Session = None

    def login(self, user_in: UserLogin):
        db_user = db_manager.get_user_by_email(self.db, email=user_in.email)
        if not db_user:
            return None
        password_match = verify_password(user_in.password, db_user.hashed_password)
        if not password_match:
            return None
        return db_user

    def create_user(self, user_in: User):
        existing_user = self._check_if_user_exists(user_in.email)
        if existing_user:
            return None
        return db_manager.create_user(self.db, user=user_in)

    def _check_if_user_exists(self, user_email: str) -> User:
        return db_manager.get_user_by_email(self.db, email=user_email)

    @staticmethod
    def get_auth_token(user_id, user_role) -> Union[str, None]:
        request_body = {
            "user_id": user_id,
            "user_role": user_role,
            "secret_key": os.environ["SECRET_KEY"],
        }
        try:
            response = requests.post(
                f"{constants.AUTH_API_URL}/generate-token",
                json=request_body,
            )
            return response.text
        except:
            return None
