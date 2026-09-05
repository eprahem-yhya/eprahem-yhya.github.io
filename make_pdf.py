# -*- coding: utf-8 -*-
"""Render the CV to a real PDF file.

    python make_pdf.py

The in-page "Save as PDF" button calls window.print(), which does nothing at
all inside Telegram's built-in browser — the most likely place a client opens
the link from. A downloadable file removes the dependency on the viewer.
"""

import os
import subprocess
import sys

CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "index.html")
OUT = os.path.join(os.path.dirname(HERE), "amber-cafe", "Eprahem-Yhya-CV.pdf")

url = "file:///" + SRC.replace(os.sep, "/")
cmd = [
    CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--print-to-pdf=" + OUT, "--no-pdf-header-footer",
    "--virtual-time-budget=10000",       # let the web fonts land first
    url,
]
p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
size = os.path.getsize(OUT) if os.path.exists(OUT) else 0
print("rc=%s · %s · %d bytes" % (p.returncode, OUT, size))
if not size:
    print((p.stderr or "")[:400], file=sys.stderr)
