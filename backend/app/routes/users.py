from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate
from app.models.user import User
from app.base import SessionLocal
from passlib.context import CryptContext
from app.password_utils import get_password_hash


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: UserCreate):
    with SessionLocal() as session:
        existing_user = session.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        print("CONTRASEÑA: "+user.password)
        password_hash = get_password_hash(user.password)
        nuevo_usuario = User(
            email=user.email,
            password_hash=password_hash
        )
        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)
    return nuevo_usuario
