
from  cryptounifier_python_sdk import MerchantAPI, WalletAPI

# WalletAPI
client = WalletAPI('crB5XNkCdvUjjnWp', 'v3/3AEQWLOzxUhvimu8X8kS5L5DCkQ6c4iVOD62yK0g=', 'btc')

#balance = client.getBalance()
balance = client.validateAddresses(["ubc"])
print(balance)

# depositAddresses = client.getDepositAddresses()
# print(depositAddresses)

# MerchantAPI
# client_MerchantAPI = MerchantAPI('', '')

# # invoice = client_MerchantAPI.createInvoice(['btc', 'bch', 'eth'])
# # print(invoice)
# invoiceInfo = client_MerchantAPI.invoiceInfo("")
# print(invoiceInfo)