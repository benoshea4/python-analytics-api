from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int


# {
#     "id": 12,
#     "name": "Event 12",
#     "description": "Event 12 description"
# }