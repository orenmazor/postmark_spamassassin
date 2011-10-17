from requests import post as POST
from json import loads

class SpamCheck():
    
    postmark_spamcheck_url = "http://spamcheck.postmarkapp.com/filter"
    
    def postmark_spamcheck(self,message, options):
        data = {'email':message,'options':options}
        result = POST(self.postmark_spamcheck_url,data)
        result.raise_for_status()
        content = loads(result.content)
        if 'error' in content:
            raise Exception(content['message'])
        return content
        
    
    def GetScore(self,email):
        results = self.postmark_spamcheck(email,"short")
        return results['score']
        
    def GetReport(self,email):
        results = self.postmark_spamcheck(email,"long")
        return results['report']