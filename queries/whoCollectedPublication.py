def whoCollectedPublication(var_dict):
	return """
	query whoCollectedPublication {
	  whoCollectedPublication(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      ...WalletFields
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)