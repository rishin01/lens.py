def notifications(var_dict):
	return """
	query notifications {
	  notifications(request: 
	        {
	        {var_dict}}
	        ) {
	    items {
	      ... on NewFollowerNotification {
	        notificationId
	        ...NewFollowerNotificationFields
	      }
	
	      ... on NewMirrorNotification {
	        notificationId
	        ...NewMirrorNotificationFields
	      }
	
	      ... on NewCollectNotification {
	        notificationId
	        ...NewCollectNotificationFields
	      }
	
	      ... on NewCommentNotification {
	        notificationId
	        ...NewCommentNotificationFields
	      }
	
	      ... on NewMentionNotification {
	        notificationId
	        ...NewMentionNotificationFields
	      }
	      ... on NewReactionNotification {
	        notificationId
	        ...NewReactionNotificationFields
	      }
	    }
	    pageInfo {
	      ...CommonPaginatedResultInfoFields
	    }
	  }
	}
	
	fragment CommentWithCommentedPublicationFields on Comment {
	  ...CommentFields
	  commentOn {
	    ... on Post {
	      ...PostFields
	    }
	    ... on Mirror {
	      ...MirrorFields
	    }
	    ... on Comment {
	      ...CommentFields
	    }
	  }
	}
	
	fragment NewFollowerNotificationFields on NewFollowerNotification {
	  __typename
	  createdAt
	  isFollowedByMe
	  wallet {
	    ...WalletFields
	  }
	}
	
	fragment NewCollectNotificationFields on NewCollectNotification {
	  __typename
	  createdAt
	  wallet {
	    ...WalletFields
	  }
	  collectedPublication {
	    __typename
	    ... on Post {
	      ...PostFields
	    }
	
	    ... on Mirror {
	      ...MirrorFields
	    }
	
	    ... on Comment {
	      ...CommentFields
	    }
	  }
	}
	
	fragment NewMirrorNotificationFields on NewMirrorNotification {
	  __typename
	  createdAt
	  profile {
	    ...ProfileFields
	  }
	  publication {
	    ... on Post {
	      ...PostFields
	    }
	    ... on Comment {
	      ...CommentFields
	    }
	  }
	}
	
	fragment NewCommentNotificationFields on NewCommentNotification {
	  __typename
	  createdAt
	  profile {
	    ...ProfileFields
	  }
	  comment {
	    ...CommentWithCommentedPublicationFields
	  }
	}
	
	fragment NewMentionNotificationFields on NewMentionNotification {
	  __typename
	  mentionPublication {
	    ... on Post {
	      ...PostFields
	    }
	    ... on Comment {
	      ...CommentFields
	    }
	  }
	  createdAt
	}
	
	fragment NewReactionNotificationFields on NewReactionNotification {
	  __typename
	  createdAt
	  profile {
	    ...ProfileFields
	  }
	  reaction
	  publication {
	    ... on Post {
	      ...PostFields
	    }
	
	    ... on Mirror {
	      ...MirrorFields
	    }
	
	    ... on Comment {
	      ...CommentFields
	    }
	  }
	}
	""".format(var_dict=var_dict)