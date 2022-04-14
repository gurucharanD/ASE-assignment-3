import warehouse
import json

warehouseObj = warehouse.Warehouse()

def test_warehouse_create():
    expected = warehouseObj.create('test_warehouse',100)
    assert expected == True

def test_warehouse_getByName_nonExistentWarehouse():
    expected = warehouseObj.getByName('randomwarehouse')
    assert expected == 'warehouse doesnt exists'

def test_warehouse_getByName():
    expected = warehouseObj.getByName('test_warehouse')
    expected = json.loads(expected)
    assert expected[0]['name'] == 'test_warehouse'

def test_warehouse_getAll():
    expected = warehouseObj.getAll()
    expected = json.loads(expected)
    assert len(expected) > 0

def test_decrementCapacity_nonExistentWarehouse():
    expected = warehouseObj.decrementCapacity('randomwarehouse')
    assert expected == 'Can not add product to a non existent warehouse'

def test_decrementCapacity():
    previous_capacity = json.loads(warehouseObj.getByName('test_warehouse'))[0]['capacity']
    expected = warehouseObj.decrementCapacity('test_warehouse')
    updated_capacity = json.loads(warehouseObj.getByName('test_warehouse'))[0]['capacity']

    assert expected == 'product added to test_warehouse'
    assert previous_capacity == updated_capacity+1

def test_incrementCapacity_nonExistentWarehouse():
    expected = warehouseObj.incrementCapacity('randomwarehouse')
    assert expected == 'Can not remove product from non existent warehouse'

def test_incrementCapacity():
    previous_capacity = json.loads(warehouseObj.getByName('test_warehouse'))[0]['capacity']
    expected = warehouseObj.incrementCapacity('test_warehouse')
    updated_capacity = json.loads(warehouseObj.getByName('test_warehouse'))[0]['capacity']

    assert expected == 'product removed from test_warehouse'
    assert previous_capacity == updated_capacity-1






