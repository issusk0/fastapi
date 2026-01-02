from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def hello_world():
    data = {
        "Message": "Hello world"
    }
    return JSONResponse(
        content=data,
        status_code=status.HTTP_200_OK,
        headers=None
    )
@app.put("/")
def write_data(data: str):
    with open("test.txt", "a+") as f:
        f.write(data + "\n")
        f.seek(0)
        return JSONResponse(
            content= f.read(),
            status_code=status.HTTP_200_OK,
            headers=None,
        )


#i quit i didnt like it is fucking ass