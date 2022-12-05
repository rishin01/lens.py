def Broadcast(var_dict):
	Broadcast_query = """ mutation Broadcast {   broadcast(request:
	{         {kwargs}}         ) {     ... on RelayerResult {
	txHash       txId     }     ... on RelayError {       reason     }
	} }  """.format(var_dict=var_dict)