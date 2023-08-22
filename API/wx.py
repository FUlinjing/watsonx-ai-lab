import json
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model

######################## TESTY PROMPTÓW #
test1 = """
Task:
Odpowiedz w jednym akapicie na pytanie: {{QUESTION}}

Input:
{{CONTEXT}}

Output: 
"""


test2 = """
{{CONTEXT}}

PYTANIE: {{QUESTION}}
        
ODPOWIEDŹ: 
"""


test3 = """
ARTYKUŁ:
###
Generative AI, znane również jako Sztuczna Inteligencja Generatywna, to obszar sztucznej inteligencji skupiający 
się na tworzeniu nowych danych, treści lub artefaktów przy użyciu algorytmów uczących się na podstawie istniejących 
danych. W przeciwieństwie do tradycyjnych algorytmów, które są zazwyczaj zaprogramowane do określonych zadań, Generative AI ma 
zdolność do tworzenia czegoś "nowego" poprzez analizę wzorców w dostępnych danych treningowych. Przykłady zastosowań Generative AI 
obejmują generowanie obrazów, muzyki, tekstu, a nawet deepfake'ów, które są realistycznymi manipulacjami wideo lub dźwięku.
###

PYTANIE: Jakie są zastosowania Generative AI w dzisiejszym świecie?

ODPOWIEDŹ: Generative AI ma szerokie zastosowanie w dzisiejszym świecie. Może być wykorzystywane do generowania realistycznych 
obrazów artystycznych, tworzenia muzyki komponowanej przez algorytmy, generowania opisów obrazów, projektowania odzieży, 
generowania tekstów literackich czy scenariuszy, a nawet do wspomagania procesu badawczego i eksploracji nowych koncepcji 
w różnych dziedzinach.


ARTYKUŁ: 
###
AI bias, znany również jako uprzedzenia algorytmiczne, to zjawisko, w którym systemy sztucznej inteligencji wykazują pewne 
formy uprzedzeń lub dyskryminacji w wynikach, które generują. Te uprzedzenia mogą wynikać z błędów w danych treningowych, 
na których uczy się algorytm, co może prowadzić do niesprawiedliwych lub nietrafnych decyzji. AI bias może być szczególnie 
problematyczny, gdy dotyczy to systemów podejmujących decyzje o zatrudnieniu, kredycie, opiece zdrowotnej czy innych istotnych 
aspektach życia, ponieważ może wprowadzać niesprawiedliwość i nieuczciwość w podejmowanych decyzjach.
###

PYTANIE: Jakie są potencjalne konsekwencje AI bias w praktycznych zastosowaniach?

ODPOWIEDŹ: AI bias może prowadzić do różnych niepożądanych konsekwencji. Na przykład, w systemach oceny wniosków o pracę, AI bias 
może prowadzić do wykluczenia pewnych grup społecznych z dostępu do pracy, co zwiększa nierówności. W medycynie, algorytmy oparte 
na błędnych danych mogą prowadzić do błędnych diagnoz lub niewłaściwego leczenia pacjentów.


ARTYKUŁ:
###
{{CONTEXT}}
###

PYTANIE: {{QUESTION}}

ODPOWIEDŹ: """


test4 = """
Artykuł:
###
{{CONTEXT}}
###

Odpowiedz na poniższe pytanie w jednym akapicie, korzystając tylko z informacji zawartych w artykule.
Odpowiadaj pełnym zdaniem, z zachowaniem właściwych znaków interpunkcyjnych i wielkich liter.
Jeśli w artykule nie ma dobrej odpowiedzi, powiedz „nie wiem”.

Pytanie: {{QUESTION}}
Odpowiedź: """


test5 = """
KONTEKST:
Generative AI, znane również jako Sztuczna Inteligencja Generatywna, to obszar sztucznej inteligencji skupiający się na tworzeniu nowych danych, treści lub artefaktów przy użyciu algorytmów uczących się na podstawie istniejących danych. W przeciwieństwie do tradycyjnych algorytmów, które są zazwyczaj zaprogramowane do określonych zadań, Generative AI ma 
zdolność do tworzenia czegoś "nowego" poprzez analizę wzorców w dostępnych danych treningowych. Przykłady zastosowań Generative AI obejmują generowanie obrazów, muzyki, tekstu, a nawet deepfake'ów, które są realistycznymi manipulacjami wideo lub dźwięku.
PYTANIE:
Jakie są zastosowania Generative AI w dzisiejszym świecie?
ODPOWIEDŹ:
Generative AI ma szerokie zastosowanie w dzisiejszym świecie. Może być wykorzystywane do generowania realistycznych obrazów artystycznych, tworzenia muzyki komponowanej przez algorytmy, generowania opisów obrazów, projektowania odzieży, generowania tekstów literackich czy scenariuszy, a nawet do wspomagania procesu badawczego i eksploracji nowych koncepcji w różnych dziedzinach. <<EOF>>


KONTEKST:
AI bias, znany również jako uprzedzenia algorytmiczne, to zjawisko, w którym systemy sztucznej inteligencji wykazują pewne formy uprzedzeń lub dyskryminacji w wynikach, które generują. Te uprzedzenia mogą wynikać z błędów w danych treningowych, na których uczy się algorytm, co może prowadzić do niesprawiedliwych lub nietrafnych decyzji. AI bias może być szczególnie 
problematyczny, gdy dotyczy to systemów podejmujących decyzje o zatrudnieniu, kredycie, opiece zdrowotnej czy innych istotnych aspektach życia, ponieważ może wprowadzać niesprawiedliwość i nieuczciwość w podejmowanych decyzjach.
PYTANIE:
Jakie są potencjalne konsekwencje AI bias w praktycznych zastosowaniach?
ODPOWIEDŹ:
AI bias może prowadzić do różnych niepożądanych konsekwencji. Na przykład, w systemach oceny wniosków o pracę, AI bias może prowadzić do wykluczenia pewnych grup społecznych z dostępu do pracy, co zwiększa nierówności. W medycynie, algorytmy oparte na błędnych danych mogą prowadzić do błędnych diagnoz lub niewłaściwego leczenia pacjentów. <<EOF>>


KONTEKST:
{{CONTEXT}}
PYTANIE:
{{QUESTION}}
ODPOWIEDŹ:
"""


