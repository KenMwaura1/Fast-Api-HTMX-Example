from pydantic import BaseModel, Field
from datetime import datetime as dt
from pytz import timezone as tz


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
    completed: str = Field(default="False")
    created_date: str = Field(default=dt.now(tz("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M"))


class NoteDB(NoteSchema):
    id: int
