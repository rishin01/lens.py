def createToggleFollowTypedData(var_dict):
	return """
	mutation createToggleFollowTypedData {
	  createToggleFollowTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      domain {
	        name
	        chainId
	        version
	        verifyingContract
	      }
	      types {
	        ToggleFollowWithSig {
	          name
	          type
	        }
	      }
	      value {
	        nonce
	        deadline
	        profileIds
	        enables
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)