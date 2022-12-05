def addReaction(var_dict):
	return """
	mutation addReaction {
	  addReaction(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)