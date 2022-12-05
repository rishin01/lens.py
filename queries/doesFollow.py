def doesFollow(var_dict):
	return """
	query doesFollow {
	  doesFollow(request: 
	        {
	        {var_dict}}
	        ) {
	    followerAddress
	    profileId
	    follows
	  }
	}
	""".format(var_dict=var_dict)