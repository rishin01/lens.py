#Different follow modes: https://docs.lens.xyz/docs/create-profile

def createProfileQuery(**kwargs):


    createProfile = """"
        mutation CreateProfile {
        createProfile(request:{ 
                        handle: "{handle}",
                        profilePictureUri: {profilePictureUri},
                        followNFTURI: {followNFTURI},
                        followModule: {followModule}
                        }) {
            ... on RelayerResult {
            txHash
            }
            ... on RelayError {
            reason
            }
            __typename
        }
        }
    """.format(handle=handle,profilePictureUri = profilePictureUri, followNFTURI = followNFTURI, followModule = followNFTURI)


