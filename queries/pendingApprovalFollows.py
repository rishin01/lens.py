def pendingApprovalFollows(var_dict):
	return """
	query pendingApprovalFollows {
	  pendingApprovalFollows(request: 
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