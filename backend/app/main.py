from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(title="RouteMaster API", version="1.0")

# Registrar rutas
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de RouteMaster 🚀"}
