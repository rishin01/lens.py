def following(var_dict):
	return """
	query following {
	  following(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      profile {
	        ...ProfileFields
	      }
	      totalAmountOfTimesFollowing
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)