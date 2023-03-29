Bank Details API using FastAPI

This project provides a simple API that allows users to obtain details of banks by their IFSC codes, branch names, and more. It's built using the FastAPI framework and is designed to be fast, efficient, and easy to use.

Installation
To install the project, follow these steps:

Clone the repository to your local machine using git clone https://github.com/shailender-shrma/bank-fastapi-app.git

Navigate to the project directory using cd bank-fastapi-app

Create a new virtual environment using python3 -m venv venv

Activate the virtual environment using source venv/bin/activate

Install the required packages using pip install -r requirements.txt

Start the server using uvicorn main:app --reload

Usage
To use the API, make a GET request to the /banks/{branch} endpoint, where {branch} is the branch of the bank you want to obtain details for. For example, to obtain details of a bank with the branch code RTGS-HO, you would make a GET request to http://127.0.0.1:8000/bank-list/RTGS-HO.


Documentation
This API comes with built-in documentation, provided by FastAPI's Swagger UI. To access the documentation, simply navigate to http://localhost:8000/docs in your web browser.

