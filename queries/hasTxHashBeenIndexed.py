def hasTxHashBeenIndexed(var_dict):
	return """
	query hasTxHashBeenIndexed {
	  hasTxHashBeenIndexed(request: 
	        {
	        {var_dict}}
	        ) {
	    __typename
	    ... on TransactionIndexedResult {
	      indexed
	      txReceipt {
	        ...TxReceiptFields
	      }
	      metadataStatus {
	        status
	        reason
	      }
	    }
	    ... on TransactionError {
	      reason
	      txReceipt {
	        ...TxReceiptFields
	      }
	    }
	  }
	}
	""".format(var_dict=var_dict)