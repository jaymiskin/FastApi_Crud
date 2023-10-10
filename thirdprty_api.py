from fastapi import FastAPI, status, HTTPException, Header, Request
import requests
from requests.auth import HTTPBasicAuth

hey = url = "https://mystoreapi.com/catalog/products"

queryparalim = {"limit":"3","skip":"7"}

response = requests.request("GET", url, params=queryparalim)
# print(response.text)


# {"products":[{"id":6424,"name":"Pen","category":""},{"id":882186,"name":"Pen","category":""},{"id":882187,"name":"Pen","category":""}],"summary":{"count":288998}}




url = "https://mystoreapi.com/catalog/categories"
payload = {
        "categories": [
            {
                "category": "Refined"
            },
            {
                "category": "Towels"
            },
            {
                "category": "Tasty"
            },
            {
                "category": "Practical"
            },
            {
                "category": "Fantastic"
            },
            {
                "category": "Rustic"
            },
            {
                "category": "Generic"
            },
            {
                "category": "Incredible"
            },
            {
                "category": "micropunta"
            },
            {
                "category": "Gloves"
            },
            {
                "category": "Fish"
            },
            {
                "category": "c1"
            },
            {
                "category": "Intelligent"
            },
            {
                "category": "Handcrafted"
            },
            {
                "category": "Unbranded"
            },
            {
                "category": "Ergonomic"
            },
            {
                "category": "encdj"
            },
            {
                "category": "Gorgeous"
            },
            {
                "category": "Refined Concrete Mouse"
            },
            {
                "category": "kfajfdk"
            },
            {
                "category": "Testsept0"
            },
            {
                "category": "Awesome Soft Sausages"
            },
            {
                "category": "Refined Metal Table"
            },
            {
                "category": "sandeep2"
            },
            {
                "category": "Heran"
            },
            {
                "category": "c7"
            },
            {
                "category": "Handmade Cotton Chicken"
            },
            {
                "category": "0988"
            },
            {
                "category": "Masctoas"
            },
            {
                "category": "c2"
            },
            {
                "category": "dolls"
            },
            {
                "category": "Refined Fresh Cheese"
            },
            {
                "category": "sudaderas"
            }
        ]
}

payload = {"limit":"5","skip":"7"}

# print(len(payload))

response = requests.request("GET", url)

response = requests.request("GET", url, params=payload)

# print(response.text)


url = "https://mystoreapi.com/catalog/product/882193 "

response = requests.request("GET", url)

# print(response.text)



url = "https://mystoreapi.com/catalog/product/882139"

payloaded = ""
response = requests.request("DELETE", url, params=payloaded)
response = requests.request("DELETE", url, data=payloaded)


# print(response.text)


url = "https://mystoreapi.com/catalog/product"

payload = {
  "name": "Mehta Nishad",
  "price": 100000,
  "manufacturer": "Own",
  "category": "Male",
  "description": "Good Guy",
  "tags": "Nothing"
}
response = requests.request("POST", url, json=payload)

# print(response.text)



url = "https://mystoreapi.com/order/new"
payload1 = {
    "customer": "Mehta",
    "address": "Ahmedabbad"
}
response = requests.request("POST", url, json=payload1)
# print(response.text)



url = "https://mystoreapi.com/order/1020/product"

payload = {
    "productId": "74407",
    "amount": 100.2
}
response = requests.request("POST", url, json=payload)
# print(response.text)




url = "https://mystoreapi.com/order/10210025"

payload = ""
response = requests.request("DELETE", url, data=payload)

# print(response.text)



url = "https://mystoreapi.com/order/74416"

response = requests.request("GET", url)

# print(response.text)


url = "https://mystoreapi.com/order/74420/product/7440"
payload = ""
response = requests.request("DELETE", url, data=payload)
# print(response.text)



url = "https://mystoreapi.com/order/my"
headers = {"Authorization": ""}
response = requests.request("GET", url, headers=headers)
# print(response.text)



url = "https://mystoreapi.com/order/74424/place"
payload = ""
headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN0cmluZyIsInN1YiI6NDMwLCJpYXQiOjE2OTU5MDE2NDMsImV4cCI6MTY5NTkwMjI0M30.RHcpYFw3o7ccdthdIsEXT_3YIvhKyZ12osadD0onLUM"}
response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)








url = "https://mystoreapi.com/auth/login"

payload = {
    "username": "mikashing",
    "password": "hellomika"
}
response = requests.request("POST", url, json=payload)

# print(response.text)


url = "https://mystoreapi.com/auth/user"

payload = {
    "username": "mikash",
    "password": "hello"
}
response = requests.request("POST", url, data=payload)

# print(response.text)






auth = HTTPBasicAuth("username", "password")
response = requests.get("https://mystoreapi.com/order/my", auth=auth)
if response.status_code == 401:
    print("Authentication required")
if response.status_code == 200:
    print(response.content)




url = "https://mystoreapi.com/catalog/products"

querystring = {"skip":"6","limit":"10"}

headers = {
    "X-RapidAPI-Key": "24c296ddccmsh57433699557bde0p1924a0jsn00fb49a671b8",
    "X-RapidAPI-Host": "demo-project53626.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)




url = "https://demo-project53626.p.rapidapi.com/catalog/product"

payload = {
  "name": "Mehta Nishad",
  "price": 100000,
  "manufacturer": "Own",
  "category": "Male",
  "description": "Good Guy",
  "tags": "Nothing"
}

headers = {
    "X-RapidAPI-Key": "24c296ddccmsh57433699557bde0p1924a0jsn00fb49a671b8",
    "X-RapidAPI-Host": "demo-project53626.p.rapidapi.com",
    "username": "miskin",
    "password": "jay",
    "BLOG": "good"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)







url = "https://tomorrow-io1.p.rapidapi.com/v4/weather/forecast"

querystring = {"location":"42.15,82,1","timesteps":"1h","units":"metric"}

headers = {
	"X-RapidAPI-Key": "24c296ddccmsh57433699557bde0p1924a0jsn00fb49a671b8",
	"X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json())













url = "https://gorest.co.in/public/v2/users/5276287"

headers = {"accept": "application/json"}
response = requests.request("GET", url, headers=headers)

print(response.text)





url = "https://jsonplaceholder.typicode.com/posts"
response = requests.request("GET", url)
# print(response.json())




api_key = 'a9da779a58da1169a94996842e5600c2'
city = 'Patan'
country = 'India'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.request("GET", url)
print(response.json())