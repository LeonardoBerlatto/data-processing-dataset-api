import requests

API_URL = "https://data-processing-dataset-api-1.onrender.com"


print("Realizando chamadas para ", API_URL)
print("--------------------")

# GET /sales
print("GET /sales")
response = requests.get(f"{API_URL}/sales")

print("Status code (should be 200):", response.status_code)
print("Response:", response.json())
print("--------------------")

# GET /sales/{invoice_id}

invoice_id = "226-31-3081"

print(f"GET /sales/{invoice_id}")

response = requests.get(f"{API_URL}/sales/{invoice_id}")

print("Status code (should be 200):", response.status_code)
print(f"Response (should be a sale with invoice {invoice_id}):", response.json())
print("--------------------")

# POST /sales

print("POST /sales")

new_sale = {
    "branch": "A",
    "city": "Yangon",
    "customer_type": "Member",
    "gender": "Female",
    "product_line": "Health and beauty",
    "unit_price": 74.69,
    "quantity": 7,
    "tax": 26.15,
    "total": 548.95,
    "date": "1/5/2019",
    "time": "13:08",
    "payment": "Ewallet",
    "cogs": 522.83,
    "gross_margin_percentage": 4,
    "gross_income": 26.15,
    "rating": 9.1
}

response = requests.post(f"{API_URL}/sales", json=new_sale)

print("Status code (should be 201):", response.status_code)
print("Response:", response.json())
print("--------------------")

# PUT /sales/{invoice_id}

print(f"PUT /sales/{invoice_id}")

updated_sale = {
    "branch": "B",
    "city": "Yangon",
    "customer_type": "Member",
    "gender": "Female",
    "product_line": "Health and beauty",
    "unit_price": 74.69,
    "quantity": 7,
    "tax": 26.15,
    "total": 548.95,
    "date": "1/5/2019",
    "time": "13:08",
    "payment": "Ewallet",
    "cogs": 522.83,
    "gross_margin_percentage": 4,
    "gross_income": 26.15,
    "rating": 9.1
}

response = requests.put(f"{API_URL}/sales/{invoice_id}", json=updated_sale)

print("Status code (should be 200):", response.status_code)
print("Response:", response.json())
print("--------------------")

# DELETE /sales/{invoice_id}

print(f"DELETE /sales/{invoice_id}")

response = requests.delete(f"{API_URL}/sales/{invoice_id}")

print("Status code (should be 204):", response.status_code)

