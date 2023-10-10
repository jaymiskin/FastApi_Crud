from fastapi import FastAPI, Response, status, HTTPException
from typing import Optional
from pydantic import BaseModel
import mysql.connector
import time



while True:
    try:
        conn = mysql.connector.connect(host='localhost', database='myfirst_schema', user='root', password='admin')
        cursor = conn.cursor()
        print("============================== Database connection was succesfull! ==============================")
        break
    except Exception as error:
        print("////////////////////////////////////////// Connecting to database failed //////////////////////////////////////")
        print("Error:", error)
        time.sleep(3)


app = FastAPI()


class Schema(BaseModel):
    product: str
    serial_no: int


class Update(BaseModel):
    product: str
    serial_no: int


@app.get("/")
def root():
    return{"DataBase": "Your Localhost id is 127.0.0.1:8000"}



@app.get("/getposts", tags=["Add, Update, Delete & Get MySQL Database table"])
def get_posts():
    cursor.execute("""SELECT * FROM new_table ORDER BY RAND() LIMIT 10""")

    getpost = cursor.fetchall()

    # if not getpost:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id was not found")
    
    return {"post_details": getpost}



@app.post("/addtable/", status_code=status.HTTP_201_CREATED, tags=["Add, Update, Delete & Get MySQL Database table"])
def create_subject(new_subject: Schema):
    cursor.execute("""INSERT INTO myfirst_schema.new_table (product, serial_no) VALUES (%s, %s)""",(new_subject.product, new_subject.serial_no))
    conn.commit()
    return {"data_added_successfully": new_subject}




@app.put("/changepost/{id}", status_code=status.HTTP_205_RESET_CONTENT, tags=["Add, Update, Delete & Get MySQL Database table"])
def change_post(id: int, change_question: Update):
    qry = f"SELECT id FROM new_table WHERE id = {id}"
    cursor.execute(qry)
    data = cursor.fetchone()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    else:
        cursor.execute("""UPDATE myfirst_schema.new_table SET  product = %s, serial_no = %s WHERE id = %s""",(change_question.product,change_question.serial_no,str(id)))
        conn.commit()
        return {'Post Updated Successfully' : change_question}
    


@app.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Add, Update, Delete & Get MySQL Database table"])
def delete_posts(id: int):
    qry1 = f"SELECT id FROM new_table WHERE id = {id}"
    cursor.execute(qry1)
    data1 = cursor.fetchone()

    
    if data1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    else:
        cursor.execute("""DELETE FROM myfirst_schema.new_table WHERE id = %s""", (str(id),))
        delete_post = cursor.fetchone()
        conn.commit()
        return {delete_post : f"Deleted this id {id} Successfully"}