def exploreProfiles(var_dict):
	return """
	query exploreProfiles {
	  exploreProfiles(request: 
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