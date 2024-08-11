# Users API con autorización OAuth2 JWT ###

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas
# from app.schemas import User, UserPass
#import app.models as models
from app.database import SessionLocal

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
@router.post("/", response_model=schemas.UserPass, status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserPass, db: Session = Depends(get_db)):
    validator_email = db.query(models.User).filter(models.User.email == user.email).first()
    if validator_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[schemas.User], status_code=status.HTTP_200_OK)
async def get_artists(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/{user_id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
async def get_artist(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_artist(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}


@router.put("/{user_id}", response_model=schemas.UserPass, status_code=status.HTTP_200_OK)
async def update_artist(user_id: int, user: schemas.UserPass, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    validator_email = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.user_id != user_id  # Excluir el usuario actual
    ).first()
    if validator_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

