import random
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="PokeAPI Proxy - Clase 3")

POKE_BASE = "https://pokeapi.co/api/v2"


@app.get("/")
def home():
    return {"message": "API viva - Clase 3 (PokéAPI)"}


@app.get("/pokemon/{name_or_id}")
async def get_pokemon(name_or_id: str):
    url = f"{POKE_BASE}/pokemon/{name_or_id.lower().strip()}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=10)

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Error consultando PokéAPI")

    data = r.json()

    return {
        "id": data["id"],
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "image": data["sprites"]["other"]["official-artwork"]["front_default"],
    }


@app.get("/pokemon/{name_or_id}/moves")
async def get_moves(name_or_id: str, limit: int = 10):
    url = f"{POKE_BASE}/pokemon/{name_or_id.lower().strip()}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=10)

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Error consultando PokéAPI")

    data = r.json()
    moves = [m["move"]["name"] for m in data["moves"]]

    # limit entre 1 y 50 para que no explote la respuesta
    limit = max(1, min(limit, 50))

    return {
        "name": data["name"],
        "total_moves": len(moves),
        "showing": limit,
        "moves": moves[:limit],
    }


@app.get("/type/{type_name}")
async def get_type(type_name: str):
    url = f"{POKE_BASE}/type/{type_name.lower().strip()}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=10)

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Tipo no encontrado")
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Error consultando PokéAPI")

    data = r.json()

    # devolvemos solo una muestra de pokémon del tipo, para no mandar una lista gigante
    pokemon_list = [p["pokemon"]["name"] for p in data["pokemon"]]
    sample = pokemon_list[:20]

    return {
        "type": data["name"],
        "pokemon_count": len(pokemon_list),
        "sample_20": sample,
    }


@app.get("/random")
async def random_pokemon():
    # Pokédex nacional ~ 1..1025 (puedes ajustar si quieres)
    random_id = random.randint(1, 1025)
    return await get_pokemon(str(random_id))
