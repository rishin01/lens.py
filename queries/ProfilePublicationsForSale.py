def ProfilePublicationsForSale(var_dict):
	return """
	query ProfilePublicationsForSale {
	  profilePublicationsForSale(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      __typename
	      ... on Post {
	        ...PostFields
	      }
	      ... on Comment {
	        ...CommentFields
	      }
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)