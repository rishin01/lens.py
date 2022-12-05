def defaultProfile(var_dict):
	return """
	query defaultProfile {
	  defaultProfile(request: 
	        {
	        {var_dict}}
	        ) {
	    ...ProfileFields
	  }
	}
	""".format(var_dict=var_dict)