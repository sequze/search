from typing import Optional
from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from models import User

SECRET = "SECRET"
import logging
log = logging.getLogger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(f"Verification requested for user {user.id}. Verification token: {token}")
