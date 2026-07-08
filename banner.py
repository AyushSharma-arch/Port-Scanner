"""
===========================================================
Professional Python Port Scanner v3.0
banner.py
===========================================================
"""

import platform
import socket
import datetime

import pyfiglet

from colorama import (
    Fore,
    Style,
    init
)

from config import (
    APP_NAME,
    VERSION,
    AUTHOR,
    DESCRIPTION,
    LINE
)

init(autoreset=True)


class Banner:

    def __init__(self):

        self.host = socket.gethostname()

        self.os = platform.system()

        self.release = platform.release()

        self.python = platform.python_version()

        self.time = datetime.datetime.now()

    # =====================================================
    # ASCII Banner
    # =====================================================

    def ascii_banner(self):

        print(

            Fore.CYAN +

            pyfiglet.figlet_format(

                "PORT SCANNER",

                font="slant"

            )

        )

    # =====================================================
    # Project Information
    # =====================================================

    def project_info(self):

        print(Fore.YELLOW + LINE)

        print(

            Fore.GREEN +

            f"{APP_NAME}  v{VERSION}"

        )

        print(

            Fore.WHITE +

            DESCRIPTION

        )

        print(

            Fore.MAGENTA +

            f"Author : {AUTHOR}"

        )

        print(Fore.YELLOW + LINE)

    # =====================================================
    # System Information
    # =====================================================

    def system_info(self):

        print(

            Fore.CYAN +

            "\nSYSTEM INFORMATION"

        )

        print(Fore.YELLOW + "-" * 50)

        print(

            f"Hostname : {self.host}"

        )

        print(

            f"Operating System : {self.os}"

        )

        print(

            f"OS Version : {self.release}"

        )

        print(

            f"Python Version : {self.python}"

        )

        print(

            "Date :",

            self.time.strftime("%d-%m-%Y")

        )

        print(

            "Time :",

            self.time.strftime("%H:%M:%S")

        )

    # =====================================================
    # Features
    # =====================================================

    def features(self):

        print(

            Fore.GREEN +

            "\nFEATURES"

        )

        print(Fore.YELLOW + "-" * 50)

        print("[✓] Multi-threaded TCP Scan")

        print("[✓] Banner Grabbing")

        print("[✓] Service Detection")

        print("[✓] JSON Report")

        print("[✓] TXT Report")

        print("[✓] CSV Report")

        print("[✓] Logging")

        print("[✓] Progress Bar")

        print("[✓] Custom Port Range")

        print("[✓] Timeout Support")

    # =====================================================
    # Usage
    # =====================================================

    def usage(self):

        print(

            Fore.BLUE +

            "\nEXAMPLES"

        )

        print(Fore.YELLOW + "-" * 50)

        print(

            "python3 scanner.py localhost"

        )

        print(

            "python3 scanner.py localhost -p 1-1000"

        )

        print(

            "python3 scanner.py scanme.nmap.org -p 22,80,443"

        )

        print(

            "python3 scanner.py 192.168.1.10 -t 200"

        )

        print(

            "python3 scanner.py localhost -o json"

        )

    # =====================================================
    # Display Banner
    # =====================================================

    def show(self):

        self.ascii_banner()

        self.project_info()

        self.system_info()

        self.features()

        self.usage()

        print()

        print(Fore.YELLOW + LINE)