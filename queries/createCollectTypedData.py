def createCollectTypedData(var_dict):
	return """
	mutation createCollectTypedData {
	  createCollectTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        CollectWithSig {
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
	        pubId
	        data
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)