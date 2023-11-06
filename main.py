from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from typing import List

# from models import Owner, Cat
from models import Owner, Cat
from schemas import OwnerModel, OwnerResponse
from db import get_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


@app.get("/owners", response_model=List[OwnerResponse], name="Response ALL owners", tags=['owners'])
async def get_owners(db: Session = Depends(get_db)):
    owners = db.query(Owner).all()
    return owners


@app.get("/owners/{owner_id}", response_model=OwnerResponse, tags=['owners'])
async def get_owners(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found in the database")
    return owner


@app.post("/owners", response_model=OwnerResponse, tags=['owners'])
async def create_owner(body: OwnerModel, db: Session = Depends(get_db)):
    try:
        owner = Owner(**body.dict())
        db.add(owner)
        db.commit()
        db.refresh(owner)
    except IntegrityError as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is exists!')
    return owner


@app.put("/owners/{owner_id}", response_model=OwnerResponse, tags=['owners'])
async def update_owner(body: OwnerModel, owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found in the database")
    owner.email = body.email
    db.commit()
    return owner


@app.delete("/owners/{owner_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['owners'])
async def remove_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found in the database")
    db.delete(owner)
    db.commit()
    return owner