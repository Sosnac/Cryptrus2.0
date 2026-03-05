#!/usr/bin/env python3
"""
Device Detection Module - Gathers device information from active hosts
"""

import subprocess
import socket
from typing import Dict, Any

class DeviceDetector:
    """Device detection and information gathering"""
    
    def __init__(self):
        self.mac_vendors = self._load_mac_vendors()
    
    def _load_mac_vendors(self) -> Dict[str, str]:
        """Load common MAC vendor prefixes"""
        return {
            '08:00:27': 'PCS Systemtechnik (VirtualBox)',
            '00:0a:95': 'Xerox',
            '00:0c:6e': 'Arista Networks',
            '00:0d:88': 'Fujitsu',
            '00:11:11': 'Cisco Systems',
            '00:15:c5': 'Apple Inc.',
            '00:1a:a0': 'Philips Electronics',
            '00:1d:92': 'Google Inc.',
            '00:25:86': 'Apple Inc.',
            '00:50:f2': 'Microsoft Corporation',
        }
    
    def get_device_info(self, ip_address: str) -> Dict[str, Any]:
        """Gather information about a device"""
        info = {
            'ip': ip_address,
            'hostname': self._get_hostname(ip_address),
            'mac': self._get_mac_address(ip_address),
            'manufacturer': self._get_manufacturer(ip_address),
            'open_ports': self._scan_common_ports(ip_address)
        }
        return info
    
    def _get_hostname(self, ip: str) -> str:
        """Get hostname from IP address"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except (socket.herror, socket.timeout):
            return "Unknown"
    
    def _get_mac_address(self, ip: str) -> str:
        """Get MAC address using ARP (Termux-compatible)"""
        try:
            result = subprocess.run(
                ['arp', '-n', ip],
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if ip in line:
                        parts = line.split()
                        if len(parts) > 2:
                            return parts[2]
        except Exception:
            pass
        return "Unknown"
    
    def _get_manufacturer(self, ip: str) -> str:
        """Get device manufacturer from MAC address"""
        mac = self._get_mac_address(ip)
        if mac != "Unknown":
            prefix = mac[:8].upper()
            return self.mac_vendors.get(prefix, f"Unknown (MAC: {mac})")
        return "Unknown"
    
    def _scan_common_ports(self, ip: str) -> list:
        """Scan for common open ports"""
        common_ports = [22, 23, 80, 443, 8080, 5900, 3389, 9200, 9300, 5432, 3306]
        open_ports = []
        
        for port in common_ports:
            if self._is_port_open(ip, port):
                open_ports.append(port)
        
        return open_ports
    
    def _is_port_open(self, ip: str, port: int) -> bool:
        """Check if port is open using netcat (Termux-compatible)"""
        try:
            result = subprocess.run(
                ['timeout', '1', 'bash', '-c', f'</dev/null >/dev/tcp/{ip}/{port}'],
                capture_output=True,
                timeout=2
            )
            return result.returncode == 0
        except Exception:
            return False
