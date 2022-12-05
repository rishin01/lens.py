def ProxyAction(var_dict):
	return """
	mutation ProxyAction {
	  proxyAction(request: 
	        {
	        {var_dict}}
	        )
	}
	""".format(var_dict=var_dict)