def profile(var_dict):
	return """
	query profile {
	  profile(request: 
	        {
	        {var_dict}}
	        ) {
	    ...ProfileFields
	  }
	}
	""".format(var_dict=var_dict)