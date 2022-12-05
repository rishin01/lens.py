def CreateMirrorViaDispatcher(var_dict):
	return """
	mutation CreateMirrorViaDispatcher {
	createMirrorViaDispatcher(request:          {         {kwargs}}
	) {     ... on RelayerResult {       txHash       txId     }     ...
	on RelayError {       reason     }   } }
	""".format(var_dict=var_dict)