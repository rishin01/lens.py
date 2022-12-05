def ExplorePublications(var_dict):
	return """
	query ExplorePublications {
	  explorePublications(request: 
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
	      ... on Mirror {
	        ...MirrorFields
	      }
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)