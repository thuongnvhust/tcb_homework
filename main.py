import json
import argparse

from flask import Flask, request, make_response, jsonify
from module import validation, resiliency, calculation

app = Flask(__name__)

# Load pools from disk
pools = resiliency.load_pools()

@app.route("/receive", methods=['POST'])
def receive():
    '''
        Returns the response of append/insert a new pool
    '''
    # Parse data
    data = request.data
    try:
        pool = json.loads(data)
    except json.decoder.JSONDecodeError:
        return make_response(jsonify(message="Data must be JSON type"), 400)

    # Validate data
    ex = validation.validate_new_pool(pool=pool)
    if ex is not None:
        return make_response(jsonify(message=ex), 400)

    # Normalize poolId
    pool['poolId'] = str(pool['poolId'])

    # Insert/append a new pool to existed pool
    if pool['poolId'] in pools:
        pools[pool['poolId']] += pool['poolValues']
        status = "appended"
    else:
        pools[pool['poolId']] = pool['poolValues']
        status = "inserted"

    # Save to disk
    warning = ""
    ex = resiliency.save_pools(pools=pools)
    if ex is not None:
        warning = "Could not save pools to disk"

    # Response
    response_message = {
        "status": status,
        "warning": warning
    }

    return make_response(jsonify(message=response_message), 200)

@app.route("/query", methods=['POST'])
def query():
    '''
        Returns the percentile and number of elements of given poolID
    '''
    # Parse data
    data = request.data
    try:
        query = json.loads(data)
    except json.decoder.JSONDecodeError:
        return make_response(jsonify(message="Data must be JSON type"), 400)

    # Validate data
    ex = validation.validate_pool_query(query=query)
    if ex is not None:
        return make_response(jsonify(message=str(ex)), 400)

    # Normalize poolId
    query['poolId'] = str(query['poolId'])

    if query['poolId'] not in pools:
        response_message = {
            "message": f"Pool Id {query['poolId']} not found"
        }
        return make_response(jsonify(message=response_message), 404)

    # Calculate percentile
    percentile_value = calculation.calculate_percentile(array=pools[query['poolId']],
                                                        percentile=query['percentile'])
    response_message = {
        "percentile_value": percentile_value,
        "number_of_elements": len(pools[query['poolId']])
    }

    return make_response(jsonify(message=response_message), 200)


if __name__ == '__main__':
    # Define and parse command-line options
    parser = argparse.ArgumentParser(description='Start API Gateway')

    # Add argument
    parser.add_argument('--host', required=False, type=str, help='Define host (default: %(default)s)')
    parser.add_argument('--port', required=False, type=int, help='Define port (default: %(default)s)')
    parser.add_argument('--debug', required=False, type=bool, help='Define debug mode (default: %(default)s)')

    args = parser.parse_args()

    # Start server
    app.run(host=args.host,
            port=args.port,
            debug=args.debug)
