import os
import time
import threading
import multiprocessing
from pathlib import Path

# Configuration
local_test_dir = "./nfs_test_local"  # Local directory for testing
file_count = 10  # Number of files to operate on
file_size = 100 * 1024 * 1024  # Size of each file in bytes (e.g., 100MB)
num_threads = 5  # Number of concurrent operations (threads or processes)
operation_type = 'write'  # 'write' or 'read'

# Ensure the local test directory exists
def setup_local_directory():
    if not os.path.exists(local_test_dir):
        os.makedirs(local_test_dir)
        print(f"Created local test directory: {local_test_dir}")

# Function to write a large file
def write_file(file_index):
    file_path = Path(local_test_dir) / f"test_file_{file_index}.dat"
    print(f"Creating file: {file_path}")
    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size))

# Function to read a large file
def read_file(file_index):
    file_path = Path(local_test_dir) / f"test_file_{file_index}.dat"
    print(f"Reading file: {file_path}")
    with open(file_path, 'rb') as f:
        while f.read(1024 * 1024):
            pass  # Continue reading the file in 1MB chunks

# Function to perform file operations using threads
def perform_operations_in_threads():
    threads = []  # List to hold threads
    start_time = time.time()  # Start timing the operations

    # Loop to create and start threads for file operations
    for i in range(file_count):
        if operation_type == 'write':
            t = threading.Thread(target=write_file, args=(i,))
        else:
            t = threading.Thread(target=read_file, args=(i,))
        threads.append(t)
        t.start()

        # If the maximum number of concurrent threads is reached, wait for them to complete
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    # Wait for any remaining threads to complete
    for t in threads:
        t.join()

    # Calculate total time taken and throughput
    end_time = time.time()
    total_time = end_time - start_time
    total_data = file_count * file_size / (1024 * 1024)  # in MB
    throughput = total_data / total_time  # MB/s
    print(f"Total data: {total_data:.2f} MB, Time taken: {total_time:.2f} seconds, Throughput: {throughput:.2f} MB/s")

# Function to perform file operations using multiprocessing
def perform_operations_in_processes():
    processes = []  # List to hold processes
    start_time = time.time()  # Start timing the operations

    # Loop to create and start processes for file operations
    for i in range(file_count):
        if operation_type == 'write':
            p = multiprocessing.Process(target=write_file, args=(i,))
        else:
            p = multiprocessing.Process(target=read_file, args=(i,))
        processes.append(p)
        p.start()

        # If the maximum number of concurrent processes is reached, wait for them to complete
        if len(processes) >= num_threads:
            for p in processes:
                p.join()
            processes = []

    # Wait for any remaining processes to complete
    for p in processes:
        p.join()

    # Calculate total time taken and throughput
    end_time = time.time()
    total_time = end_time - start_time
    total_data = file_count * file_size / (1024 * 1024)  # in MB
    throughput = total_data / total_time  # MB/s
    print(f"Total data: {total_data:.2f} MB, Time taken: {total_time:.2f} seconds, Throughput: {throughput:.2f} MB/s")

# Main function
if __name__ == "__main__":
    setup_local_directory()  # Setup local test directory
    print(f"Starting {operation_type} operations in local directory...")

    # Uncomment one of the following lines to use threads or multiprocessing:
    perform_operations_in_threads()
    # perform_operations_in_processes()

