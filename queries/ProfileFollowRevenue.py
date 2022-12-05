def ProfileFollowRevenue(var_dict):
	return """
	query ProfileFollowRevenue {
	  profileFollowRevenue(request: 
	        {
	        {var_dict}}
	        ) {
	    revenues {
	      total {
	        asset {
	          name
	          symbol
	          decimals
	          address
	        }
	        value
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)