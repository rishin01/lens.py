def createSetProfileImageURITypedData(var_dict):
	return """
	mutation createSetProfileImageURITypedData {
	  createSetProfileImageURITypedData(request: 
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
	        SetProfileImageURIWithSig {
	          name
	          type
	        }
	      }
	      value {
	        nonce
	        deadline
	        imageURI
	        profileId
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)