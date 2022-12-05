def followers(var_dict):
	return """
	query followers {
	  followers(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      wallet {
	        ...WalletFields
	      }
	      totalAmountOfTimesFollowed
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)