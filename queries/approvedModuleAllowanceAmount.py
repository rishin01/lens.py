def approvedModuleAllowanceAmount(var_dict):
	return """
	query approvedModuleAllowanceAmount {
	  approvedModuleAllowanceAmount(request: 
	        {
	        {var_dict}}
	        ) {
	    currency
	    module
	    contractAddress
	    allowance
	  }
	}
	""".format(var_dict=var_dict)