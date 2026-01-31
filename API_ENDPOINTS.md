# API Endpoints - PokéAPI Proxy
ROONEY ROJAS DE LA HOZ  

## Estructura del Proyecto

```
diplomado+/
├── main.py                    # Punto de entrada FastAPI
├── appsettings.py             # Configuración centralizada
├── clients/                   # Cliente HTTP para PokéAPI
├── services/                  # Lógica de negocio
├── controllers/               # Endpoints/rutas FastAPI
└── dtos/                      # Funciones de transformación
```

## Endpoints Disponibles

### `GET /`
**Descripción:** Endpoint de bienvenida que verifica que la API esté funcionando correctamente.

**Funcionamiento:**
- No requiere parámetros
- Retorna un mensaje de confirmación

**Respuesta:**
```json
{
  "message": "API FUNCIONANDO DIPLOMADO SEMANA 1 (PokéAPI)"
}
```

**Ejemplo de uso:**
```
GET http://localhost:8000/
```

---

### `GET /pokemon/{name_or_id}`
**Descripción:** Obtiene información completa de un Pokémon específico por su nombre o ID numérico.

**Funcionamiento:**
1. Recibe el nombre (ej: "pikachu") o ID (ej: "25") en la URL
2. Consulta la PokéAPI externa mediante el cliente HTTP
3. Transforma los datos usando DTOs para devolver solo información relevante
4. Retorna datos estructurados: ID, nombre, tipos, habilidades, estadísticas e imagen

**Parámetros:**
- `name_or_id` (path, requerido): Nombre del Pokémon en minúsculas o ID numérico

**Ejemplos de uso:**
```
GET /pokemon/pikachu
GET /pokemon/25
GET /pokemon/charizard
```

**Respuesta exitosa:**
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
    "special-attack": 50,
    "special-defense": 50,
    "speed": 90
  },
  "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
}
```

**Errores:**
- `404`: Pokémon no encontrado (nombre o ID inválido)
- `502`: Error al consultar PokéAPI (problema de conexión o servidor externo)

---

### `GET /pokemon/{name_or_id}/moves`
**Descripción:** Obtiene la lista de movimientos que puede aprender un Pokémon, con límite configurable.

**Funcionamiento:**
1. Busca el Pokémon por nombre o ID
2. Extrae todos los movimientos disponibles
3. Aplica un límite (entre 1 y 50) para controlar el tamaño de la respuesta
4. Retorna el nombre del Pokémon, total de movimientos, cantidad mostrada y la lista limitada

**Parámetros:**
- `name_or_id` (path, requerido): Nombre o ID del Pokémon
- `limit` (query, opcional): Cantidad de movimientos a mostrar (1-50, default: 10)

**Ejemplos de uso:**
```
GET /pokemon/pikachu/moves
GET /pokemon/pikachu/moves?limit=5
GET /pokemon/25/moves?limit=20
```

**Respuesta exitosa:**
```json
{
  "name": "pikachu",
  "total_moves": 102,
  "showing": 5,
  "moves": [
    "mega-punch",
    "mega-kick",
    "thunder-punch",
    "thunder-shock",
    "thunderbolt"
  ]
}
```

**Notas:**
- Si `limit` es mayor a 50, se ajusta automáticamente a 50
- Si `limit` es menor a 1, se ajusta automáticamente a 1
- `total_moves` muestra el número real de movimientos disponibles

**Errores:**
- `404`: Pokémon no encontrado
- `502`: Error al consultar PokéAPI

---

### `GET /type/{type_name}`
**Descripción:** Obtiene información sobre un tipo de Pokémon y una muestra de Pokémon que pertenecen a ese tipo.

**Funcionamiento:**
1. Recibe el nombre del tipo (fire, water, electric, etc.)
2. Consulta la PokéAPI para obtener todos los Pokémon de ese tipo
3. Retorna solo una muestra de 20 Pokémon para evitar respuestas muy grandes
4. Incluye el conteo total de Pokémon de ese tipo

**Parámetros:**
- `type_name` (path, requerido): Nombre del tipo en minúsculas

**Tipos disponibles:** fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy, normal

**Ejemplos de uso:**
```
GET /type/fire
GET /type/water
GET /type/electric
```

**Respuesta exitosa:**
```json
{
  "type": "fire",
  "pokemon_count": 75,
  "sample_20": [
    "charmander",
    "charmeleon",
    "charizard",
    "vulpix",
    "ninetales",
    ...
  ]
}
```

**Notas:**
- `pokemon_count` muestra el total real de Pokémon de ese tipo
- `sample_20` contiene solo los primeros 20 nombres para optimizar la respuesta
- El tipo se normaliza a minúsculas automáticamente

**Errores:**
- `404`: Tipo no encontrado (nombre inválido)
- `502`: Error al consultar PokéAPI

---

### `GET /random`
**Descripción:** Obtiene un Pokémon aleatorio del Pokédex nacional.

**Funcionamiento:**
1. Genera un ID aleatorio entre 1 y 1025 (rango configurable en `appsettings.py`)
2. Utiliza el mismo endpoint de búsqueda por ID
3. Retorna la información completa del Pokémon seleccionado

**Parámetros:**
- Ninguno

**Ejemplo de uso:**
```
GET /random
```

**Respuesta exitosa:**
Misma estructura que `GET /pokemon/{name_or_id}`:
```json
{
  "id": 42,
  "name": "golbat",
  "types": ["poison", "flying"],
  "abilities": ["inner-focus", "infiltrator"],
  "stats": {
    "hp": 75,
    "attack": 80,
    "defense": 70,
    ...
  },
  "image": "https://..."
}
```

**Notas:**
- El rango de IDs puede ajustarse en `appsettings.py`:
  - `RANDOM_POKEMON_MIN_ID = 1`
  - `RANDOM_POKEMON_MAX_ID = 1025`
- Cada llamada retorna un Pokémon diferente (aleatorio)

**Errores:**
- `502`: Error al consultar PokéAPI (muy raro, solo si falla la conexión) 