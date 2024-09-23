# data-processing-dataset-api

## Description
This project is a simple API that allows you to create, read, update and delete data from sales. The dataset is stored in a file called `sales.csv`.

## Requirements
- Python 3.9 or higher

## Installation
1. Clone this repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the API with `python main.py`

## Endpoints
- `GET /sales`: Returns all sales
- `GET /sales/{invoice_id}`: Returns a sale by its invoice id
- `POST /sales`: Creates a new sale
- `PUT /sales/{invoice_id}`: Updates a sale by its invoice id
- `DELETE /sales/{invoice_id}`: Deletes a sale by its invoice id

All endpoints are public available at https://data-processing-dataset-api-1.onrender.com

## Docs
- [Postman Collection](/resources/docs/Trabalho_2.postman_collection.json)
- [Swagger UI](https://data-processing-dataset-api-1.onrender.com/docs)

## Script 
This project also contains a script to test the deployed API. You can run it with `python ./resources/script.py`.

Change the `API_URL` variable to test the API locally.
Change the invoice_id to test the `GET /sales/{invoice_id}`, `PUT /sales/{invoice_id}` and `DELETE /sales/{invoice_id}` endpoints.