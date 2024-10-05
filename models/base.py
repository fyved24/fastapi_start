from datetime import datetime, UTC
from functools import partial

from sqlmodel import Field, SQLModel


class BizBaseModel(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=partial(datetime.now, UTC), nullable=False)
    updated_at: datetime | None = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None, nullable=True)
    deleted: bool | None = Field(default=False, nullable=False)
