import uuid
import pandas as pd
import warehouse  

warehouseObj = warehouse.Warehouse()

class Product:

  def create(self,name,price,quantity,warehouse):
    try:
        id = uuid.uuid4()
        df = pd.read_csv('./data/products.csv')
        df = df.append({'id':id,'name':name,'price':price,'quantity':quantity,'warehouse':warehouse},ignore_index=True)
        df.to_csv('./data/products.csv')
        warehouseObj.decrementCapacity(warehouse)
        return 'product created'

    except Exception as e:
        print("An exception occurred while creating product",e)      
        return e  

  def getByName(self,name):
    try:
      df = pd.read_csv('./data/products.csv',usecols = ['id','name','price','quantity','warehouse'])
      product = df[df['name'] == name]

      return 'product doesnt exists'  if product.empty  else df[df['name'] == name].to_json(orient ='records')
    except Exception as e:
        print("An exception occurred while  product getByName",e)      
        return e  
  
  def getById(self,id):
    try:
      df = pd.read_csv('./data/products.csv',usecols = ['id','name','price','quantity','warehouse'])
      product = df[df['id'] == id]

      return 'product doesnt exists'  if product.empty  else product.to_json(orient ='records')
    except Exception as e:
        print("An exception occurred while  product getById",e)      
        return e  

  def getAll(self):
    try:
      df = pd.read_csv('./data/products.csv',usecols = ['id','name','price','quantity','warehouse'])
      return df.to_json(orient ='records')
    except Exception as e:
        print("An exception occurred while  product getAll",e)      
        return e  




def main():
    product = Product()
    product.create('television','120$',100,'WH3')

    productDetails = product.getByName('television')
    print(productDetails)

    allProducts = product.getAll()
    print(allProducts)



main()


