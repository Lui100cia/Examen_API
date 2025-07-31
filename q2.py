from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/home", response_class=HTMLResponse)
async def hello():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Welcome home page<title/>
        </head>
        <body>
            <h1>Welcome home!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)