test6 = """KONTEKST:
{{CONTEXT}}
PYTANIE:
{{QUESTION}}
ODPOWIEDŹ: """


test7="""
Poniżej znajduje się instrukcja opisująca zadanie. Napisz odpowiedź, która odnosi się do całej treści Artykułu.

### Instrukcja:
Odpowiedz w jednym akapicie na pytanie zadane do treści artykułu: {{QUESTION}}

Artykuł:
{{CONTEXT}}

### Odpowiedź:
"""





my_prompt = test7 

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
        #model_id    = ModelTypes.GPT_NEOX
        #model_id     = ModelTypes.MT0_XXL
        #model_id    = ModelTypes.FLAN_T5_XXL
        #model_id    = ModelTypes.FLAN_UL2
        gen_parms   = None
        project_id  = self.wxProjectid
        space_id    = None
        verify      = False

        return Model( model_id, wx_credentials, gen_parms, project_id, space_id, verify ) 
    
    def _remove_newline(self, input):
        if input.startswith('\n'):
            input = input[1:]
        if input.endswith('\n'):
            input = input[:-1]
        return input


    def genWX(self, prompt):
        gen_params_override = {  
            "decoding_method": "greedy",  
            "max_new_tokens": 500,  
            "min_new_tokens": 0,  
            "stop_sequences": [ ],  
            "repetition_penalty": 1 
        }
        generated_response = self.wxModel.generate( prompt, gen_params_override )
        retVal = {
            "output" : "",
            "prompt" : prompt
        }
        for resp in generated_response['results']:
            retVal["output"] = retVal["output"] + resp['generated_text']
        retVal["output"] = self._remove_newline(retVal["output"])
        return retVal
    
    def buildRAGPrompt(self, question, context):
        prompt_template=my_prompt


        prompt = prompt_template.replace('{{QUESTION}}',question).replace('{{CONTEXT}}',context)
        return prompt


if __name__ == '__main__':
    wx = wxService('./service.WX.cred')
    Q = "W jaki sposób projektuje się systemy sztucznej inteligencji wysokiego ryzyka?"
    C = "['1. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje się w taki sposób, w tym poprzez uwzględnienie odpowiednich narzędzi interfejsu człowiek-maszyna, aby w całym cyklu życia systemu sztucznej inteligencji wysokiego ryzyka mogły je skutecznie nadzorować osoby fizyczne, proporcjonalnie do ryzyka związanego z tymi systemami. Osoby fizyczne odpowiedzialne za zapewnienie nadzoru ze strony człowieka muszą posiadać wystarczający poziom kompetencji w zakresie sztucznej inteligencji zgodnie z art. 4b oraz należy im zapewnić niezbędne wsparcie i uprawnienia do pełnienia tej funkcji w okresie, w którym system sztucznej inteligencji jest używany, oraz do przeprowadzenia dokładnego dochodzenia po incydencie.', '1. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje się w sposób zapewniający wystarczającą przejrzystość ich działania, umożliwiającą dostawcom i użytkownikom racjonalne zrozumienie funkcjonowania systemu. Zapewnia się stopień przejrzystości odpowiedni do przeznaczenia systemu sztucznej inteligencji w celu osiągnięcia zgodności z odpowiednimi obowiązkami dostawcy i użytkownika, które określono w rozdziale 3 niniejszego tytułu. Przejrzystość oznacza zatem, że w momencie wprowadzania do obrotu systemu sztucznej inteligencji wysokiego ryzyka wykorzystuje się wszystkie dostępne środki techniczne zgodnie z powszechnie uznanym aktualnym stanem wiedzy, aby zapewnić dostawcy i użytkownikowi możliwość interpretacji wyników systemu sztucznej inteligencji. Użytkownik musi być w stanie zrozumieć system sztucznej inteligencji oraz korzystać z niego na podstawie ogólnej wiedzy na temat sposobu funkcjonowania systemu sztucznej inteligencji i przetwarzanych przez niego danych, dzięki czemu będzie on mógł wyjaśnić decyzje podjęte przez system sztucznej inteligencji osobom, których decyzje te będą dotyczyć zgodnie z art. 68 lit. c).', 'ba) jeżeli dokonują istotnych zmian w systemie sztucznej inteligencji, w tym systemie sztucznej inteligencji ogólnego przeznaczenia, który nie został sklasyfikowany jako system inteligencji wysokiego ryzyka i który wprowadzono już do obrotu lub oddano do użytku, w taki sposób, że system sztucznej inteligencji staje się systemem sztucznej inteligencji wysokiego ryzyka zgodnie z art. 6;', '2a. Systemy sztucznej inteligencji wysokiego ryzyka projektuje się i opracowuje tak, aby zawierały funkcję rejestracji zdarzeń umożliwiającą rejestrowanie zużycia energii, a także pomiar lub obliczanie zużycia zasobów oraz wpływu systemu sztucznej inteligencji wysokiego ryzyka na środowisko na wszystkich etapach jego cyklu życia.']"
    prompt = wx.buildRAGPrompt( Q, C )
    print(wx.genWX(prompt))