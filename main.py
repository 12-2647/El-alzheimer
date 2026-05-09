from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/sintomas", response_class=HTMLResponse)
async def sintomas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="sintomas.html"  
    )

@app.get("/causas", response_class=HTMLResponse)
async def causas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="causas.html"  
    )   

@app.get("/diagnostico", response_class=HTMLResponse)
async def diagnostico(request: Request):   
    return templates.TemplateResponse(
        request=request,
        name="diagnostico.html"  
    )

@app.get("/tratamiento", response_class=HTMLResponse)
async def tratamiento(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="tratamiento.html"  
    )

@app.get("/contacto", response_class=HTMLResponse)
async def contacto(request: Request):  
    return templates.TemplateResponse(
        request=request,
        name="contacto.html"  
    )