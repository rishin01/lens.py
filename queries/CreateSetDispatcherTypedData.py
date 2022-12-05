def CreateSetDispatcherTypedData(var_dict):
	return """
	mutation CreateSetDispatcherTypedData {
	  createSetDispatcherTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        SetDispatcherWithSig {
	          name
	          type
	        }
	      }
	      domain {
	        name
	        chainId
	        version
	        verifyingContract
	      }
	      value {
	        nonce
	        deadline
	        profileId
	        dispatcher
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)