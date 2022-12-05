def generateModuleCurrencyApprovalData(var_dict):
	return """
	query generateModuleCurrencyApprovalData {
	  generateModuleCurrencyApprovalData(request: 
	        {
	        {var_dict}}
	        ) {
	    to
	    from
	    data
	  }
	}
	""".format(var_dict=var_dict)