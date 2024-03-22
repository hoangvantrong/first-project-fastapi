from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter
from ..import models, schemas, database, utils, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]

)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Vote)
def create_vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_vote = models.Vote(**vote.dict(), user_id=current_user)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote
