from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

# This function runs every time a packet is captured
def packet_handler(packet):

    # Check if the packet contains an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        protocol = "OTHER"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        time = datetime.now().strftime("%H:%M:%S")

        print(f"[{time}] {protocol} | {src_ip} -> {dst_ip} | Size: {size} bytes")

print("Starting Network Sniffer...")
print("Press CTRL + C to stop\n")

# sniff() parameters:
# prn=packet_handler  → function to execute for each packet
# store=False         → do not store packets in memory
# count=15            → stop after 15 packets
# filter="ip"         → capture only IP packets (BPF filter)

sniff(prn=packet_handler, store=False, count=15)
