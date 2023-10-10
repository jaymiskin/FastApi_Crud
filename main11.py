from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import List 

# from random import randint
import psycopg2
import psycopg2.extras 
import time

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello this is my crud operation"}

class Subject(BaseModel):
    subject: str
    subject_active: bool = True


class Question(BaseModel):
    question: str
    answer: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    subject_id: int


class example(BaseModel):
    id: int
    ans: str

class exm(BaseModel):
    item: List[example]


@app.post("/currrentquestion", tags=["crud_operation"])
def example1(item: exm):
    if len(item.item) != 10:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Questions are no 10')
    
    correct_ans = 0
    incorrect_ans = 0
    
    percentage = (9 / 10) * 100
    print("Percentage: ", percentage, "%" )

    for ada in item.item:
        cursor.execute(f""" SELECT option_c, option_d FROM updatequestion WHERE id = {ada.id};""")
        data = cursor.fetchone()

        if data == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Questions with ID: {ada.id} not found')

        cursor.execute(""" SELECT answer FROM updatequestion WHERE id = %s AND answer = %s; """, (ada.id, ada.ans))
        updated_post1 = cursor.fetchone()

        if updated_post1 == None:
            incorrect_ans +=1
        else:
            correct_ans += 1

    return {'correct' : correct_ans, 'wrong_ans': incorrect_ans}  

    



while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin', cursor_factory=psycopg2.extras.RealDictCursor)
        cursor = conn.cursor()
        print("============================== Database connection was succesfull! ==============================")
        break
    except Exception as error:
        print("////////////////////////////////////////// Connecting to database failed //////////////////////////////////////")
        print("Error:", error)
        time.sleep(3)


@app.post("/createsubject", status_code=status.HTTP_201_CREATED, tags=["crud_operation"])
def create_subject(new_subject: Subject):
    cursor.execute("""INSERT INTO crud (subject, subject_active) VALUES (%s, %s) RETURNING * """,(new_subject.subject, new_subject.subject_active))
    db_post = cursor.fetchone()
    conn.commit()
    return {"data_added": db_post}




@app.post("/updatepost/", status_code=status.HTTP_201_CREATED, tags=["crud_operation"])
def create_question(new_questions: Question):
    cursor.execute("""INSERT INTO updatequestion (question, answer, option_a, option_b, option_c, option_d, subject_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING * """,
                   (new_questions.question, new_questions.answer, new_questions.option_a, new_questions.option_b, new_questions.option_c, new_questions.option_d, new_questions.subject_id))
    db_posted = cursor.fetchone()
    conn.commit()
    return {"data_added_successfully": db_posted}




@app.put("/updatepost/{id}", status_code=status.HTTP_201_CREATED, tags=["crud_operation"])
def update_post(id: int, update_question: Question):
    
    cursor.execute("""UPDATE updatequestion SET question = %s, answer = %s, option_a = %s, option_b = %s, option_c = %s, option_d = %s , subject_id = %s WHERE id = %s RETURNING *""", 
                   (update_question.question,update_question.answer,update_question.option_a,update_question.option_b,update_question.option_c,update_question.option_d,update_question.subject_id,str(id)))
    updated_post = cursor.fetchall()
    conn.commit()

    if updated_post == None or not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    return {'data_updated' : updated_post}  


@app.get("/getposts/{id}", tags=["crud_operation"])
def get_posts(id: int, response: Response):
    cursor.execute("""SELECT * FROM updatequestion WHERE subject_id  = %s ORDER BY RANDOM() limit 10 """, (str(id),))

    getpost = cursor.fetchall()

    if not getpost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    return {"post_details": getpost}


@app.post("/currentquestion/{id}", tags=["crud_operation"])
def current_ans(id: int):
    cursor.execute("""SELECT * FROM updatequestion ORDER BY id """, (str(id),))
    getquestion= cursor.fetchall()


    if not getquestion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_details": getquestion}