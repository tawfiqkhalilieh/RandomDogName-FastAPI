import json
import random
from fastapi import *

app = FastAPI()

@app.get("/")
def dogs():
    with open('dogs.json', 'r') as f:
        rnd = random.randrange(706)
        data = json.load(f)
        return data["names"][rnd]
     
     
if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=4557, reload=True, debug=True, workers=3)
