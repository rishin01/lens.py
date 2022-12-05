def CreatePostViaDispatcher(var_dict):
	return """
mutation CreatePostViaDispatcher {
  createPostViaDispatcher(request: 
        {
        {kwargs}}
        ) {
    ... on RelayerResult {
      txHash
      txId
    }
    ... on RelayError {
      reason
    }
  }
}

	""".format(var_dict=var_dict)