def createMirrorTypedData(var_dict):
	return """
	mutation createMirrorTypedData {
	  createMirrorTypedData(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    expiresAt
	    typedData {
	      types {
	        MirrorWithSig {
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
	        profileIdPointed
	        pubIdPointed
	        referenceModuleData
	        referenceModule
	        referenceModuleInitData
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)