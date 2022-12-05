def CreatePostViaDispatcher(var_dict):
	return """
	mutation CreatePostViaDispatcher {
	  createPostViaDispatcher(request: 
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