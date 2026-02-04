from app.base import Base, engine
from app.models import user, zone, parking_report, parking_availability_stats

# 5️⃣ Función para probar conexión
def test_connection():
    try:
        with engine.connect() as conn:
            print("✅ Connected to PostgreSQL successfully!")
    except Exception as e:
        print("❌ Connection failed:", e)

# Crear todas las tablas
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    test_connection()
    create_tables()
