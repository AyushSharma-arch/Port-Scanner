"""
===========================================================
Professional Python Port Scanner v3.0
logger.py
===========================================================
"""

import logging
import os

from config import LOG_DIRECTORY


class ScannerLogger:

    def __init__(self):

        os.makedirs(LOG_DIRECTORY, exist_ok=True)

        self.logger = logging.getLogger("ProfessionalPortScanner")

        self.logger.setLevel(logging.INFO)

        self.logger.propagate = False

        if not self.logger.handlers:

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)-8s | %(message)s",

                datefmt="%d-%m-%Y %H:%M:%S"

            )

            file_handler = logging.FileHandler(

                os.path.join(

                    LOG_DIRECTORY,

                    "scanner.log"

                )

            )

            file_handler.setLevel(logging.INFO)

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    # ==========================================
    # INFO
    # ==========================================

    def info(self, message):

        self.logger.info(message)

    # ==========================================
    # WARNING
    # ==========================================

    def warning(self, message):

        self.logger.warning(message)

    # ==========================================
    # ERROR
    # ==========================================

    def error(self, message):

        self.logger.error(message)

    # ==========================================
    # DEBUG
    # ==========================================

    def debug(self, message):

        self.logger.debug(message)

    # ==========================================
    # Scan Started
    # ==========================================

    def scan_started(self, host):

        self.info("=" * 60)

        self.info("SCAN STARTED")

        self.info(f"Target : {host}")

    # ==========================================
    # Open Port
    # ==========================================

    def open_port(self, port, service):

        self.info(

            f"OPEN PORT : {port} ({service})"

        )

    # ==========================================
    # Closed Port
    # ==========================================

    def closed_port(self, port):

        self.debug(

            f"CLOSED PORT : {port}"

        )

    # ==========================================
    # Scan Completed
    # ==========================================

    def scan_completed(

            self,

            total_ports,

            open_ports,

            closed_ports,

            duration

    ):

        self.info("SCAN COMPLETED")

        self.info(

            f"Total Ports : {total_ports}"

        )

        self.info(

            f"Open Ports : {open_ports}"

        )

        self.info(

            f"Closed Ports : {closed_ports}"

        )

        self.info(

            f"Duration : {duration:.2f} sec"

        )

        self.info("=" * 60)

    # ==========================================
    # Exception
    # ==========================================

    def exception(self, error):

        self.logger.exception(error)