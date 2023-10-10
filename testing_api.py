# https://test-goldtech.rupiyatech.link/test/user_add

from fastapi import FastAPI, Header, Response, status, HTTPException, Query, Depends
from typing import List
from pydantic import BaseModel
import requests


app = FastAPI()

class demo_2(BaseModel):
    name: str
    age: int

class demo(BaseModel):
    c_id: str
    data: List[demo_2]




    
@app.post("/test/user_add")
def add_user(payload: demo, response: Response, tra_id: str = Header(...),device_id: str = Header(...)):
    if payload.c_id == '':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'success': 'failure', 'error_code': 400, 'msg': 'Customer Identification Number can not be blank', 'data': []}
    
    customer_id = payload.c_id
    data = payload.data

    if not customer_id or not data:
        raise HTTPException(status_code=400, detail="Invalid payload format")
    

    return{"message": "user added successfully"}




def f_get_all_user(tra_id, device_id):
    url = 'https://test-goldtech.rupiyatech.link/test/get_all_user'

    headers = {
        "Tra-ID": tra_id,
        "Device-ID": device_id
    }
    response = requests.request('GET', url, headers=headers)
    response_json = response.json()
    print('response ', response_json)
    if str(response_json['status']) == 'success' and str(response.status_code) == '200':
        
        return response_json
    else:
        return response_json

# [{'id': 1, 'user_name': 'jay', 'user_age': 20}, {'id': 2, 'user_name': 'jay', 'user_age': 20}]


@app.get("/test/get_all_users")
def get_all_users(response: Response, tra_id: str = Header(...),device_id: str = Header(...)):

        data = f_get_all_user(tra_id, device_id)

        # print(data['data'][0])
        # print(data['data'][0]['details'])
        print(data)

        if data['status'] == 'success' and len(data['data']) > 0:
            response.status_code = status.HTTP_200_OK
            return {'status': 'success', 'error_code': 200, 'msg': data['msg'], 'data': data['data'][0]['details']}
        
        elif data['status'] == 'failure':
            return {'status': 'failure', 'error_code': 400, 'msg': data['msg'], 'data': []}
        
        else:
            return {'status': 'failure', 'error_code': 400, 'msg': 'No data found', 'data': []}









# def get_user_by_id(id: int, tra_id, device_id):
#     url = f"https://test-goldtech.rupiyatech.link/test/{id}"

#     headers = {
#         "Tra-ID": tra_id,
#         "Device-ID": device_id
#     }
#     response = requests.request('GET', url, headers=headers)
#     response_json = response.json()
#     print('response ', response_json)
#     if str(response_json['status']) == 'success' and str(response.status_code) == '200':
        
#         return response_json
#     else:
#         return response_json
    


# @app.get("/test/{id}")
# def get_user_data(id: int, response: Response, tra_id: str = Header(...),device_id: str = Header(...)):
    
#     data = get_user_by_id(id, tra_id, device_id)
    
#     try:
#         data = (data['data'][0])
#         print(data)

#         if data['status'] == 'success' and len(data['data']) > 0:
#             response.status_code = status.HTTP_200_OK
#             return {'status': 'success', 'error_code': 200, 'msg': data, 'data': data['data'][0]['details']}
#         elif data['status'] == 'failure':
#             return {'status': 'failure', 'error_code': 400, 'msg': data['msg'], 'data': []}
#         else:
#             return {'status': 'failure', 'error_code': 400, 'msg': 'No data found', 'data': []}
#     except Exception as e:
#         print(f"Error fetching user data: {str(e)}")
#         return {'status': 'failure', 'error_code': 500, 'msg': 'No data found', 'data': []}
    








# def delete_user_by_id(url, id:int):
#     url = f"{url}/{id}"

#     try:
#         response = requests.delete(url)

#         if response.status_code == 200:
#             print(f"User with ID {id} has been deleted successfully.")
#         else:
#             print(f"Failed to delete user with ID {id}. Status code: {response.status_code}")

#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
        
# url = f"https://test-goldtech.rupiyatech.link/test/delete/{id}"
# delete_user_by_id(url, id)



# @app.delete("/test/delete/{id}")
# def delete_user_bi_id(id: int, response: Response, tra_id: str = Header(...),device_id: str = Header(...)):

#     headers={
#         "tra_id": tra_id,
#         "device_id": device_id
#     }

#     try:
#         user = id, headers
#         print(user)
#         if user:
#             return{"message": "user deleted successfully", "user": user}
#         else:
#             response.status_code = status.HTTP_404_NOT_FOUND
#     except Exception as e:
#         print(f'Error deleting user{str(e)}')
#         response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR