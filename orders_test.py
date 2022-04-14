import orders
import json

ordersObj = orders.Order()

def test_create():
    # test scenario: place order for a product that doesnt exists
    expected = ordersObj.create('randomProduct','dfee093f-2fa3-43ef-beb6-d4f789c24506',100,5)
    assert expected ==  'cannot place order for non-existent product or customer'

    # test scenario: place order for a user that doesnt exists
    expected = ordersObj.create('9fc6f336-62c1-4cfa-8dda-49e5d71ec504','randomUser',100,5)
    assert expected ==  'cannot place order for non-existent product or customer'

    # test scenario: place order for 0 quantity
    expected = ordersObj.create('9fc6f336-62c1-4cfa-8dda-49e5d71ec504','dfee093f-2fa3-43ef-beb6-d4f789c24506',100,0)
    assert expected ==  'quantity cannot be zero'

    # test scenario: place order for quantity greater than available
    expected = ordersObj.create('9fc6f336-62c1-4cfa-8dda-49e5d71ec504','dfee093f-2fa3-43ef-beb6-d4f789c24506',100,100000)
    assert expected ==  'cannot place order for {} items. Please reduce the quantity'.format(100000)

    # test scenario: place order for an item with less than quantity 5 in inventory
    expected = ordersObj.create('1cc32dec-0a34-4f4b-a936-0b1dc89e5ee3','dfee093f-2fa3-43ef-beb6-d4f789c24506',100,100000)
    assert expected ==  'sorry we cannot place the order at this time'

    #test scenario: successful order 
    expected = ordersObj.create('9fc6f336-62c1-4cfa-8dda-49e5d71ec504','dfee093f-2fa3-43ef-beb6-d4f789c24506',100,1)
    assert expected ==  True 

def test_getAll():
    expected = json.loads(ordersObj.getAll())
    assert len(expected) > 0

def test_getById():
    expected = json.loads(ordersObj.getById('95756322-6d89-4f9a-b849-0305f1da367f'))
    assert expected[0]['id']=='95756322-6d89-4f9a-b849-0305f1da367f'




