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
            "max_new_tokens": 500,  
            "min_new_tokens": 250,  
            "stop_sequences": [],  
            "repetition_penalty": 1 
        }
        generated_response = self.wxModel.generate( prompt, gen_parms_override )
        retVal = ""
        for resp in generated_response['results']:
            retVal = retVal + resp['generated_text']
        return retVal
    
    def buildRAGPrompt(self, question, context):
        prompt_template = """
        Odpowiedz w jednym akapicie na pytanie: {{QUESTION}}

        Input:
        {{CONTEXT}}

        Output: 
        """
        prompt = prompt_template.replace('{{QUESTION}}',question).replace('{{CONTEXT}}',context)
        return prompt


if __name__ == '__main__':
    wx = wxService('./service.WX.cred')
    Q = "W jaki sposób projektuje się systemy sztucznej inteligencji wysokiego ryzyka?"
    C = "['1. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje się w taki sposób, w tym poprzez uwzględnienie odpowiednich narzędzi interfejsu człowiek-maszyna, aby w całym cyklu życia systemu sztucznej inteligencji wysokiego ryzyka mogły je skutecznie nadzorować osoby fizyczne, proporcjonalnie do ryzyka związanego z tymi systemami. Osoby fizyczne odpowiedzialne za zapewnienie nadzoru ze strony człowieka muszą posiadać wystarczający poziom kompetencji w zakresie sztucznej inteligencji zgodnie z art. 4b oraz należy im zapewnić niezbędne wsparcie i uprawnienia do pełnienia tej funkcji w okresie, w którym system sztucznej inteligencji jest używany, oraz do przeprowadzenia dokładnego dochodzenia po incydencie.', '1. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje się w sposób zapewniający wystarczającą przejrzystość ich działania, umożliwiającą dostawcom i użytkownikom racjonalne zrozumienie funkcjonowania systemu. Zapewnia się stopień przejrzystości odpowiedni do przeznaczenia systemu sztucznej inteligencji w celu osiągnięcia zgodności z odpowiednimi obowiązkami dostawcy i użytkownika, które określono w rozdziale 3 niniejszego tytułu. Przejrzystość oznacza zatem, że w momencie wprowadzania do obrotu systemu sztucznej inteligencji wysokiego ryzyka wykorzystuje się wszystkie dostępne środki techniczne zgodnie z powszechnie uznanym aktualnym stanem wiedzy, aby zapewnić dostawcy i użytkownikowi możliwość interpretacji wyników systemu sztucznej inteligencji. Użytkownik musi być w stanie zrozumieć system sztucznej inteligencji oraz korzystać z niego na podstawie ogólnej wiedzy na temat sposobu funkcjonowania systemu sztucznej inteligencji i przetwarzanych przez niego danych, dzięki czemu będzie on mógł wyjaśnić decyzje podjęte przez system sztucznej inteligencji osobom, których decyzje te będą dotyczyć zgodnie z art. 68 lit. c).', 'ba) jeżeli dokonują istotnych zmian w systemie sztucznej inteligencji, w tym systemie sztucznej inteligencji ogólnego przeznaczenia, który nie został sklasyfikowany jako system inteligencji wysokiego ryzyka i który wprowadzono już do obrotu lub oddano do użytku, w taki sposób, że system sztucznej inteligencji staje się systemem sztucznej inteligencji wysokiego ryzyka zgodnie z art. 6;', '2a. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje tak, aby zawierały funkcję rejestracji zdarzeń umożliwiającą rejestrowanie zużycia energii, a także pomiar lub obliczanie zużycia zasobów oraz wpływu systemu sztucznej inteligencji wysokiego ryzyka na środowisko na wszystkich etapach jego cyklu życia.']"
    prompt = wx.buildRAGPrompt( Q, C )
    print(wx.genWX(prompt))