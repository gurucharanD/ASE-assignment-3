import products
import json

productsObj = products.Product()

def test_create():
    expected = productsObj.create('test_product',100,200,'test_warehouse')
    assert expected == 'product created'

def test_getByName():
    expected = productsObj.getByName('test_product')
    expected = json.loads(expected)
    assert expected[0]['name'] == 'test_product'

    # testing scenario => for a non existant product 
    expected = productsObj.getByName('randomProduct')
    assert expected == 'product doesnt exists'

def test_getById():
    expected = productsObj.getById('fc317654-08e1-488d-b65d-7fdfb826f0e9')
    expected = json.loads(expected)
    assert expected[0]['id'] == 'fc317654-08e1-488d-b65d-7fdfb826f0e9'
    assert expected[0]['name'] == 'test_product'

    # testing scenario => for a non existant product 
    expected = productsObj.getByName('randomProduct')
    assert expected == 'product doesnt exists'

def test_getAll():
    expected = productsObj.getAll()
    expected = json.loads(expected)
    assert len(expected) > 0



