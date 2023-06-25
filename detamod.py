from deta import Deta

class Detaman:
    def __init__(self,deta_token,deta_db):
        self.deta_man = Deta(deta_token)
        self.detadb = deta_man.Base(deta_db)
    
    def putToken(self,token_user,token_service,token_data,token_exp):
        print("puttoing token")
        token_owner = token_user."_".token_service
        now_time = datetime.now()
        
        
        datetime_exp = datetime.datetime.fromtimestamp(token_exp)
        datetime_now = datetime.datetime.fromtimestamp(now_time)

        if datetime_now>=datetime_exp
            return None
        else:
            try:
                self.detadb.insert(token_data,token_owner,expiry_at = datetime_exp)
            except deta.errors.ItemExistsError as e:
                print(e)
                return None
            else:
                return "SUCCESS"

    def getToken(self,token_user,token_service):
        token_owner = token_user."_".token_service
        tokendt = self.detadb.get(token_owner)
        if tokendt == None:
            return None
        else:
            return "TK_OK"

    def checkStatus(self,tken):
        