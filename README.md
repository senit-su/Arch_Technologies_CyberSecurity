---

# Cybersecurity Mini Projects (Python)

This repository contains two educational cybersecurity projects developed using Python:

"* Task 1: Basic Network Sniffer
* Task 2: Educational Keylogger Simulation"

Both projects were created strictly for academic and learning purposes.

---

# TASK 1 – Basic Network Sniffer (Python)

## Overview

This project implements a basic network sniffer in Python to capture and analyze live network traffic. It demonstrates how data flows through a network and how packets are structured at the Network (IP) and Transport (TCP/UDP/ICMP) layers.

The sniffer captures packets in real time and extracts:

"* Source IP address
* Destination IP address
* Protocol (TCP, UDP, ICMP)
* Packet size"

---

## Technologies Used

* Python 3
* Scapy (packet manipulation library)
* Npcap (Windows packet capture driver)
* Visual Studio Code

---

## Features

* Live packet capture
* Protocol identification (TCP/UDP/ICMP)
* Packet filtering using BPF filters
* Automatic stop after defined packet count
* Optional report file generation

---

## Installation

1. Install Python 3
2. Install Scapy:

   ```bash
   pip install scapy
   ```
3. Install Npcap

   * Enable WinPcap API-compatible mode
4. Run VS Code as Administrator (required for packet capture)

---

## Usage

Run the script:

```bash
python network_sniffer.py
```

Optional: Modify the `filter` parameter to capture specific traffic.

Examples:

* `"ip"` → Capture only IP packets
* `"tcp"` → Capture only TCP packets
* `"tcp port 8080"` → Capture Burp Suite traffic

---

## Example Output

```
[10:15:22] TCP | 192.168.1.5 -> 142.250.183.206 | Size: 74 bytes
```

---

## Learning Outcomes

* Understanding packet structure
* Differentiating network vs transport layer
* Using Berkeley Packet Filters (BPF)
* Real-time traffic monitoring

---

## Ethical Disclaimer

This project was developed strictly for educational purposes. Packet capturing should only be performed on authorized systems and networks.

---

# TASK 2 – Educational Keylogger Simulation

## Important Disclaimer

This project is for educational use only in controlled, authorized environments.

* Only run on systems you own or have explicit permission to test
* Unauthorized use of keyloggers is illegal and unethical
* This simulation helps cybersecurity professionals understand threats to better defend against them

---

## Overview

This project simulates a basic software keylogger to demonstrate how keystroke logging works and to analyze associated cybersecurity risks.

The script:

* Captures keystrokes in real time
* Logs them to a local file with timestamps
* Distinguishes between regular characters and special keys
* Stops when ESC is pressed

---

## Requirements

* Python 3.x
* pynput library

---

## Installation & Setup

Install dependency:

```bash
pip install pynput
```

Run the script:

```bash
python edu_keylogger.py
```

---

## How It Works

The script uses `pynput.keyboard.Listener` to monitor keyboard events:

* on_press()

  * Logs regular characters normally
  * Logs special keys in brackets
  * Stops execution when ESC is pressed

All keystrokes are saved to:

```
keylog.txt
```

---

## Sample Log Output

```
2024-05-20 10:30:15,123: H
2024-05-20 10:30:15,145: e
2024-05-20 10:30:15,167: l
2024-05-20 10:30:15,189: l
2024-05-20 10:30:15,211: o
2024-05-20 10:30:15,256: [space]
2024-05-20 10:30:15,389: [enter]
```

---

## Security Analysis

This simulation highlights the risks of keylogging:

| Risk             | Description                            |
| ---------------- | -------------------------------------- |
| Credential Theft | Passwords and PINs can be captured     |
| Data Breaches    | Private messages and documents exposed |
| Financial Loss   | Banking details compromised            |
| Account Takeover | Email and social accounts accessed     |

---

## Protection Measures

* Enable Two-Factor Authentication (2FA)
* Keep software updated
* Use a password manager
* Install reputable antivirus software
* Avoid suspicious downloads
* Check for hardware keyloggers on public systems

---

## Learning Objectives

* Understand keystroke logging mechanisms
* Analyze risks associated with keyloggers
* Learn defensive cybersecurity strategies
* Apply ethical security practices

---

## Clean Up

After testing:

```bash
rm edu_keylogger.py keylog.txt
```

---

## Author

Sarah Binte Tariq
Cybersecurity & Python Enthusiast

---
