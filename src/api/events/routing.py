import os
from fastapi import APIRouter
from .schemas import (
    EventSchema, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
    )

router = APIRouter()
from ..db.config import DB_URL

# Get DATA Here
# LIST VIEW
# GET /api/events/
@router.get("/")
def read_events() -> EventListSchema:
    # A bunch of items in a table
    print(os.environ.get("DB_URL"), DB_URL)   
    return {
        "results": [{"id": 1}, {"id": 2}, {"id": 3}],
        "count": 3
        }

# SEND DATA HERE
# CREATE VIEW
# POST /api/events/
@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    # A bunch of items in a table
    data = payload.model_dump() # Payload -> dict -> pydantic
    return {"id": 123, **data}

# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # A single row
    return {"id": event_id}

# Update this DATA 
# PUT /api/events/12
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventSchema:
    # A single row
    data = payload.model_dump()
    return {"id": event_id, **data}

#@router.delete("/{event_id}")
# def delete_event(event_id: int) -> EventSchema:
    # A single row
    #return {"id": event_id}