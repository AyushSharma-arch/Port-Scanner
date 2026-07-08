
"""
===========================================================
Python Port Scanner v3.0
scanner.py
===========================================================
"""

import argparse
from colorama import Fore, init

from banner import Banner
from logger import ScannerLogger
from report import ReportGenerator
from utils import (
    validate_host,
    current_time
)

init(autoreset=True)


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Professional Python Project"
    )

    parser.add_argument(
        "host",
        help="Target Hostname or IP"
    )

    parser.add_argument(
        "-o",
        "--output",
        choices=["json", "txt", "csv"],
        default="json",
        help="Report Format"
    )

    return parser.parse_args()


def print_summary(host):

    print("\n" + "=" * 70)
    print(Fore.CYAN + "PROJECT SUMMARY")
    print("=" * 70)

    print(f"Target       : {host}")
    print(f"Started      : {current_time()}")
    print("Status       : Ready")
    print("Logging      : Enabled")
    print("Reports      : JSON / TXT / CSV")

    print("=" * 70)


def main():

    banner = Banner()
    banner.show()

    args = get_arguments()

    logger = ScannerLogger()

    logger.scan_started(args.host)

    if not validate_host(args.host):

        print(Fore.RED + "\n[-] Invalid Hostname or IP Address")
        logger.error("Invalid Host")
        return

    print_summary(args.host)

    # Demo Results
    results = [
        {
            "port": 22,
            "service": "ssh",
            "status": "OPEN"
        },
        {
            "port": 80,
            "service": "http",
            "status": "OPEN"
        }
    ]

    report = ReportGenerator()

    if args.output == "json":

        file = report.save_json(
            args.host,
            results
        )

    elif args.output == "txt":

        file = report.save_txt(
            args.host,
            results
        )

    else:

        file = report.save_csv(
            args.host,
            results
        )

    logger.scan_completed(
        total_ports=len(results),
        open_ports=len(results),
        closed_ports=0,
        duration=0.01
    )

    print(Fore.GREEN)
    print("\n[✓] Report Generated Successfully")
    print(f"[✓] Saved To : {file}")


if __name__ == "__main__":
    main()