def createSetFollowNFTUriTypedData(var_dict):
	return """
	mutation createSetFollowNFTUriTypedData {
	  createSetFollowNFTUriTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        SetFollowNFTURIWithSig {
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
	        profileId
	        deadline
	        followNFTURI
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)