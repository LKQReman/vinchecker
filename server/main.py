from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from zeep import Client
from zeep.wsse.username import UsernameToken
from server.config import settings

client = Client('https://ws.vinlink.com/VLWS/services/Decoder?wsdl', wsse = UsernameToken(settings.USERNAME,settings.PASSWORD))
templates = Jinja2Templates(directory="templates")

tags_metadata = []

app = FastAPI(
    title="Humdov",
    description="Mobile",
    openapi_tags=tags_metadata
)
origins = ["*"]

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.post("/result")
async def process_vin(request: Request, vin: str = Form(...)):
    return templates.TemplateResponse("result.html", {"request": request, "vin": vin})