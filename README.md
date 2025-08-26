# ASCII Art Generator API

A FastAPI backend service that generates ASCII art from text input.

## Features

- **Root endpoint** (`/`): Returns a welcome message
- **Health check** (`/health`): Returns service health status
- **ASCII art generation** (`/ascii`): Converts text to ASCII art with customizable fonts

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

   Or using uvicorn directly:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the API:**
   - Server will start at: `http://localhost:8000`
   - Interactive API docs: `http://localhost:8000/docs`
   - ReDoc documentation: `http://localhost:8000/redoc`

## API Endpoints

### GET /

Returns a welcome message.

**Response:**

```json
{
  "message": "ascii art generator"
}
```

### GET /health

Health check endpoint.

**Response:**

```json
{
  "status": "healthy",
  "service": "ascii-art-generator"
}
```

### GET /ascii

Generate ASCII art from text.

**Parameters:**

- `text` (required): Text to convert to ASCII art
- `font` (optional): Font style to use (default: "standard")

**Example requests:**

```bash
# Basic usage
curl "http://localhost:8000/ascii?text=Hello"

# With custom font
curl "http://localhost:8000/ascii?text=Hello&font=slant"
```

**Example response:**

```
 _   _      _ _
| | | | ___| | | ___
| |_| |/ _ \ | |/ _ \
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/
```

## Available Fonts

Some popular pyfiglet fonts you can use:

- `standard` (default)
- `slant`
- `3x5`
- `3d`
- `banner`
- `big`
- `block`
- `bubble`
- `digital`
- `mini`

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pyfiglet**: Python library for generating ASCII art text
