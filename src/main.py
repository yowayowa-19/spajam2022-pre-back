from fastapi import FastAPI
from routers import users, missions, ranking
import uvicorn


app = FastAPI()


def main():
    app.include_router(users.router)
    app.include_router(missions.router)
    app.include_router(ranking.router)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
