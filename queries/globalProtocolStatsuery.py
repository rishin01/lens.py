def globalProtocolStatsuery(var_dict):
	return """
	query globalProtocolStatsuery globalProtocolStats(
	        {
	        {var_dict}}
	        : GlobalProtocolStatsRequest) {
	  globalProtocolStats(request: 
	        {
	        {var_dict}}
	        ) {
	    totalProfiles
	    totalBurntProfiles
	    totalPosts
	    totalMirrors
	    totalComments
	    totalCollects
	    totalFollows
	    totalRevenue {
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
	""".format(var_dict=var_dict)