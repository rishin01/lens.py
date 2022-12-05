def removeReaction(var_dict):
	return """
	mutation removeReaction {
	  removeReaction(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)