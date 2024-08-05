from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Połączenie z bazą danych z użyciem pymysql
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/gym_app", echo=True)
# Deklaratywna baza dla SQLAlchemy
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    UserID  = Column(Integer, primary_key=True, autoincrement=True)
    Login  = Column(String(50), nullable=False, unique=True)
    Password = Column(String(50), nullable=False)
    Email  = Column(String(100), nullable=True, unique=True)
    Active = Column(Boolean, nullable=False, default=True)
 
    def create_user(self,session):
        session.add(self)
        session.commit()
        pass
    @classmethod
    def get_all_users(cls, session):
        return session.query(cls).all()

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

def create_user(Login, Password, Email=None, Active=True):
    new_user = User(Login=Login, Password=Password, Email=Email, Active=Active)
    new_user.create_user(session)