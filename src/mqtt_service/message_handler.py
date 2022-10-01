from src.infra.repositories.user_repository import UserRepository
from datetime import datetime
import json

class MessageHandler:  
    @classmethod
    def execute_query(cls,payload):
        print(payload)
        payload = json.loads(payload)
        query_result = UserRepository.query_user_by_id(payload)
        if query_result:
            print(f'query result ->> {query_result["user"]}')
            cls.validate_credits(query_result["user"])
        
            
    @staticmethod
    def user_verify_year(time_user):
        # horario": "09/30/2022, 20:58:41"
        # time_user = datetime.strptime(time_user,"%D/%m/%y %H:%M:%S")
        current_year = datetime.now().year
        print(f'rutirt ->>> {current_year}')
        dif = current_year - time_user.year
        if dif < 4:
            return True
        
        else:
            return False
        
    
    @classmethod
    def validate_credits(cls,user):
        from src.ui.http import mqtt
        # user = user.to_json()
        # print(f'dkjsg ->>>>>>>>>>>>{user["user"]}')
        updated_user = {}
        updated_user["user"] = {}
        updated_user["user"]["name"] = user["name"]
        updated_user["user"]["rfid"] =  user["rfid"]
        credits = user["credits"]
        updated_user["credits"] = credits
        time_user = user["created_at"] 
        if credits > 1.8 and cls.user_verify_year(time_user):
            value = UserRepository.query_update_user(user)
            updated_user = json.dumps(updated_user)
            mqtt.client.publish("ru/confirm",updated_user, qos=1)
            
        else:
            updated_user["message"] = "User does not have enough credit"
            updated_user = json.dumps(updated_user)
            mqtt.client.publish("ru/confirm",updated_user,qos=1)
        
            
    
    
    