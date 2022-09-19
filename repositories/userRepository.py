from src.database import ConnectionHandler
from schemas.user import User

db_handler = ConnectionHandler()
class UserRepository:
    
    
    @classmethod
    def insert_user(user: User):
        pass
    
    @classmethod
    def update_credit(name_str:str):
        pass
    