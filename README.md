# ping-sweep (Python)
This Python script performs a basic ICMP ping sweep over a subnet. It iterates through all host IPs in a given network and reports which hosts are reachable.

## Features
- Iterates over all usable hosts in a subnet
- Sends one ping per host
- Prints whether each host is UP or DOWN
- Works on Unix-like systems

## Limitations
- Uses ICMP ping only, which many devices block
- Assumes a Unix-like system (uses ping -c)
- Network is hard-coded
- Scans hosts sequentially and is slow on larger networks
- DOWN does not always mean the host is offline

## Next Steps
- Allowing user-specified networks via command-line arguments
- Cross-platform support for Windows
- Parallel scanning for faster performance
- Alternative discovery methods for hosts that block ping
  

