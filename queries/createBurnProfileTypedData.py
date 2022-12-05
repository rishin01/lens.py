def createBurnProfileTypedData(var_dict):
	return """
	mutation createBurnProfileTypedData {
	  createBurnProfileTypedData(request: 
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
	        BurnWithSig {
	          name
	          type
	        }
	      }
	      value {
	        nonce
	        deadline
	        tokenId
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)