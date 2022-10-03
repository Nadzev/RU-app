from src.infra.repositories.user_repository import UserRepository
from schemas.pydantic.ru_model_pydantic import Attendance, User
from datetime import datetime
import json
from schemas.mongoengine.ru_model import AttendanceMongoengine

from bson import ObjectId
class MessageHandler:  
    
    
    @classmethod
    def execute_query(cls,payload):
        from src.ui.http import mqtt
        print(payload)
        payload = json.loads(payload)
        query_result = None
        try:
            query_result = UserRepository.query_user_by_id(payload)
        
        except Exception as error:
            print(error)
            msg = json.dumps({"message":"Usuario nao encontrado"})
            mqtt.client.publish("ru/confirm",msg,qos=1)
            return {"Not found":"User not founded"}
        
        
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


        if not cls.user_verify_year(time_user):
            updated_user["message"] = "Cartao passou da validade!"
            updated_user = json.dumps(updated_user)
            mqtt.client.publish("ru/confirm",updated_user,qos=1)

        elif credits > 1.8 and cls.user_verify_year(time_user): #????????????

            _user = User(
                rfid=updated_user["user"]["rfid"],
                name=updated_user["user"]["name"],
                credits=float(user["credits"])-1.8,
                created_at=time_user)
    
            _attendance = Attendance(id=ObjectId(), user=_user, clock_in=datetime.utcnow())
            attendance_db = AttendanceMongoengine.from_entity(_attendance)
            attendance_db.save()

            value = UserRepository.query_update_user(user)
            
            updated_user["message"] = "Compra efetuada!"
            updated_user = json.dumps(updated_user)
            mqtt.client.publish("ru/confirm",updated_user, qos=1)
        elif(credits<1.8):
            updated_user["message"] = "Usuario nao tem credito suficiente"
            updated_user = json.dumps(updated_user)
            mqtt.client.publish("ru/confirm",updated_user,qos=1)
        #elif(credits>1.8 and not cls.user_verify_year(time_user)):
            #updated_user["message"] = "Cartao passou da validade!"
            #updated_user = json.dumps(updated_user)
            #mqtt.client.publish("ru/confirm",updated_user,qos=1)
            
    
    
    