import invoice
import json

invoiceObj = invoice.Invoice()

def test_create():
    # scenario: creating invoice for an order that doesnt exists
    expected = invoiceObj.create('randomOrderId',100,50)
    assert expected == 'cannot create invoice for non-existent order'

    expected = invoiceObj.create('5c556f03-f182-4330-8d2f-70d629a4d73a',100,50)
    assert expected == True

    expected = invoiceObj.create('5c556f03-f182-4330-8d2f-70d629a4d73a',100,100)
    assert expected == True

def test_getAll():

    expected = json.loads(invoiceObj.getAll())
    assert len(expected) > 0
    
def test_getById():
    expected = json.loads(invoiceObj.getById('a6f8eb5b-c252-430f-b1de-134488422277'))
    assert expected[0]['id'] == 'a6f8eb5b-c252-430f-b1de-134488422277'

def test_getAllByStatus():

    # fetch all open invoices
    expected = json.loads(invoiceObj.getAllByStatus('open'))
    assert expected[0]['status'] == 'open'

    # fetch all closed invoices
    expected = json.loads(invoiceObj.getAllByStatus('closed'))
    assert expected[0]['status'] == 'closed'

    # input invalid status
    expected = invoiceObj.getAllByStatus('progress')
    assert expected == 'invalid status'

def test_makeTotalPayment():

    # invoice doesnt exists
    expected = invoiceObj.makeTotalPayment('randomInvoice')
    assert expected == 'invoice doesnt exists'

    expected = invoiceObj.makeTotalPayment('a6f8eb5b-c252-430f-b1de-134488422277')
    assert expected == True

    expected = json.loads(invoiceObj.getById('a6f8eb5b-c252-430f-b1de-134488422277'))
    assert expected[0]['status'] == 'closed'


def test_makePartialPayment():

    expected = invoiceObj.makeTotalPayment('randomInvoice')
    assert expected == 'invoice doesnt exists'

    expected = invoiceObj.makePartialPayment('f89111e7-6416-4de3-85f3-437e1a32a53a',10)
    assert expected == True


    updated_paidAmount = json.loads(invoiceObj.getById('f89111e7-6416-4de3-85f3-437e1a32a53a'))[0]
    assert updated_paidAmount['status'] == 'open'






