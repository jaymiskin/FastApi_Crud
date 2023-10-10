from fastapi import FastAPI
import razorpay
from fastapi import FastAPI, HTTPException
from fastapi import Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



client_id = razorpay.Client(auth=("rzp_test_LDeNYi74fpVhxz", "hTpRr6dC1DrXJ17FlRLIN76h"))
@app.post("/create-order")
def create_order(amount: int):
    try:
        response = client_id.order.create({"amount": amount, "currency": "INR", "receipt": "order_rcptid_11", "notes": [f"I'm paid my {amount}rs for my clothes"]})
        # data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
        # payment = client_id.order.create(data=data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/webhook")
async def webhook(request: Request):
    try:
        request_data = await request.json()
        # Validate Razorpay webhook signature here
        # Process the webhook event
        # return {"status": "Webhook received"}
        return {"status": request_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))