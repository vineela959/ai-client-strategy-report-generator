from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import uuid
import os

from ai_agent import generate_strategy


app = FastAPI(
    title="AI Client Strategy Report Generator"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create folders if missing
os.makedirs("reports", exist_ok=True)



@app.get("/")
def home():
    return FileResponse("index.html")



app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)



class ClientRequest(BaseModel):

    client_name: str
    industry: str
    goals: str



@app.post("/generate")
def generate_report(data: ClientRequest):

    try:

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
                    result.replace("\n", "<br/>"),
                    styles["BodyText"]
                )
            ]
        )


        return {

            "strategy_report": result,

            "pdf_file": "/" + filename

        }


    except Exception as e:

        print("GENERATE ERROR:", e)

        return {

            "error": str(e)

        }
