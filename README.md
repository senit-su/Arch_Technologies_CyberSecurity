---
#TASK 1
# Basic Network Sniffer (Python)

## Overview
This project implements a **basic network sniffer in Python** to capture and analyze live network traffic. The program demonstrates how data flows across a network and how packets are structured at the IP and transport layers.

The sniffer captures packets in real time and extracts:

* Source IP address
* Destination IP address
* Protocol (TCP, UDP, ICMP)
* Packet size

---
## Technologies Used

* Python 3
* Scapy (Packet manipulation library)
* Npcap (Windows packet capture driver)
* Visual Studio Code

---
## Features

* Live packet capture
* Protocol identification (TCP/UDP/ICMP)
* Packet filtering using BPF filters
* Automatic stop after a defined number of packets
* Optional report file generation

---
## Installation

1. Install Python 3
2. Install Scapy:

   ```
   pip install scapy
   ```
3. Install Npcap (enable WinPcap API-compatible mode)
4. Run VS Code as Administrator (required for packet capture)

---
## Usage
Run the script:
```
python network_sniffer.py
```
Optional: Modify the `filter` parameter to capture specific traffic:

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
This project demonstrates:

* Basic packet sniffing concepts
* Network vs Transport layer analysis
* Use of Berkeley Packet Filters (BPF)
* Real-time network monitoring
---
## Ethical Disclaimer

This project is developed strictly for educational purposes.
Packet capture should only be performed on authorized networks.
---
