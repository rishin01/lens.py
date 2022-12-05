def createSetFollowModuleTypedData(var_dict):
	return """
	mutation createSetFollowModuleTypedData {
	  createSetFollowModuleTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        SetFollowModuleWithSig {
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
	        followModule
	        followModuleInitData
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)