def followerNftOwnedTokenIds(var_dict):
	return """
	query followerNftOwnedTokenIds {
	  followerNftOwnedTokenIds(request: 
	        {
	        {var_dict}}
	        ) {
	    followerNftAddress
	    tokensIds
	  }
	}
	""".format(var_dict=var_dict)