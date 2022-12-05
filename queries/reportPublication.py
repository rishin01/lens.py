def reportPublication(var_dict):
	return """
	mutation reportPublication {
	  reportPublication(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)