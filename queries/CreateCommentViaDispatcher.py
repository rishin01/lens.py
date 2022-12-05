def CreateCommentViaDispatcher(var_dict):
	return """
	mutation CreateCommentViaDispatcher {
	  createCommentViaDispatcher(request: 
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