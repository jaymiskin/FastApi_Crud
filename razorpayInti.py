from fastapi import FastAPI, Response, status, HTTPException, Header, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import razorpay
import mysql.connector
import datetime
import time
from uuid import uuid4
import requests
import httpx
import json
import pytz
import traceback
from base64 import b64encode
from requests.auth import HTTPBasicAuth






# x = requests.delete('https://w3schools.com/python/demopage.php')

# print(x.text)


# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}

# headers = {'Content-Type': 'application/json', 'Tra-ID': '', 'Device-ID': ''}
# y = requests.request('POST', url, json = myobj, headers=headers)

app = FastAPI()

class Update(BaseModel):
    amount: int

# Initialize Razorpay
razorpay_client = razorpay.Client(auth=("rzp_test_eRWWigkEQZJa16", "UfHY9zYSeWYG91Joknn1wnVJ"))

while True:
    try:
        mysql_connection = conn = mysql.connector.connect(host='localhost', database='myfirst_schema', user='root', password='admin')
        mysql_connection = cursor = conn.cursor()
        print("============================== Database connection was succesfull! ==============================")
        break
    except Exception as error:
        print("////////////////////////////////////////// Connecting to database failed //////////////////////////////////////")
        print("Error:", error)
        time.sleep(3)


# Pydantic model for request data
class PaymentRequest(BaseModel):
    amount: int



def unique_receipt_id():
    uuid = uuid4()
    print(f'The Lenghth of receipt :- {len(uuid.hex)}')
    return uuid.hex


@app.post('/create_payment')
def create_payment(payment_request: PaymentRequest, Tran_ID: str = Header(...)):
    # Create a Razorpay order
    try:
        order_amount = payment_request.amount   # Amount in paise (100 paise = 1 INR)
        print(f'Order amount of user :- {order_amount}')
        order_currency = "INR"
        receipt_id = unique_receipt_id()
        notes = f"I'm paid my {order_amount}rs for clothes"
        razorpay_order = razorpay_client.order.create({
            'amount': (order_amount * 100),
            'currency': order_currency,
            'receipt': receipt_id,
            'notes': {'user_data': notes},
            'payment_capture': 1  # Automatically capture the payment
        })

        # Store Razorpay order details and transaction data in MySQL
        cursor = conn.cursor()
        insert_query = "INSERT INTO myfirst_schema.razorpay_table (id, amount, status, notes, receipt_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (razorpay_order['id'], order_amount, 'created', notes, receipt_id))
        conn.commit()
        cursor.close()

        return razorpay_order
    
    except Exception as error:
        print(error)
        # return {"message": "The amount must be atleast INR 1.00"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The amount must be atleast INR 1.00")



@app.get("/getallpost")
def get_posts():
    cursor.execute("""SELECT * FROM myfirst_schema.razorpay_table ORDER BY RAND() LIMIT 4""")

    getpost = cursor.fetchall()
    
    return {"post_details": getpost}



@app.delete("/deletepost/{id}")
def delete_posts(id: str):
    qry1 = f'SELECT id FROM myfirst_schema.razorpay_table WHERE id = "{id}"'
    # print(qry1)
    cursor.execute(qry1)
    data1 = cursor.fetchone()
    
    if data1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    else:
        cursor.execute(""" DELETE FROM myfirst_schema.razorpay_table WHERE id = %s """, (str(id),))
        delete_post = cursor.fetchone()
        conn.commit()
        return {delete_post : f"Deleted this id {id} Successfully"}
        raise HTTPException(delete_post, status_code=status.HTTP_204_NO_CONTENT, detail=f"Deleted this id {id} Successfully")
    


@app.put("/updateid/{id}")
def change_post(id: str, change_question: Update):
    qry = f'SELECT id FROM myfirst_schema.razorpay_table WHERE id = "{id}"'
    cursor.execute(qry)
    data = cursor.fetchone()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    else:
        cursor.execute("""UPDATE myfirst_schema.razorpay_table SET amount = %s WHERE id = %s""",(change_question.amount,str(id)))
        conn.commit()
        return {'Post Updated Successfully' : change_question}



# update new_table set product = 'Earbuds', serial_no = 5 where id = 5






# url1 = "https://api.razorpay.com/"
# # response = requests.request('GET', url1)
# # x = response.json()
# # print(x)



# url1 = "https://api.razorpay.com/v1/items"
# todo = {"userId": 1, "title": "Buy milk", "completed": True}
# headers =  {"Content-Type":"application/json"}
# # response = requests.request('POST', url1, data=json.dumps(todo), headers=headers)
# # y = response.json()
# # print(y)



# url1 = "https://api.razorpay.com"
# response = requests.request('GET', url1)
# z = response.json()
# {"userId": 9, 'id': 173, 'title': "harum ad aperiam quis", 'completed': False}
# # print(z)

# todo = {"userId": 9, 'id': 173, "title": "Wash car", "successfully complated": True}
# # response = requests.request('PUT', url1, data=todo)
# # ab = response.json()


# def convert_to_paisa(amt):
#     paisa = float(amt) * 100
#     return paisa


# def reference_id():
#     uuid = uuid4()
#     print(f'The Lenghth of receipt :- {len(uuid.hex)}')
#     return uuid.hex



# def description(reason):
#     if reason == 1:
#         return "This item is out of stock."
#     elif reason == 2:
#         return "Your account balance is too low."
#     elif reason == 3:
#         return "Invalid input. Please provide valid data."
#     else:
#         return "Unknown reason."

# reason = 2
# description = description(reason)

# def create_customer(c_name, mobile_no, email_id):
#     customer = {
#         "customer": {
#             "name": c_name,
#             "contact": "+91" + mobile_no,
#             "email": email_id
#         }
#     }
#     return customer

# c_name = "jay miskin"
# mobile_no = "1234567890"
# email_id = "jaymiskin@gmail.com"

# customer_data = create_customer(c_name, mobile_no, email_id)




# def basic_auth():
#     username = "jaymiskin007@gmail.com"
#     password = "alwaysjay28"
#     token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
#     print('token ', f'Basic {token}')
#     return f'Basic {token}'


# def create_callback_json(call_back_url):
#     callback_data = {
#         "callback_url": call_back_url
#     }
#     return json.dumps(callback_data)

# call_back_url = "https://example.com/callback"


# utc_time_str = str(datetime.datetime.now() + datetime.timedelta(minutes=15))




# name = (requests.get('https://api.razorpay.com/v1/payment_links/'))



# url = "https://api.razorpay.com/v1/payment_links/"
# try:
#     amt = convert_to_paisa(5000)
#     # trx_id = reference_id()
#     payload = json.dumps({
#             "amount": str(amt),
#             "currency": "INR",
#             "accept_partial": False,
#             "first_min_partial_amount": 0,
#             "expire_by": utc_time_str,
#             "reference_id": reference_id(),
#             "description": 'test',
#             "customer": {
#                 "name": c_name,
#                 "contact": "+91" + mobile_no,
#                 "email": email_id
#             },
#             "notify":{
#                 "sms": False,
#                 "email": False
#             },
#             "reminder_enable": 1,
#             "callback_url": call_back_url,
#             "callback_method": "get"

#         })


#     headers = {
#                 'Authorization': 'basic_auth()',
#                 'Content-Type': 'application/json'
#             }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print('hello ', response.text)

# except Exception as e:
#     print('exe ', traceback.format_exc())





# if name.status_code == 200:
#     data = name.json()
#     print(data)
# else:
#     print(f"Request failed with status code: {response.status_code}")

