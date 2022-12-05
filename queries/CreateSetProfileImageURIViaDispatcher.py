def CreateSetProfileImageURIViaDispatcher(var_dict):
	return """
	mutation CreateSetProfileImageURIViaDispatcher {
	  createSetProfileImageURIViaDispatcher(request: 
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