---
# TASK 1
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

# TASK 2
# Educational Keylogger Simulation
This project is a basic keylogger simulation created strictly for educational purposes to understand how keystroke logging works and to analyze associated cybersecurity risks.

## IMPORTANT DISCLAIMER
This code is for educational use ONLY in controlled, authorized environments.
- Only run on systems you own or have explicit permission to test
- Unauthorized use of keyloggers is illegal and unethical
- This simulation helps cybersecurity professionals understand threats to better defend against them

## Overview
This Python script demonstrates the fundamental mechanics of a software keylogger:
- Captures keystrokes in real-time
- Logs them to a local file with timestamps
- Distinguishes between regular characters and special keys
- Runs in the background until manually stopped

## Requirements
- Python 3.x
- pynput library

## Installation & Setup
1. Clone or download this repository

2. Install the required library:
   ```bash
   pip install pynput
   ```

3. Run the script:
   ```bash
   python edu_keylogger.py
   ```

## How It Works
The script uses the pynput.keyboard.Listener class to monitor keyboard events:

- on_press function: Triggered every time a key is pressed
  - Regular characters (letters, numbers, symbols) are logged as-is
  - Special keys (Shift, Enter, Space, etc.) are logged in [brackets]
  - Pressing ESC stops the keylogger

- Logging: All keystrokes are saved to keylog.txt with timestamps

## Sample Output
Console:
```
[*] Keylogger started. Logging keystrokes to keylog.txt
[*] Press 'ESC' to stop.
[!] Escape key pressed. Stopping keylogger...
[*] Keylogger stopped.
```

Log file (keylog.txt):
```
2024-05-20 10:30:15,123: H
2024-05-20 10:30:15,145: e
2024-05-20 10:30:15,167: l
2024-05-20 10:30:15,189: l
2024-05-20 10:30:15,211: o
2024-05-20 10:30:15,256: [space]
2024-05-20 10:30:15,278: W
2024-05-20 10:30:15,300: o
2024-05-20 10:30:15,322: r
2024-05-20 10:30:15,344: l
2024-05-20 10:30:15,366: d
2024-05-20 10:30:15,389: [enter]
```

## Security Analysis
This simulation demonstrates why keyloggers are dangerous:

| Risk | Description |
|------|-------------|
| Credential Theft | Passwords, usernames, and PINs can be captured |
| Data Breaches | Private messages, documents, and personal information exposed |
| Financial Loss | Banking details and credit card numbers at risk |
| Account Takeover | Attackers can access email, social media, and corporate accounts |

## Protection Measures
After running this simulation, implement these defenses:

1. Use Two-Factor Authentication (2FA) - Even with passwords, attackers can't access accounts
2. Keep software updated - Patches vulnerabilities keyloggers exploit
3. Use a password manager - Auto-fill credentials to avoid typing them
4. Install reputable antivirus - Detects and blocks keylogger installations
5. Be cautious with downloads - Avoid suspicious email attachments and websites
6. Check for physical devices - Inspect for hardware keyloggers on public computers

## Learning Objectives
- Understand the technical mechanics of keystroke logging
- Recognize the severity of this attack vector
- Learn defensive strategies for real-world protection
- Apply this knowledge to cybersecurity practices

## Clean Up
Always delete the script and log files after testing:
```bash
rm edu_keylogger.py keylog.txt
```
---
Remember: This knowledge is power—use it to protect, not to harm. Ethical understanding of attack methods is the foundation of strong cybersecurity defense.

## Author

Sarah Binte Tariq - 
Cybersecurity & Python Enthusiast
