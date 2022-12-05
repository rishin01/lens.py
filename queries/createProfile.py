def createProfile(var_dict):
	return """
	mutation createProfile {
	  createProfile(request: 
	        {
	        {var_dict}}
	        ) {
	    ... on RelayerResult {
	      txHash
	    }
	    ... on RelayError {
	      reason
	    }
	    __typename
	  }
	}
	""".format(var_dict=var_dict)