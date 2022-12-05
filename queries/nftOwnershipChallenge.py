def nftOwnershipChallenge(var_dict):
	return """
	query nftOwnershipChallenge {
	  nftOwnershipChallenge(request: 
	        {
	        {var_dict}}
	        ) {
	    id
	    text
	  }
	}
	""".format(var_dict=var_dict)