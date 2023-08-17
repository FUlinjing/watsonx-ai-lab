import json
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model


class wxService:
    def __init__(self, configFile):
        self.configFile = configFile
        self._readWXconfig()
        self.wxModel = self._crWX()

    
    def _readWXconfig(self):
        with open(self.configFile, 'r') as json_file:
            data = json.load(json_file)
            self.wxApiKey = data['apikey']
            self.wxUrl = data['url']
            self.wxProjectid = data['projectid']
            #print(self.wxApiKey, self.wxUrl)
    
    def _crWX(self):
        wx_credentials = { 
            "url"    : self.wxUrl, 
            "apikey" : self.wxApiKey
        }    
        model_id    = ModelTypes.MPT_7B_INSTRUCT2
        gen_parms   = None
        project_id  = self.wxProjectid
        space_id    = None
        verify      = False

        return Model( model_id, wx_credentials, gen_parms, project_id, space_id, verify ) 

    def genWX(self, prompt):
        gen_parms_override = {  
            "decoding_method": "greedy",  
            "max_new_tokens": 400,  
            "min_new_tokens": 0,  
            "stop_sequences": [],  
            "repetition_penalty": 1 
        }
        generated_response = self.wxModel.generate( prompt, gen_parms_override )
        print( json.dumps( generated_response, indent=2 ) )


if __name__ == '__main__':
    wx = wxService('./service.WX.cred')
    wx.genWX("In today's sales meeting, we ")