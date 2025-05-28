import subprocess
subprocess.run("pip install -r requirements.txt")
subprocess.run("pip install torch==2.3.1+cu121 torchvision==0.18.1+cu121 torchaudio==2.3.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html")
import uvicorn
import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
import traceback
from Evaluate import *
app = FastAPI()

class conversation(BaseModel):
    question:str
    bot_answer:str
    real_answer:str

@app.post("/evaluate/")
def Evaluate(conversation: conversation):
    return evaluate(conversation.question,conversation.bot_answer,conversation.real_answer)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2222)