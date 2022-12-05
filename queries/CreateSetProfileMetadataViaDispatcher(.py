def CreateSetProfileMetadataViaDispatcher((var_dict):
	return """
	mutation CreateSetProfileMetadataViaDispatcher(
	 utation CreateSetProfileMetadataViaDispatcher(
	  
	        {
	        {var_dict}}
	        : CreatePublicSetProfileMetadataURIRequest!
	) {
	  createSetProfileMetadataViaDispatcher(request: 
	        {
	        {var_dict}}
	        ) {
	    ... on RelayerResult {
	      txHash
	      txId
	    }
	    ... on RelayError {
	      reason
	    }
	  }
	}
	""".format(var_dict=var_dict)