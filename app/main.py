from fastapi import FastAPI


from fastapi.staticfiles import StaticFiles

from app.routes import livros

app = FastAPI(title="Bailônia", 
              version="1.0.0",
              description="Sistema de Cadastro de Livros para fins educativos")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(livros.router)
app.include_router(livros.front_router)


@app.get("/")
def check_status():
    return {"status": "ok"}

