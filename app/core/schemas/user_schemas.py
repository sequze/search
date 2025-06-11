from fastapi_users import schemas


class BaseSchema:
    username: str


class UserRead(BaseSchema, schemas.BaseUser[int]):
    pass


class UserCreate(BaseSchema, schemas.BaseUserCreate):
    pass


class UserUpdate(BaseSchema, schemas.BaseUserUpdate):
    pass
