from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import pyfiglet
from typing import Optional

# Create FastAPI instance
app = FastAPI(
    title="ASCII Art Generator API",
    description="A simple API to generate ASCII art from text",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint that returns a simple message"""
    return {"message": "ascii art generator"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "ascii-art-generator"}

@app.get("/ascii", response_class=PlainTextResponse)
async def generate_ascii_art(
    text: str = Query(..., description="Text to convert to ASCII art"),
    font: Optional[str] = Query("standard", description="Font style for ASCII art")
):
    """
    Generate ASCII art from the provided text
    
    Args:
        text: The text to convert to ASCII art
        font: The font style to use (default: standard)
    
    Returns:
        ASCII art representation of the text
    """
    try:
        # Generate ASCII art using pyfiglet
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        # If font is not found, fall back to standard font
        ascii_art = pyfiglet.figlet_format(text, font="standard")
        return ascii_art

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
