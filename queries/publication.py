def publication(var_dict):
	return """
	query publication {
	  publication(request: 
	        {
	        {var_dict}}
	        ) {
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
	}
	""".format(var_dict=var_dict)