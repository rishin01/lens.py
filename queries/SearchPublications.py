def SearchPublications(var_dict):
	return """
	query SearchPublications {
	  search(request: 
	        {
	        {var_dict}}
	        ) {
	    ... on PublicationSearchResult {
	      __typename
	      items {
	        __typename
	        ... on Comment {
	          ...CommentFields
	        }
	        ... on Post {
	          ...PostFields
	        }
	      }
	      pageInfo {
	        ...CommonPaginatedResultInfoFields
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)