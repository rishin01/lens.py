def createSetProfileMetadataTypedData(var_dict):
	return """
	mutation createSetProfileMetadataTypedData {
	  createSetProfileMetadataTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        SetProfileMetadataURIWithSig {
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
	        metadata
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)