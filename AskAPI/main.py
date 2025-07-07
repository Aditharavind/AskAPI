from fastapi import FastAPI
import openai
import os
from fastapi.responses import JSONResponse


openai.api_key=os.getenv("openai_api_key")
app=FastAPI(title="AskAPI")

@app.get("/")
def home():
    return{"message":"Welcome to AskAPI"}
@app.get("/test-openai")
def test_openai():
    try:
        response=openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role":"user","content":"Say hello from AskAPI"}
            ]
        )
        return{"response":response.choices[0].message["content"]}
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})