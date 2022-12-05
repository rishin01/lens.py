def profiles(var_dict):
	return """
	query profiles {
	  profiles(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      ...ProfileFields
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)