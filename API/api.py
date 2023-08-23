
# Initialize variables during module import
print("DEBUG: Initializing module api.py.")
from flask import abort, jsonify
from wd import wdService
from wx import wxService

wd = wdService('./service.WD.cred')
wx = wxService('./service.WX.cred')

# Hardcoded API key for demonstration purposes
TOKEN_DB = {
                "e6208484c8548f40d9a18c27bc9286a0a1dba0ab4979146460f1cc2d92635e33": {"username": "User01"},
                "544ae5b1fb60e449db5ff6f1666cfbab779cd7eaa044e4f1bad2df7e300bc797": {"username": "User02"}
            }


def apikeyAuth(token):
    info = TOKEN_DB.get(token, None)
    if not info:
        abort(
            400,
            "Invalid api key.",
        )
    print("INFO: user " + info["username"] + " authenticated.")
    return info

def ping():
    return "pong"

def rag(inputData):
    #print(inputData)
    question = inputData.get("question")
    #print(type(question))
    if question:
        wd_results = wd.queryWD(question)
        context = ""
        for passage in wd_results:
            if len(context) < 2000:
                context = context + passage['text']
        #print(context)
        prompt = wx.buildRAGPrompt(question, context)
        wx_results = wx.genWX(prompt)
        #print(wx_results)
        retVal =  jsonify({"question": question, 'answer': wx_results["output"], 'source' : wd_results, "prompt": wx_results["prompt"]})
        return retVal,200
    else:
        abort(
            400,
            "No question provided.",
        )

def ragBAM(inputData):
    #print(inputData)
    question = inputData.get("question")
    #print(type(question))
    if question:
        wd_results = wd.queryWD(question)
        context = ""
        for passage in wd_results:
            if len(context) < 2000:
                context = context + passage['text']
        #print(context)
        PT = "<s>[INST]" + \
            "<<SYS>>Jesteś bardzo pomocnym asystentem. Zawsze podajesz zwięzłe odpowiedzi w maksymalnie 4 zdaniach. Dostałeś informacje w formie fragmentów tekstu.<</SYS>>\n" + \
            "Używając wyłacznie informacji podanych poniżej odpowiedz w jednym krótkim akapicie na pytanie postawione na końcu\n\n" + \
            "Podane informacje:\n" + \
            "{{CONTEXT}}\n" + \
            "[/INST]\n\n" +\
            "PYTANIE: {{QUESTION}}\n" + \
            "ODPOWIEDŹ: "
        prompt = wx.buildRAGPrompt(question, context, promptTemplate=PT)
        wx_results = wx.genBAM(prompt)
        #print(wx_results)
        retVal =  jsonify({"question": question, 'answer': wx_results["output"], 'source' : wd_results, "prompt": wx_results["prompt"]})
        return retVal,200
    else:
        abort(
            400,
            "No question provided.",
        )
