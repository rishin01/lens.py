def createSetDefaultProfileTypedData(var_dict):
	return """
	mutation createSetDefaultProfileTypedData {
	  createSetDefaultProfileTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        SetDefaultProfileWithSig {
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
	        wallet
	        profileId
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)