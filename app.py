
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Look for 'templates' folder in the same directory as this file
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    print("✅ Dashboard route hit")
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": "Admin"
    })
