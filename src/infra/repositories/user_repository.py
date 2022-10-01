
from schemas.mongoengine import AttendanceMongoengine

class UserRepository:
    @classmethod
    async def find_user(cls,user):
        print("User:{}")
    
    
    @classmethod
    def query_user_by_id(cls,user):
        query_result = AttendanceMongoengine.objects.get(user__rfid=user['rfid'])
        return query_result
    
    @classmethod
    def query_update_user(cls,user):
        user_rfid = user["rfid"]
        
        query_result = AttendanceMongoengine.objects(user__rfid=user_rfid).update_one(dec__user__credits=1.80)
        return query_result
        
        