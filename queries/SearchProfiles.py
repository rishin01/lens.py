def SearchProfiles(var_dict):
	return """
	query SearchProfiles {
	  search(request: 
	        {
	        {var_dict}}
	        ) {
	    ... on ProfileSearchResult {
	      __typename
	      items {
	        ... on Profile {
	          ...ProfileFields
	        }
	      }
	      pageInfo {
	        ...CommonPaginatedResultInfoFields
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)