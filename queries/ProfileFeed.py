def ProfileFeed(var_dict):
	return """
	query ProfileFeed {
	  feed(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      root {
	        __typename
	        ... on Post {
	          ...PostFields
	        }
	        ... on Comment {
	          ...CommentFields
	        }
	      }
	      electedMirror {
	        mirrorId
	        profile {
	          id
	          handle
	        }
	        timestamp
	      }
	      mirrors {
	        profile {
	          id
	          handle
	        }
	        timestamp
	      }
	      collects {
	        profile {
	          id
	          handle
	        }
	        timestamp
	      }
	      reactions {
	        profile {
	          id
	          handle
	        }
	        reaction
	        timestamp
	      }
	      comments {
	        ...CommentFields
	      }
	    }
	    pageInfo {
	      prev
	      next
	      totalCount
	    }
	  }
	}
	""".format(var_dict=var_dict)