def verify(var_dict):
	return """
	query verify {
	  verify(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)