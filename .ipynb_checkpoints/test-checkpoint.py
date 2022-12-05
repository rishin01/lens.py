from GraphQLClient import client
from queries import *
from gql import gql
import web3

client = client()
# print(client.client.schema)
wallet_private_address = '9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab'

wallet_public_address = '0xC711C6493cBf0CC4b468c58B964d3c4B6bA7507D'
txt = "\nunknown wants you to sign in with your Ethereum account:\n0xC711C6493cBf0CC4b468c58B964d3c4B6bA7507D\n\nSign in with ethereum to lens\n\nURI: unknown\nVersion: 1\nChain ID: 80001\nNonce: 3c8afc0488a285e1\nIssued At: 2022-11-13T03:12:54.543Z\n "

result = web3.eth.sign(
    wallet_private_address,
    text = txt
)
print(result)

# chAllenge = gql(Challenge("address:"+'"'+wallet_public_address+'"'))
# print("mutation:"+"'"+chAllenge+"'")
# x = client.execute_query("query:"+"'"+chAllenge+"'")

# query = gql(
#     """
#     query ping {
#     ping
#     }
#     """
# )

aUthenticate = gql(authenticate("address:"+'"'+wallet_public_address+'",'+'signature:'+'"'+result+'"'))
x = client.execute_query(aUthenticate)
print(x)
# create_profile = createProfile("handle:'Tobias Sarcasm',profilePictureUri: null,followNFTURI: null,followModule: null")




# x = client.execute_query(create_profile)
# print(x)