import uuid
import pandas as pd


class Warehouse:

  def create(self, name,capactiy):
    try:
        id = uuid.uuid4()
        df = pd.read_csv('./data/warehouse.csv')
        df = df.append({'id':id,'name':name,'capacity':capactiy},ignore_index=True)
        df.to_csv('./data/warehouse.csv')
        return True

    except Exception as e:
        print("An exception occurred while creating Warehouse",e)      
        return e  

  def getByName(self,name):
    try:
      df = pd.read_csv('./data/warehouse.csv',usecols = ['id','name','capacity'])
      warehouse = df[df['name'] == name]

      return 'warehouse doesnt exists'  if warehouse.empty  else df[df['name'] == name].to_json(orient ='records')
    except Exception as e:
        print("An exception occurred while  warehouse getByName",e)      
        return e  

  def getAll(self):
    try:
      df = pd.read_csv('./data/warehouse.csv',usecols = ['id','name','capacity'])
      return df.to_json(orient ='records')
    except Exception as e:
        print("An exception occurred while  warehouse getAll",e)      
        return e  

  def decrementCapacity(self,wareHouseName):
    try:
        name = wareHouseName
        warehouse = self.getByName(name)

        if warehouse == 'warehouse doesnt exists':
          return 'Can not add product to a non existent warehouse'

        df = pd.read_csv('./data/warehouse.csv')
        df.loc[df['name'].isin([name]), 'capacity'] -= 1
        df.to_csv('./data/warehouse.csv')

        return 'product added to {}'.format(name)

    except Exception as e:
        print("An exception occurred while addProduct Warehouse",e)      
        return e  

  def incrementCapacity(self,wareHouseName):
    try:
        name = wareHouseName
        warehouse = self.getByName(name)

        if warehouse == 'warehouse doesnt exists':
          return 'Can not remove product from non existent warehouse'

        df = pd.read_csv('./data/warehouse.csv')
        df.loc[df['name'].isin([name]), 'capacity'] += 1
        df.to_csv('./data/warehouse.csv')

        return 'product removed from {}'.format(name)

    except Exception as e:
        print("An exception occurred while addProduct Warehouse",e)      
        return e  


def main():
    warehouse = Warehouse()
    warehouse.create('WH3',350)

    warehouseDetails = warehouse.getByName('WH3')
    print(warehouseDetails)

    allWarehouses = warehouse.getAll()
    print(allWarehouses)
    print(warehouse.incrementCapacity("WH3"))

    print(warehouse.decrementCapacity("WH4"))



main()


