# id,productid,customerid,shippingcharge,amount
import uuid
import pandas as pd
import customer
import products
import json

from warehouse import Warehouse

customerObj = customer.Customer()
productObj = products.Product()
warehouseObj = Warehouse()

class Order:

    def create(self,productId,customerId,shippingCharge,quantity):
        try:
            product = productObj.getById(productId)
            customer = customerObj.getById(customerId)

            if product == 'product doesnt exists' or customer == 'customer doesnt exists':
                return 'cannot place order for non-existent product or customer'

            product = json.loads(product)[0]
            customer = json.loads(customer)[0]

            if quantity == 0:
                return 'quantity cannot be zero'

            if product['quantity'] <= 5:
                 return 'sorry we cannot place the order at this time'

            if quantity > product['quantity']:
                return 'cannot place order for {} items. Please reduce the quantity'.format(quantity)

            amount = product['price']*quantity

            id = uuid.uuid4()
            df = pd.read_csv('./data/orders.csv')
            df = df.append({'id':id,'productId':productId,'customerId':customerId,'shippingCharge':shippingCharge,'quantity':quantity,'amount':amount},ignore_index=True)
            df.to_csv('./data/orders.csv')

            warehouseObj.incrementCapacity(product['warehouse'])

            return True
        except Exception as e:
            print("An exception occurred while Order create",e)      
            return e
    
    def getAll(self):
        try:
            df = pd.read_csv('./data/orders.csv',usecols = ['id','productId','customerId','shippingCharge','amount'])
            return df.to_json(orient ='records')
        except Exception as e:
            print("An exception occurred while Order getAll",e)      
            return e  

    def getById(self,id):
        try:
            df = pd.read_csv('./data/orders.csv',usecols = ['id','productid','customerid','shippingcharge','amount'])
            order = df[df['id'] == id]

            return 'order doesnt exists'  if order.empty  else order.to_json(orient ='records')
        except Exception as e:
            print("An exception occurred while  order getById",e)      
            return e  



def main():
    order = Order()
    # print(order.create('57c5de66-0793-4f52-bbe5-b59e88845c45','2969443c-2b1b-4f4a-b245-ed3a2af1c702',1030,20))
    # print(order.getAll())
    return

main()