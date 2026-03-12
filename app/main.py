from fastapi import FastAPI
from routes import auth_routes, project_routes, dpr_routes

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(project_routes.router, prefix="/projects", tags=["Projects"])
app.include_router(dpr_routes.router, prefix="/projects", tags=["DPR"])