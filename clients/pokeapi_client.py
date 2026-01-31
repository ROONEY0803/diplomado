import httpx
from typing import Dict, Any
from appsettings import AppSettings


class PokeAPIClient:
    def __init__(self):
        self.base_url = AppSettings.POKEAPI_BASE_URL
        self.timeout = AppSettings.POKEAPI_TIMEOUT

    async def get_pokemon(self, name_or_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/pokemon/{name_or_id.lower().strip()}"
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=self.timeout)
            if r.status_code == 404:
                raise ValueError("Pokémon no encontrado")
            if r.status_code != 200:
                raise ConnectionError("Error consultando PokéAPI")
            return r.json()

    async def get_type(self, type_name: str) -> Dict[str, Any]:
        url = f"{self.base_url}/type/{type_name.lower().strip()}"
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=self.timeout)
            if r.status_code == 404:
                raise ValueError("Tipo no encontrado")
            if r.status_code != 200:
                raise ConnectionError("Error consultando PokéAPI")
            return r.json()
