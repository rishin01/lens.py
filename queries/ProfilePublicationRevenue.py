def ProfilePublicationRevenue(var_dict):
	return """
	query ProfilePublicationRevenue {
	  profilePublicationRevenue(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
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
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)