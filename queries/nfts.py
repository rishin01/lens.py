def nfts(var_dict):
	return """
	query nfts {
	  nfts(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      contractName
	      contractAddress
	      symbol
	      tokenId
	      owners {
	        amount
	        address
	      }
	      name
	      description
	      contentURI
	      originalContent {
	        uri
	        metaType
	      }
	      chainId
	      collectionName
	      ercType
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	""".format(var_dict=var_dict)