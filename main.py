from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    transfers = [
        {"date": "23/12/2020 22:11:49", "reference": "tr-20201223-000146", "from": "warehouse 2", "to": "warehouse 1", "cost": 34500, "tax": 4500, "total": 34500, "status": "Completed"},
        {"date": "19/10/2020 07:17:58", "reference": "tr-20201019-001798", "from": "warehouse 1", "to": "warehouse 2", "cost": 1, "tax": 0, "total": 1, "status": "Completed"},
        {"date": "08/12/2020 02:27:35", "reference": "tr-20201208-017736", "from": "warehouse 1", "to": "warehouse 2", "cost": 352, "tax": 32, "total": 352, "status": "Completed"},
        {"date": "22/02/2020 01:38:59", "reference": "tr-20200122-526504", "from": "warehouse 1", "to": "warehouse 2", "cost": 1000, "tax": 0, "total": 1000, "status": "Completed"},
        {"date": "06/12/2019 07:55:04", "reference": "tr-20191206-075504", "from": "warehouse 1", "to": "warehouse 3", "cost": 2, "tax": 0, "total": 2, "status": "Completed"},
        {"date": "08/08/2018 08:17:12", "reference": "tr-20210808-951712", "from": "warehouse 2", "to": "warehouse 1", "cost": 100, "tax": 0, "total": 100, "status": "Completed"},
    ]
    return templates.TemplateResponse("dashboard.html", {"request": request, "transfers": transfers})
