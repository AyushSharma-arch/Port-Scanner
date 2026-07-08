"""
===========================================================
Professional Python Port Scanner v3.0
utils.py
===========================================================
"""

import socket
import ipaddress
from datetime import datetime


# ==========================================================
# Validate IPv4 Address
# ==========================================================

def is_valid_ip(ip):

    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


# ==========================================================
# Resolve Hostname -> IP
# ==========================================================

def resolve_host(host):

    try:
        return socket.gethostbyname(host)

    except socket.gaierror:
        return None


# ==========================================================
# Reverse DNS Lookup
# ==========================================================

def get_hostname(ip):

    try:
        return socket.gethostbyaddr(ip)[0]

    except Exception:
        return "Unknown"


# ==========================================================
# Parse Port Range
# Examples:
# 22
# 22,80,443
# 1-1000
# ==========================================================

def parse_ports(port_string):

    ports = []

    try:

        if "-" in port_string:

            start, end = map(int, port_string.split("-"))

            for port in range(start, end + 1):

                if 1 <= port <= 65535:
                    ports.append(port)

        elif "," in port_string:

            for port in port_string.split(","):

                p = int(port.strip())

                if 1 <= p <= 65535:
                    ports.append(p)

        else:

            p = int(port_string)

            if 1 <= p <= 65535:
                ports.append(p)

    except Exception:
        return []

    return sorted(list(set(ports)))


# ==========================================================
# Get Service Name
# ==========================================================

def get_service(port):

    try:
        return socket.getservbyport(port)

    except Exception:
        return "Unknown"


# ==========================================================
# Current Date & Time
# ==========================================================

def current_time():

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


# ==========================================================
# Scan Duration
# ==========================================================

def format_duration(seconds):

    if seconds < 60:
        return f"{seconds:.2f} sec"

    minutes = int(seconds // 60)

    sec = seconds % 60

    return f"{minutes} min {sec:.2f} sec"
# ==========================================================
# Validate Host
# ==========================================================

def validate_host(host):

    if is_valid_ip(host):
        return True

    ip = resolve_host(host)

    return ip is not None


# ==========================================================
# Validate Port List
# ==========================================================

def validate_ports(ports):

    valid = []

    for port in ports:

        if 1 <= port <= 65535:
            valid.append(port)

    return valid


# ==========================================================
# Remove Duplicate Ports
# ==========================================================

def unique_ports(ports):

    return sorted(list(set(ports)))


# ==========================================================
# Clean Banner Output
# ==========================================================

def clean_banner(banner):

    if not banner:
        return "-"

    banner = banner.replace("\r", "")
    banner = banner.replace("\n", " ")
    banner = banner.strip()

    if len(banner) > 80:
        banner = banner[:80] + "..."

    return banner


# ==========================================================
# Format Table Row
# ==========================================================

def format_row(status, port, service, banner):

    return (
        f"{status:<10}"
        f"{port:<8}"
        f"{service:<15}"
        f"{banner}"
    )


# ==========================================================
# Format Scan Header
# ==========================================================

def scan_header():

    print("=" * 75)

    print(
        f"{'STATUS':<10}"
        f"{'PORT':<8}"
        f"{'SERVICE':<15}"
        "BANNER"
    )

    print("-" * 75)


# ==========================================================
# Scan Summary
# ==========================================================

def scan_summary(total_ports,
                 open_ports,
                 closed_ports,
                 duration):

    print("\n" + "=" * 75)

    print("SCAN SUMMARY")

    print("=" * 75)

    print(f"Total Ports   : {total_ports}")

    print(f"Open Ports    : {open_ports}")

    print(f"Closed Ports  : {closed_ports}")

    print(f"Scan Time     : {format_duration(duration)}")

    print("=" * 75)


# ==========================================================
# Convert Result Dictionary
# ==========================================================

def build_result(port,
                 service,
                 banner):

    return {

        "port": port,

        "service": service,

        "banner": banner

    }


# ==========================================================
# Sort Scan Results
# ==========================================================

def sort_results(results):

    return sorted(

        results,

        key=lambda x: x["port"]

    )


# ==========================================================
# Display Target Information
# ==========================================================

def print_target(host,
                 ip,
                 hostname,
                 threads,
                 timeout):

    print("=" * 75)

    print(f"Target Host : {host}")

    print(f"Target IP   : {ip}")

    print(f"Hostname    : {hostname}")

    print(f"Threads     : {threads}")

    print(f"Timeout     : {timeout}")

    print(f"Started     : {current_time()}")

    print("=" * 75)


# ==========================================================
# End of utils.py
# ==========================================================