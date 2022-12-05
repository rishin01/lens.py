def PublicationRevenue(var_dict):
	return """
	query PublicationRevenue {
	  publicationRevenue(request: 
	        {
	        {var_dict}}
	        ) {
	    publication {
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
	    revenue {
	      total {
	        asset {
	          name
	          symbol
	          decimals
	          address
	        }
	        value
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)