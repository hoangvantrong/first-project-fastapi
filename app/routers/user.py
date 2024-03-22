from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import session
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["User"]

)

    
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user( user:schemas.UserCreate, db: session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    new_user = models.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id:int, db: session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f" User with id {id} not found")
    return user