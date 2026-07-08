"""
===========================================================
Python Port Scanner v3.0
Configuration File
Author : Ayush Sharma
===========================================================
"""

# ===============================
# Application Information
# ===============================

APP_NAME = "Professional Python Port Scanner"

VERSION = "3.0.0"

AUTHOR = "Ayush Sharma"

DESCRIPTION = "Multi-threaded TCP Port Scanner with Banner Grabbing"


# ===============================
# Default Scanner Configuration
# ===============================

DEFAULT_TIMEOUT = 1.0

DEFAULT_THREADS = 100

DEFAULT_PORT_RANGE = "1-1024"


# ===============================
# Output Configuration
# ===============================

REPORT_DIRECTORY = "reports"

LOG_DIRECTORY = "logs"

SCREENSHOT_DIRECTORY = "screenshots"


# ===============================
# Report Formats
# ===============================

REPORT_JSON = "json"

REPORT_TXT = "txt"

REPORT_CSV = "csv"


# ===============================
# Colors
# ===============================

SUCCESS = "[+]"

ERROR = "[-]"

WARNING = "[!]"

INFO = "[*]"


# ===============================
# Console Lines
# ===============================

LINE = "=" * 75

SMALL_LINE = "-" * 75


# ===============================
# Default Socket Buffer
# ===============================

BUFFER_SIZE = 1024


# ===============================
# Progress Bar
# ===============================

PROGRESS_UNIT = "port"

PROGRESS_DESCRIPTION = "Scanning"


# ===============================
# Supported Banner Ports
# ===============================

BANNER_PORTS = [

    21,     # FTP
    22,     # SSH
    23,     # Telnet
    25,     # SMTP
    80,     # HTTP
    110,    # POP3
    143,    # IMAP
    443,    # HTTPS
    3306,   # MySQL
    5432,   # PostgreSQL
    6379,   # Redis
    8080,   # HTTP Alternate

]


# ===============================
# Default HTTP Request
# ===============================

HTTP_REQUEST = (

    b"HEAD / HTTP/1.0\r\n"
    b"Host: localhost\r\n"
    b"User-Agent: PythonPortScanner\r\n"
    b"\r\n"

)


# ===============================
# Application Banner
# ===============================

WELCOME_MESSAGE = f"""
{LINE}

{APP_NAME}
Version : {VERSION}

Author : {AUTHOR}

{DESCRIPTION}

{LINE}
"""


# ===============================
# End of File
# ===============================