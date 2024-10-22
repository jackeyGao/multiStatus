from typing import Union
import subprocess
from fastapi import FastAPI

app = FastAPI()


@app.get("/pstatus")
def mongostatus():
    result = subprocess.run(["ps", "-ef"], capture_output=True, text=True)
    return {"stdout": result.stdout}
