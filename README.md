# Bot 2.0

Bot de Discord hecho en Python con `discord.py` (versión con comandos, sucesora de [Bot-Discord](https://github.com/ItsTuki/Bot-Discord)).

## Comandos

Prefijo: `$`

| Comando | Qué hace |
|---|---|
| `$duck` | Envía una foto aleatoria de un pato usando la API pública [random-d.uk](https://random-d.uk). |
| `$mem` | Envía una imagen al azar de la carpeta `tukis/` (memes propios). |

## Requisitos

- Python 3.8 o superior
- Paquetes: `discord.py` y `requests`

```bash
pip install discord.py requests
```

## Cómo usarlo

1. Crea una aplicación y un bot en el [Portal de desarrolladores de Discord](https://discord.com/developers/applications) y activa el intent **Message Content**.
2. Crea una carpeta `tukis/` junto a `main.py` y pon dentro las imágenes que quieras que use `$mem`.
3. Reemplaza `"Token Here"` en la última línea de `main.py` por el token de tu bot (no lo subas a GitHub).
4. Ejecuta:

```bash
python main.py
```

## Estructura

```
main.py   # lógica del bot y comandos
tukis/    # imágenes para el comando $mem
```
