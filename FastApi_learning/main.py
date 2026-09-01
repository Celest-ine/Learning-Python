from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

booking_applications: list[dict] = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890",
        "date": "2026-08-31",
        "time": "10:00 AM",
        "car_model": "Toyota Camry",
        "service_type": "Oil change",
        "status": "pending",
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "phone": "098-765-4321",
        "date": "2026-09-01",
        "time": "2:00 PM",
        "car_model": "Honda Accord",
        "service_type": "Brake service",
        "status": "pending",
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False) #create a route for the root endpoint
@app.get("/bookings", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>Book a Service<h1>" #return a simple HTML response with a headline

#@app.get("/bookings") #Create a route for booking endpoints
#def create_booking():
    #booking_id = len(booking_applications) + 1
    #booking["id"] = booking_id
    #booking["status"] = "pending"
    #booking_applications.append(booking)
    #return {"message": "Booking created successfully", "booking": booking}

@app.get("/api/bookings")
def get_bookings():
    return booking_applications