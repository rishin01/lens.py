def createPostTypedData(var_dict):
	return """
	mutation createPostTypedData {   createPostTypedData(request:
	{         {kwargs}}         ) {     id     expiresAt     typedData {
	types {         PostWithSig {           name           type         }
	}       domain {         name         chainId         version
	verifyingContract       }       value {         nonce
	deadline         profileId         contentURI         collectModule
	collectModuleInitData         referenceModule
	referenceModuleInitData       }     }   } }
	""".format(var_dict=var_dict)