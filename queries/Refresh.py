def Refresh(var_dict):
	return """
	mutation Refresh {
	  refresh(request: 
	        {
	        {var_dict}}
	        ) {
	    accessToken
	    refreshToken
	  }
	}
	""".format(var_dict=var_dict)