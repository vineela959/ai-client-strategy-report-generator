from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import uuid

from backend.ai_agent import generate_strategy


app = FastAPI(
    title="AI Client Strategy Report Generator"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount(
    "/frontend",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)


app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)



class ClientRequest(BaseModel):

    client_name: str
    industry: str
    goals: str



@app.get("/")
def home():

    return {
        "message":"API running"
    }



@app.post("/generate")
def generate_report(data: ClientRequest):


    result = generate_strategy(
        data.client_name,
        data.industry,
        data.goals
    )


    filename = f"reports/{uuid.uuid4()}.pdf"


    pdf = SimpleDocTemplate(filename)


    styles = getSampleStyleSheet()


    pdf.build(
        [
            Paragraph(
                result.replace("\n","<br/>"),
                styles["BodyText"]
            )
        ]
    )


    return {

        "strategy_report": result,

        "pdf_file": "/" + filename

    }