from requests import post as POST
from json import loads

class SpamCheck():
    
    postmark_spamcheck_url = "http://spamcheck.postmarkapp.com/filter"
    
    def __postmark_spamcheck(message, options):
        data = {'email':email,'options':'short'}
        result = POST(self.postmark_spamcheck_url,data)
        result.raise_for_status()
        content = loads(result.content)
        if 'error' in content:
            raise Exception(content['message'])
        else
            return content['score']
        
    
    def GetScore(self,email):
        results = __postmark_spamcheck(email,"short")
    def GetReport(email):
        results = __postmark_spamcheck(email,"short")