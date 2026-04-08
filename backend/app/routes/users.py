from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserResponse, Token
from app.models.user import User
from app.base import SessionLocal
from app.password_utils import get_password_hash, verify_password
from app.security import create_access_token, get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: UserCreate):
    with SessionLocal() as session:
        existing_user = session.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        password_hash = get_password_hash(user.password)
        nuevo_usuario = User(
            email=user.email,
            password_hash=password_hash
        )
        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)
    return nuevo_usuario

@router.post("/login", response_model = Token)
def login_user(user:UserCreate):
    with SessionLocal() as session:
        existing_user = session.query(User).filter(User.email == user.email).first()

        if not existing_user:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        
        if not verify_password(user.password,existing_user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        
        access_token = create_access_token(
            data={"sub":str(existing_user.id)}
        )
        return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/{id}", response_model = UserResponse)
def read_user(id:int, current_user: User = Depends(get_current_user)):
    if id != current_user.id:
        raise HTTPException(status_code=404, detail="Not Authorize")
    with SessionLocal() as session:
        existing_user = session.query(User).filter(User.id == id).first()
        if not existing_user:
            raise HTTPException(status_code=404, detail="ID not found")
        return existing_user