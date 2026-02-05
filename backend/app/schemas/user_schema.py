from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr      # valida automáticamente que sea un email correcto
    password: str        # contraseña en texto plano (se hasheará en el backend)

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True   # permite devolver objetos SQLAlchemy directamente
