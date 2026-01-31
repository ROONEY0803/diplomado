from typing import Dict, Any
from appsettings import AppSettings


def to_pokemon_dto(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": data["id"],
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "image": data["sprites"]["other"]["official-artwork"]["front_default"],
    }


def to_moves_dto(data: Dict[str, Any], limit: int) -> Dict[str, Any]:
    moves = [m["move"]["name"] for m in data["moves"]]
    limit = max(
        AppSettings.MOVES_LIMIT_MIN,
        min(limit, AppSettings.MOVES_LIMIT_MAX)
    )
    return {
        "name": data["name"],
        "total_moves": len(moves),
        "showing": limit,
        "moves": moves[:limit],
    }


def to_type_dto(data: Dict[str, Any]) -> Dict[str, Any]:
    pokemon_list = [p["pokemon"]["name"] for p in data["pokemon"]]
    return {
        "type": data["name"],
        "pokemon_count": len(pokemon_list),
        "sample_20": pokemon_list[:AppSettings.TYPE_SAMPLE_SIZE],
    }
