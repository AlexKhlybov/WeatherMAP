import uvicorn
from app.routers import routers
# from app.views import views    
from fastapi import FastAPI

import aiohttp

app = FastAPI()

# session = None

# @app.on_event('startup')
# async def startup_event():
#     global session 
#     session = aiohttp.ClientSession()

# @app.on_event('shutdown')
# async def shutdown_event():
#     await session.close()

app.include_router(routers.app)
# app.include_router(views.app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)