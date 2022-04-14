
import pandas as pd
import uuid
import orders 
import json

orderObj = orders.Order()

class Invoice:

    def create(self,orderid,totalAmount,paidAmount):
        try:
            order  = orderObj.getById(orderid)
            if order == 'order doesnt exists':
                return 'cannot create invoice for non-existent order'

            order = json.loads(order)[0]
            id = uuid.uuid4()

            if totalAmount == paidAmount:
                status = 'closed'
            else:
                 status = 'open'
            
            df = pd.read_csv('./data/invoices.csv')
            df = df.append({'id':id,'orderId':orderid,'totalAmount':totalAmount,'paidAmount':paidAmount,'status':status},ignore_index=True)
            df.to_csv('./data/invoices.csv')

            return True
        except Exception as e:
            print("An exception occurred while Invoice create",e)      
            return e
    
    def getAll(self):
        try:
            df = pd.read_csv('./data/invoices.csv',usecols = ['id','orderId','totalAmount','paidAmount','status'])
            return df.to_json(orient ='records')
        except Exception as e:
            print("An exception occurred while  Invoice getAll",e)      
            return e  

    def getById(self,invoiceId):
        try:
            df = pd.read_csv('./data/invoices.csv',usecols = ['id','orderId','totalAmount','paidAmount','status'])
            invoice = df[df['id'] == invoiceId]

            return 'invoice doesnt exists'  if invoice.empty  else invoice.to_json(orient ='records')
        except Exception as e:
            print("An exception occurred while  invoice getById",e)      
            return e  

    def getAllByStatus(self,status):

        if status != "open" and status!= "closed":
            return 'invalid status'

        try:
            df = pd.read_csv('./data/invoices.csv',usecols = ['id','orderId','totalAmount','paidAmount','status'])
            invoices = df[df['status'] == status]

            return 'no invoices in {} status '.format(status)  if invoices.empty  else invoices.to_json(orient ='records')
        except Exception as e:
            print("An exception occurred while  invoice getAllByStatus",e)      
            return e  

    def makeTotalPayment(self,invoiceId):
        try:
            invoice = self.getById(invoiceId)
            
            if invoice == 'invoice doesnt exists':
                return invoice

            invoice = json.loads(invoice)[0]

            invoice['paidAmount'] = invoice['totalAmount']
            invoice['status'] = 'closed'

            df = pd.read_csv('./data/invoices.csv')
            df.drop(invoice,True)
            df = df.append(invoice,ignore_index=True)
            df.to_csv('./data/invoices.csv')

            return True
        except Exception as e:
            return e

    def makePartialPayment(self,invoiceId,amount):
        try:
            invoice = self.getById(invoiceId)
            
            if invoice == 'invoice doesnt exists':
                return invoice

            invoice = json.loads(invoice)[0]

            invoice['paidAmount'] = invoice['paidAmount']+amount

            df = pd.read_csv('./data/invoices.csv')
            df.drop(invoice,True)
            df = df.append(invoice,ignore_index=True)
            df.to_csv('./data/invoices.csv')

            return True
        except Exception as e:
            return e       


def main():
    invoice = Invoice()

    # print(invoice.create('05acdbec-bae5-4bc9-a530-18f4aaca0059',1000,200))
    # print(invoice.getAll())
    # print(invoice.getById('99350f7a-15b4-4edd-9ca4-cff1c1f88c92'))
    # print(invoice.getById('123'))
    # print(invoice.getAllByStatus('open'))
    # print(invoice.getAllByStatus('closed'))
    # print(invoice.makeTotalPayment('39701fbd-f262-4aaa-8c71-7bf531a4fbef'))

    return

main()