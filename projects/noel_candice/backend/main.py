from fastapi import FastAPI

app = FastAPI()


@app.get("/greet/{username}")  # type: ignore
async def greet_user(username: str) -> dict[str, str]:
    return {"message": f"Hello {username}"}
