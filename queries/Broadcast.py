def Broadcast(var_dict):
	return """
	mutation Broadcast {
	  broadcast(request: 
	        {
	        {var_dict}}
	        ) {
	    ... on RelayerResult {
	      txHash
	      txId
	    }
	    ... on RelayError {
	      reason
	    }
	  }
	}
	""".format(var_dict=var_dict)