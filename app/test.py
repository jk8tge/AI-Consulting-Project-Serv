from fastapi import FastAPI
import os
from dotenv import load_dotenv
from openai import OpenAI

# **** OpenAI Testing Step 1: Edit this from prompt -> from fitness_scheme.py ****
from fitness_scheme import FitnessResponse, FitnessPrompt, fitness_prompt, SYSTEM_MSG

# OpenAI API key check
load_dotenv()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# **** OpenAI Testing Step 2: Edit this SYSTEM_MSG (this engineers the model system) ****


# **** OpenAI Testing Step 3: Build FitnessPrompt (this engineers the model system) ****
p = FitnessPrompt(
    physique={
        "height": 180,
        "weight": 85,
        "gender": "Male",
        "age": 35,
    },
    goalType="hypertrophy & weight cut",
    experience="Intermediate ~ advanced (2+ years consistent training)",
    hoursPerWeek=12,
    constraints="",
    preferences="",
    dietEffort="",
    startDate="2025-09-15",
    endDate="2025-09-22",
)



@app.get("/gerate_plan")
def generate_plan():
    try:
        return call_openai(p)
    

def call_openai(p: FitnessPrompt) -> FitnessResponse:
    # 1. curl
    # -> backend 리포가 있고 <- 서버구동
    # app은 앱이자나 이건 개인 기기 구동하는거잖아
    
    # 2. python -m 해가지ㅗㄱ return을 받아오은 ㄴ내장 라이브러리
    return response


///
curl -X POST https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \ 

///



# Pydantic Structured Input only
response = client.responses.parse(
    model=OPENAI_MODEL,
    input=[
        {
            "role": "system", 
            "content": SYSTEM_MSG
        },
        {
            "role": "user",
            "content": fitness_prompt(p)
        }
    ],
    # **** OpenAI Testing Step 3: Edit this Structured Output format ****
    text_format=FitnessResponse,
)

print(response.output_parsed)


response.daily[0].block[0].details[0].done = True