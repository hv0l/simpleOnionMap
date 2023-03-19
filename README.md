# Onion Scanner

Onion Scanner is a Python script that performs port scans using Nmap on Onion websites within the Tor network.

## Requirements

- Python 3
- Tor
- Proxychains
- Nmap

## Installation

1. Clone this repository or download the ZIP file and extract it.
2. Install the dependencies by running the command `pip install -r requirements.txt`.
3. Copy the `onion_scan.py` script to the `/usr/local/bin` directory and make sure it's executable with `chmod +x onion_scan.py`.

## Usage

Run the script with the command:

```sudo python3 onion_scan.py```


The script will guide you through the following steps:

1. Enter the Onion URL.
2. Choose the type of scan:
   - Stealth Scan (-sS)
   - Quick Scan (no options)
   - Comprehensive Scan (-A)

The scan output will be displayed in the terminal and saved to an XML file with a name based on the Onion URL.

