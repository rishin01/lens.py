def Challenge(var_dict):
	return """
	query Challenge {
	  challenge(request: 
	        {
	        {var_dict}}
	        ) {
	    text
	  }
	}
	""".format(var_dict=var_dict)