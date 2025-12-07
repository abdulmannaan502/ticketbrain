from app.database import SessionLocal
from app.models import User

def main():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for u in users:
            print(f"ID={u.id} | email={u.email} | created_at={u.created_at}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
