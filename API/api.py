
# Initialize variables during module import
print("DEBUG: Initializing module api.py.")
from flask import abort, jsonify
from wd import wdService
from wx import wxService

wd = wdService('./service.WD.cred')
wx = wxService('./service.WX.cred')

# Hardcoded API key for demonstration purposes
API_KEY = 'ala_ma_kota'

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
            context = context + passage['text']
        #print(context)
        prompt = wx.buildRAGPrompt(question, context)
        wx_results = wx.genWX(prompt)
        #print(wx_results)
        retVal =  jsonify({"question": question, 'answer': wx_results, 'source' : wd_results})
        return retVal,200
    else:
        abort(
            400,
            "No question provided.",
        )

    
   
