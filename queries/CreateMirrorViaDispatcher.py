def CreateMirrorViaDispatcher(var_dict):
	return """
	mutation CreateMirrorViaDispatcher {
	  createMirrorViaDispatcher(request: 
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