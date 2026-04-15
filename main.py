from fastapi import FastAPI

app = FastAPI()

# This handles GET requests to the root "/"
@app.get("/")
async def read_root():
    return {"message": "API is running"}

# A health check for monitoring tools
@app.get("/health")
async def health_check():
    return {"message": "healthy"}

# Your personal info endpoint
@app.get("/me")
async def get_me():
    return {
        "name": "Ajayi Oluwatise",
        "email": "dr393462@gmail.com",
        "github": "https://github.com/Oluwatise-Ajayi"
    }