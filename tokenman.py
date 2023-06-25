class Token:
    def __init__(self,token,usr_service):
            self.tk = token
            self.us = usr_service
            self.deta_man = Deta(deta_token)

            self.dt_user_db = deta_man.Base("ayeuserz")
            self.dt_tk_db = deta_man.Base("ayetokenz")

    def checkStatus(self,tkn):
        try:
            raw_str = self.dt_tk_db.get(tkn)
        except ValueError:
            return None
        else:
            if raw_str != None:
                json_obj = json.loads(json_obj)
                tkn_stat = json_obj["status"]
                return tkn_stat
            else:
                return None
            
    def addToken(self,tkn):
            add_res = self.dt_user_db.put()