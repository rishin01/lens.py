ProxyAction_query = """
mutation ProxyAction {
  proxyAction(request: 
        {
        {args}}
        )
}

""".format(args=args)