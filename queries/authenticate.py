def authenticate(var_dict):
	return """
	mutation Authenticate {
	  authenticate(request: 
	        {
	        {var_dict}}
	        ) {
	    accessToken
	    refreshToken
	  }
	}
	""".format(var_dict=var_dict)