import sys
import os

# Add the python directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python'))

# Import the FastAPI app from the main server
try:
    from valuecell.server.api.app import create_app
    
    # Create the app instance
    app = create_app()
    
    # Vercel expects the app to be available at module level
    handler = app
    
except ImportError as e:
    # Fallback in case of import issues
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
        return {"message": "ValueCell API", "error": f"Import error: {str(e)}"}
    
    @app.get("/health")
    async def health():
        return {"status": "ok"}
    
    handler = app