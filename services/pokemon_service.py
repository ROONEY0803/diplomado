from clients.pokeapi_client import PokeAPIClient
from dtos.pokemon_dto import to_pokemon_dto, to_moves_dto, to_type_dto


class PokemonService:
    def __init__(self):
        self.client = PokeAPIClient()

    async def get_pokemon(self, name_or_id: str) -> dict:
        data = await self.client.get_pokemon(name_or_id)
        return to_pokemon_dto(data)

    async def get_moves(self, name_or_id: str, limit: int = 10) -> dict:
        data = await self.client.get_pokemon(name_or_id)
        return to_moves_dto(data, limit)

    async def get_type(self, type_name: str) -> dict:
        data = await self.client.get_type(type_name)
        return to_type_dto(data)
