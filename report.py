"""
===========================================================
Python Port Scanner v3.0
report.py
===========================================================
"""

import json
import csv
import os
from datetime import datetime

from config import REPORT_DIRECTORY


class ReportGenerator:

    def __init__(self):

        os.makedirs(REPORT_DIRECTORY, exist_ok=True)

    def _timestamp(self):

        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def save_json(self, target, results):

        filename = os.path.join(
            REPORT_DIRECTORY,
            f"{target}_scan.json"
        )

        data = {
            "target": target,
            "generated": self._timestamp(),
            "total_open_ports": len(results),
            "results": results
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return filename

    def save_csv(self, target, results):

        filename = os.path.join(
            REPORT_DIRECTORY,
            f"{target}_scan.csv"
        )

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Port",
                "Service",
                "Status"
            ])

            for item in results:

                writer.writerow([
                    item["port"],
                    item["service"],
                    item["status"]
                ])

        return filename

    def save_txt(self, target, results):

        filename = os.path.join(
            REPORT_DIRECTORY,
            f"{target}_scan.txt"
        )

        with open(filename, "w", encoding="utf-8") as file:

            file.write("=" * 70 + "\n")
            file.write("PORT SCAN REPORT\n")
            file.write("=" * 70 + "\n\n")

            file.write(f"Target : {target}\n")
            file.write(
                f"Generated : {self._timestamp()}\n\n"
            )

            file.write(
                f"{'PORT':<10}"
                f"{'SERVICE':<15}"
                f"{'STATUS'}\n"
            )

            file.write("-" * 70 + "\n")

            for item in results:

                file.write(
                    f"{item['port']:<10}"
                    f"{item['service']:<15}"
                    f"{item['status']}\n"
                )

        return filename