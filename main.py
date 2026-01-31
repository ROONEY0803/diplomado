from fastapi import FastAPI
from controllers.pokemon_controller import router

app = FastAPI(title="PokeAPI Proxy - Clase 3")
app.include_router(router)


@app.get("/")
def home():
    return {"message": "API FUNCIONANDO DIPLOMADO SEMANA 1 (PokéAPI)"}
