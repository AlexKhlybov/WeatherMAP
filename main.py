import uvicorn
from app.routers import routers
# from app.views import views    
from fastapi import FastAPI

import aiohttp

app = FastAPI()

app.include_router(routers.app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)