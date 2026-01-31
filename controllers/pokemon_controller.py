import random
from fastapi import APIRouter, HTTPException
from services.pokemon_service import PokemonService
from appsettings import AppSettings

router = APIRouter()
service = PokemonService()


@router.get("/pokemon/{name_or_id}")
async def get_pokemon(name_or_id: str):
    try:
        return await service.get_pokemon(name_or_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/pokemon/{name_or_id}/moves")
async def get_moves(name_or_id: str, limit: int = 10):
    try:
        return await service.get_moves(name_or_id, limit)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/type/{type_name}")
async def get_type(type_name: str):
    try:
        return await service.get_type(type_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/random")
async def random_pokemon():
    random_id = random.randint(
        AppSettings.RANDOM_POKEMON_MIN_ID,
        AppSettings.RANDOM_POKEMON_MAX_ID
    )
    try:
        return await service.get_pokemon(str(random_id))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))
