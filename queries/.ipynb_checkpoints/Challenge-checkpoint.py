def Challenge(var_dict):
	return """
	query Challenge {
	  challenge(request: 
	        {
	        {kwargs}}
	        ) {
	    text
	  }
	}
		""".format(var_dict=var_dict)