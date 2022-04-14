import customer
import json

customerObj = customer.Customer()

def test_customer_create():
    expected = customerObj.create('test_user','CA',10,'test@test')
    assert expected == True

def test_customer_getById_nonExistentUser():
    expected =  customerObj.getById('someRandomId')
    assert expected == 'customer doesnt exists'

def test_customer_getById():
    expected =  customerObj.getById('dfee093f-2fa3-43ef-beb6-d4f789c24506')
    assert expected == '[{"id":"dfee093f-2fa3-43ef-beb6-d4f789c24506","name":"guru","state":"CA","tax":10,"email":"guru@gmail.com"}]'


def test_customer_getByName_nonExistentUser():
    expected =  customerObj.getByName('someRandomName')
    assert expected == 'customer doesnt exists'

def test_customer_getByName():
    expected =  customerObj.getByName('test_user')
    expected = json.loads(expected)
    assert expected[0]['name'] == 'test_user'