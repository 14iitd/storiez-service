import starlette.responses
from fastapi import FastAPI


from starlette.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.responses import FileResponse

@app.get("/")
async def health_check():

    return FileResponse("home.html")
@app.get("/")
async def health_check():

    return FileResponse("home.html")


@app.get("/p/{post_id}")
async def get_onePost(post_id:str):
    import requests
    res=requests.get(f"https://playchat.live/storiez/post/{post_id}")

    return starlette.responses.Response(res.text)

@app.get("/privacy")
async def health_check():

    return FileResponse("privacy.html")
app.mount("/", StaticFiles(directory="pages", html = True), name="html5")

# If this script is executed, run the FastAPI application directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)