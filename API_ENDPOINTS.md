# API Endpoints - PokéAPI Proxy

## Endpoints Disponibles

### `GET /`
Verifica que la API esté funcionando.

**Respuesta:**
```json
{
  "message": "API viva - Clase 3 (PokéAPI)"
}
```

---

### `GET /pokemon/{name_or_id}`
Obtiene información de un Pokémon por nombre o ID.

**Parámetros:**
- `name_or_id` (path): Nombre del Pokémon (ej: "pikachu") o ID numérico (ej: "25")

**Respuesta:**
```json
{
  "id": 25,
  "name": "pikachu",
  "types": ["electric"],
  "abilities": ["static", "lightning-rod"],
  "stats": {
    "hp": 35,
    "attack": 55,
    "defense": 40,
    ...
  },
  "image": "https://..."
}
```

**Errores:**
- `404`: Pokémon no encontrado
- `502`: Error al consultar PokéAPI

---

### `GET /pokemon/{name_or_id}/moves`
Obtiene los movimientos de un Pokémon.

**Parámetros:**
- `name_or_id` (path): Nombre o ID del Pokémon
- `limit` (query, opcional): Cantidad de movimientos a mostrar (1-50, default: 10)

**Ejemplo:**
```
GET /pokemon/pikachu/moves?limit=5
```

**Respuesta:**
```json
{
  "name": "pikachu",
  "total_moves": 102,
  "showing": 5,
  "moves": ["mega-punch", "mega-kick", ...]
}
```

---

### `GET /type/{type_name}`
Obtiene información de un tipo de Pokémon y una muestra de Pokémon de ese tipo.

**Parámetros:**
- `type_name` (path): Nombre del tipo (ej: "fire", "water", "electric")

**Respuesta:**
```json
{
  "type": "fire",
  "pokemon_count": 75,
  "sample_20": ["charmander", "charmeleon", ...]
}
```

**Nota:** Devuelve solo los primeros 20 Pokémon para evitar respuestas muy grandes.

---

### `GET /random`
Obtiene un Pokémon aleatorio del Pokédex nacional (ID 1-1025).

**Respuesta:**
Misma estructura que `GET /pokemon/{name_or_id}`.

**Ejemplo:**
```json
{
  "id": 42,
  "name": "golbat",
  "types": ["poison", "flying"],
  ...
}
```
