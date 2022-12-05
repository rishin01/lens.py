def MutualFollowersProfiles(var_dict):
	return """
	query MutualFollowersProfiles {
	  mutualFollowersProfiles(request: 
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