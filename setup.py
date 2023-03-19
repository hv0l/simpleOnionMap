from setuptools import setup
import os
import shutil

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="onion_scan",
    install_requires=requirements,
    scripts=["onion_scan.py"],
)

# Copy the script to /usr/local/bin
shutil.copy("onion_scan.py", "/usr/local/bin/onion_scan.py")
os.chmod("/usr/local/bin/onion_scan.py", 0o755)
