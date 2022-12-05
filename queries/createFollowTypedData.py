def createFollowTypedData(var_dict):
	return """
	mutation createFollowTypedData {
	  createFollowTypedData(request: 
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
	        FollowWithSig {
	          name
	          type
	        }
	      }
	      value {
	        nonce
	        deadline
	        profileIds
	        datas
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)