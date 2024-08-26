# NFS Throughput Test Script

This script is designed to test the throughput of an NFS-mounted filesystem by simulating multiple concurrent file operations (read/write). It uses Python's threading and multiprocessing modules to perform these operations, simulating a real-world scenario where multiple users or processes are accessing the NFS share simultaneously.

## Features

- Automatically mounts an NFS share.
- Simulates concurrent read or write operations on multiple files.
- Measures and reports throughput in MB/s.
- Configurable number of files, file sizes, and concurrent operations.

## Requirements

- Python 3.x
- NFS client tools installed (`nfs-common` package on Linux).
- An NFS server available and accessible from the client machine.
- Root privileges (for mounting NFS shares).

## Configuration

Before running the script, update the configuration variables in the script:

- `nfs_mount_point`: The directory where the NFS share will be mounted (e.g., `/mnt/nfs_test`).
- `nfs_server`: The NFS server address and share path (e.g., `nfs_server_ip:/nfs_share`).
- `file_count`: The number of files to operate on.
- `file_size`: The size of each file in bytes (e.g., `100 * 1024 * 1024` for 100MB files).
- `num_threads`: The number of concurrent operations (threads or processes) to run.
- `operation_type`: Set to `'write'` for writing files or `'read'` for reading files.

## Usage

1. **Mount the NFS Share**: Ensure the NFS share is available and accessible.

2. **Run the Script**:

   ```bash
   sudo python3 nfs_throughput_test.py

