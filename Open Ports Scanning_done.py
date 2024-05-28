import nmap
from urllib.parse import urlparse

def classify_vulnerability(port):
    high_vulnerability_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 465, 514, 587, 993, 995, 1433, 1521, 3306, 3389, 5432, 5900]
    medium_vulnerability_ports = [69, 123, 137, 161, 389, 514, 636, 2049, 3306, 5432]
    
    if port in high_vulnerability_ports:
        return "High"
    elif port in medium_vulnerability_ports:
        return "Medium"
    else:
        return "Low"

def scan_ports(target_host):
    try:
        # Initialize the port scanner
        nmScan = nmap.PortScanner()
        print("Scanning ports for:", target_host)
        
        # Scan the target host for all ports
        nmScan.scan(target_host)
        print("Scan results:", nmScan)
        
        # Check if any hosts are found
        if nmScan.all_hosts():
            # Print detailed scan results
            for host in nmScan.all_hosts():
                print('Host: %s' % host)
                print('State: %s' % nmScan[host].state())
                for proto in nmScan[host].all_protocols():
                    print('Protocol: %s' % proto)
                    ports = nmScan[host][proto].keys()
                    ports = sorted(ports)
                    if ports:
                        for port in ports:
                            vulnerability = classify_vulnerability(int(port))
                            print('Port: %s\tState: %s\tVulnerability: %s' % (port, nmScan[host][proto][port]['state'], vulnerability))
                    else:
                        print('No open ports found.')
        else:
            print("No hosts found.")
    except Exception as e:
        print("Error:", e)

def main():
    try:
        target_website = input("Enter the target website URL: ")
        
        # Extract hostname from URL
        parsed_url = urlparse(target_website)
        target_host = parsed_url.netloc
        
        # Call the scan_ports function
        scan_ports(target_host)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
