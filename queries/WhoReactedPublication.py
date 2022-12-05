def WhoReactedPublication(var_dict):
	return """
	query WhoReactedPublication {
	  whoReactedPublication(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      reactionId
	      reaction
	      reactionAt
	      profile {
	        ...ProfileFields
	      }
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)