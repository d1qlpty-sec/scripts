#!/usr/bin/env python3
"""
ARP spoof detector (Scapy).
Tracks each MAC->IP mapping; if a known MAC suddenly claims a different IP,
it flags a possible ARP spoofing attack.

Usage:
    sudo apt install python3-scapy
    sudo python3 arp_spoof_detector.py
"""
from scapy.all import sniff

ip_mac_map = {}

def process(packet):
    src_ip = packet['ARP'].psrc
    src_mac = packet['Ether'].src
    if src_mac in ip_mac_map:
        old_ip = ip_mac_map.get(src_mac, "unknown")
        if old_ip != src_ip:
            print(f"[!] Possible ARP spoof: {src_mac} was {old_ip}, now claims {src_ip}")
    else:
        ip_mac_map[src_mac] = src_ip

# filter examples: "arp" | "tcp" | "udp and port 53" | "host 192.168.1.10"
sniff(count=0, filter="arp", store=0, prn=process)
