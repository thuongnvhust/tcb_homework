def validate_new_pool(pool: dict) -> Exception:
    '''
        Returns exception of specific video in seconds

        :param dict pool:
            Specifies pool
    '''
    # Validate keys
    pool_keys = ['poolId', 'poolValues']
    if set(pool.keys()) != set(pool_keys):
        return Exception(f"Request data must have {pool_keys}")
    
    # Validate type of values
    if type(pool['poolId']) != int:
        return Exception(f"poolId must be numeric")

    if type(pool['poolValues']) != list:
        return Exception(f"poolValues must be a list")
    else:
        for value in pool['poolValues']:
            if type(value) != int:
                return Exception(f"poolValues must be a list of integer")
    
    return None

def validate_pool_query(query: dict) -> Exception:
    '''
        Returns exception of specific video in seconds

        :param dict pool:
            Specifies pool
    '''
    # Validate keys
    query_keys = ['poolId', 'percentile']
    if set(query.keys()) != set(query_keys):
        return Exception(f"Request data must have {query_keys}")
    
    # Validate type of values
    if type(query['poolId']) != int:
        return Exception(f"poolId must be numeric")

    if type(query['percentile']) != float and type(query['percentile']) != int:
        return Exception(f"percentile must be a number")
    else:
        if query['percentile'] <= 0 or query['percentile'] >= 100:
            return Exception(f"percentile must be in range(0, 100)")
    
    return None