import sys
import os
import json
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model

### required for BAM
from genai.credentials import Credentials
from genai.schemas import GenerateParams
from genai.model import Model as GenAIModel

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
Below is an instruction describing the task. Write an answer that addresses the entire content of the Article.

### Instructions:
Answer the question posed to the article in one paragraph: {{QUESTION}}

Article:
{{CONTEXT}}

### Answer:
"""

my_prompt = test7 

class wxService:
    def __init__(self, configFile):
        self.configFile = configFile
        self._readConfig()
        self.wxModel = self._crWX()
        self.bamModel = self._crBAM()

    def _readConfig(self):
        with open(self.configFile, 'r') as json_file:
            data = json.load(json_file)
            self.wxApiKey = data['apikey']
            self.wxUrl = data['url']
            self.wxProjectid = data['projectid']
            #print(self.wxApiKey, self.wxUrl)
            self.bamApiKey = ""
            self.bamUrl    = ""
            try:
                self.bamApiKey = data['bam-apikey']
                self.bamUrl    = data['bam-url']
            except Exception as e:
                pass
            #print("DEBUG: BAM config", self.bamApiKey, self.bamUrl)
             
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
        gen_params   = None
        project_id  = self.wxProjectid
        space_id    = None
        verify      = False

        return Model( model_id, wx_credentials, gen_params, project_id, space_id, verify ) 
    
    def _crBAM(self):
        if( self.bamApiKey != "" and self.bamUrl != ""):
            bam_credentials = Credentials(api_key=self.bamApiKey, api_endpoint=self.bamUrl)
            #print(bam_credentials.DEFAULT_API)
            #print(bam_credentials.api_key, bam_credentials.api_endpoint)
            bam_params      = GenerateParams(decoding_method="greedy", max_new_tokens=500)
            bam_modelName   = "meta-llama/llama-2-70b-chat"

            return GenAIModel(bam_modelName, credentials=bam_credentials, params=bam_params)
        else:
            return None

    def _remove_newline(self, input):
        if input.startswith('\n'):
            input = input[1:]
        if input.endswith('\n'):
            input = input[:-1]
        return input
    
    def _countWords(self, text):
        # Split the text into words using whitespace as the delimiter
        words = text.split()
        
        # Count the number of words
        word_count = len(words)
        
        return word_count

    def buildRAGPrompt(self, question, context, promptTemplate=""):
        if promptTemplate == "":
            promptTemplate = my_prompt
        prompt = promptTemplate.replace('{{QUESTION}}',question).replace('{{CONTEXT}}',context)
        return prompt

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
    
    def genBAM(self, prompt):
        if self.bamModel is not None:
            retVal = {
                "output" : "",
                "prompt" : prompt
            }
            print("DEBUG: here is the prompt: ", prompt )
            print("DEBUG: prompt length in words ", self._countWords( prompt ) )
            generated_response = self.bamModel.generate([prompt])
            for resp in generated_response:
                retVal["output"] = retVal["output"] + self._remove_newline(resp.generated_text)
            return retVal
        else:
            return None
    


if __name__ == '__main__':
    wx = wxService('./service.WX.cred')
    Q = "How are high-risk AI systems designed?"
    C = "['1. High-risk artificial intelligence systems shall be designed and developed in such a way, including by incorporating appropriate human-machine interface tools, that they can be effectively overseen by natural persons throughout the lifecycle of the high-risk artificial intelligence system, proportionate to the risk related to those systems. The natural persons responsible for providing human oversight shall have a sufficient level of competence in artificial intelligence in accordance with Article 4b and shall be provided with the necessary support and authority to perform this function during the period in which the artificial intelligence system is used , and to conduct a thorough post-incident investigation.', '1. High-risk AI systems shall be designed and developed to provide sufficient transparency of their operation to enable providers and users to reasonably understand the functioning of the system. A degree of transparency shall be provided that is appropriate to the purpose of the AI ​​system. intelligence in order to comply with the respective supplier and user obligations set out in Chapter 3 of this Title. Transparency therefore means that when a high-risk AI system is placed on the market, all available technical means are used, in accordance with the generally recognized state of the art, to ensure that the supplier and user can interpret the results of the AI ​​system. You must be able to understand and use the AI ​​system based on a general knowledge of how the AI ​​system works and the data it processes, so that you can explain decisions made by the AI ​​system to those affected by those decisions in accordance with joke. 68 lit. (c).', 'ba) if they make material changes to an artificial intelligence system, including a general purpose artificial intelligence system that is not classified as a high-risk intelligence system and that has already been placed on the market or put into service, in such a way that the artificial intelligence system becomes a high-risk artificial intelligence system in accordance with Art. 6;', '2a. High-risk AI systems shall be designed and developed to include event logging functionality to record energy consumption and measure or calculate resource consumption and the environmental impact of the high-risk AI system at all stages of its life cycle.']"
    PT = "<s>[INST]" + \
            "<<SYS>>You are a very helpful assistant. You always give concise answers in no more than 4 sentences. You received information in the form of text fragments.<</SYS>>\n" + \
         "Using only the information provided below, answer the question at the end in one short paragraph\n\n" + \
         "Information provided:\n" + \
         "{{CONTEXT}}\n" + \
         "[/INST]\n\n" +\
         "QUESTION: {{QUESTION}}\n" + \
         "ANSWER: "
    prompt = wx.buildRAGPrompt( Q, C, PT )
    print(prompt)
    print(wx.genBAM(prompt)['output'])