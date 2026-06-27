
# Import required libraries
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Target URL to test
URL = "http://ec2-54-167-34-77.compute-1.amazonaws.com:8080/"

# Total number of requests to send
TOTAL_REQUESTS = 10000

# Number of concurrent users (threads)
CONCURRENT_USERS = 3

# Counters for successful and failed requests
success = 0
failed  = 0

# Store response times for latency calculations
latencies = []


def make_request():
    """
    Sends a single HTTP GET request and measures latency.
    Returns:
        (True, latency)  -> if status code is 200
        (False, latency) -> if non-200 response
        (False, None)    -> if request fails
    """

    # Record start time
    start = time.time()

    try:
        # Send GET request
        response = requests.get(URL, timeout=10)

        # Calculate response time
        latency = time.time() - start

        # Success if HTTP 200
        if response.status_code == 200:
            return True, latency
        else:
            return False, latency

    except Exception:
        # Request failed due to timeout, DNS issue, connection error, etc.
        return False, None


# Record test start time
start_time = time.time()

# Create thread pool for concurrent execution
with ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:

    # Submit all requests to thread pool
    futures = [
        executor.submit(make_request)
        for _ in range(TOTAL_REQUESTS)
    ]

    # Process completed requests
    for future in as_completed(futures):

        ok, latency = future.result()

        if ok:
            success += 1
        else:
            failed += 1

        # Store latency for statistics
        if latency:
            latencies.append(latency)

# Calculate total test duration
duration = time.time() - start_time

# Print summary
print("\n========== LOAD TEST RESULTS ==========")
print(f"Target URL       : {URL}")
print(f"Total Requests   : {TOTAL_REQUESTS}")
print(f"Concurrent Users : {CONCURRENT_USERS}")
print(f"Successful       : {success}")
print(f"Failed           : {failed}")
print(f"Duration         : {duration:.2f} sec")
print(f"Requests/sec     : {TOTAL_REQUESTS / duration:.2f}")

# Print latency metrics
if latencies:
    print(f"Average Latency  : {sum(latencies)/len(latencies):.3f} sec")
    print(f"Minimum Latency  : {min(latencies):.3f} sec")
    print(f"Maximum Latency  : {max(latencies):.3f} sec")



print("======================================")





