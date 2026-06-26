#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def get_contract(id):
    contract = [contract["contract_information"] for contract in contracts if contract["id"] == id ]
    if len(contract) == 0:
        return make_response(f'Contract not found.',404)
    else:
        return make_response(f'{contract[0]}',200)

@app.route('/customer/<string:customer_name>')
def get_customer(customer_name):
    customer = next((customer for customer in customers if customer == customer_name),None)
    print(customer)
    if customer == None:
        return make_response(f'Customer not found.',404)
    else:
        return make_response(f'',204)
        
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
