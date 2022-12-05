authenticate_query = """
mutation authenticate {
  authenticate(request: 
        {
        {args}}
        ) {
    accessToken
    refreshToken
  }
}

"""