import uvicorn
from fastapi import FastAPI

from routers import missions, ranking, users

app = FastAPI()

app.include_router(users.router)
app.include_router(missions.router)
app.include_router(ranking.router)


@app.get("/")
def root():
    return {"message": "hello"}


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
