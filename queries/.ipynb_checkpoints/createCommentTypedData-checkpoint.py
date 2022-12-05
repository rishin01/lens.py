def createCommentTypedData(var_dict):
	return"""
	mutation createCommentTypedData {   createCommentTypedData(request:
	{         {kwargs}}         ) {     id     expiresAt     typedData {
	types {         CommentWithSig {           name           type
	}       }       domain {         name         chainId         version
	verifyingContract       }       value {         nonce
	deadline         profileId         profileIdPointed
	pubIdPointed         contentURI         collectModule
	collectModuleInitData         referenceModule
	referenceModuleInitData         referenceModuleData       }     }   }
	}
	""".format(var_dict=var_dict)