from fastapi import FastAPI
from api import router 
import uvicorn 
from config import connect
app = FastAPI()

if __name__ == '__main__':
    
    cur=connect.cursor()
    print("соединение с бд успешно")
    
    with open("basa.sql", "r") as file:
        script=file.read()
        cur.execute(script)
        connect.commit()
        print("таблица успешно сохранена")
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8080)