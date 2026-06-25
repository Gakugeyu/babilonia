from fastapi import FastAPI


from app.routes import livros

app = FastAPI(title="Bailônia", 
              version="1.0.0",
              description="Sistema de Cadastro de Livros para fins educativos")

app.include_router(livros.router)


@app.get("/")
def check_status():
    return {"status": "ok"}

