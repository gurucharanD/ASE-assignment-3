import uuid
import pandas as pd


class Customer:

  def create(self, name,state,tax,email):
    id = uuid.uuid4()
    df = pd.read_csv('./data/customers.csv')
    df = df.append({'id':id,'name':name,'state':state,'tax':tax,'email':email},ignore_index=True)
    df.to_csv('./data/customers.csv')
    return True

  def getById(self,id):
    df = pd.read_csv('./data/customers.csv',usecols = ['id','name','state','tax','email'])
    customer = df[df['id'] == id]

    return 'customer doesnt exists'  if customer.empty  else customer.to_json(orient ='records')

  def getByName(self,name):
    df = pd.read_csv('./data/customers.csv',usecols = ['id','name','state','tax','email'])
    customer = df[df['name'] == name]

    return 'customer doesnt exists'  if customer.empty  else df[df['name'] == name].to_json(orient ='records')

  def getAll(self):
    df = pd.read_csv('./data/customers.csv',usecols = ['id','name','state','tax','email'])
    return df.to_json(orient ='records')



def main():

    customer = Customer()
    customer.create('guru','CA',10,'guru@gmail.com')

    customerDetails = customer.getByName('customer1')
    print(customerDetails)

    allCustomers = customer.getAll()
    print(allCustomers)

main()


