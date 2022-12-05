def hidePublication(var_dict):
	return """
	mutation hidePublication {
	  hidePublication(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)