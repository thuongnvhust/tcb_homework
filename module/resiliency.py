import json

POOLS_PATH = "resource/pools.json"

def load_pools() -> dict:
    '''
        Returns a dict loaded from disk

        :param dict pools:
            Specifies pools
    '''
    try:
        with open(POOLS_PATH, 'r') as json_file:
            pools = json.load(json_file)
    except Exception:
        return {}

    return pools

def save_pools(pools=dict) -> Exception:
    '''
        Returns exeption when save pools to disk

        :param dict pools:
            Specifies pools
    '''
    try:
        with open(POOLS_PATH, "w") as write_file:
            json.dump(pools, write_file, indent=4)
    except Exception as ex:
        return ex

    return None
