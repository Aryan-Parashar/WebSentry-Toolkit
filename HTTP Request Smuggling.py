import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HTTP REQUEST SMUGGLING")
print(ascii_banner)

def check_http_request_smuggling(url):
    print(f"[*] Checking for HTTP Request Smuggling vulnerability on: {url}")

    try:
        # Send a GET request to the target website
        response = requests.get(url)
        if response.status_code != 200:
            print("[!] Error: Failed to fetch the target website.")
            return "medium"

        print("[*] Initial response headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Crafted request to test for smuggling vulnerability
        smuggling_request = f"GET / HTTP/1.1\r\nHost: {url.split('//')[1].split('/')[0]}\r\nContent-Length: 0\r\nTransfer-Encoding: chunked\r\nContent-Length: 3\r\n\r\nF\r\n0\r\n\r\n"
        print("[*] Sending crafted request:")
        print(smuggling_request)

        # Send the crafted request and analyze the response
        crafted_response = requests.post(url, headers={"Content-Length": "31"}, data=smuggling_request)
        if crafted_response.status_code != 200:
            print("[!] Error: Failed to send crafted request.")
            return "medium"

        print("[*] Crafted response headers:")
        for header, value in crafted_response.headers.items():
            print(f"{header}: {value}")

        # Check if the target is vulnerable
        if response.headers.get("Content-Length") == crafted_response.headers.get("Content-Length"):
            print("[+] Potential HTTP Request Smuggling vulnerability detected!")
            print("[*] To exploit this vulnerability, consider sending a request with a smuggling payload.")
            print("[!] Mitigations:")
            print("- Ensure proper parsing of headers and body in the same order on both the front-end and back-end servers.")
            print("- Use security mechanisms such as WAF (Web Application Firewall) to detect and block such malformed requests.")
            print("- Regularly update and patch web server software to fix known vulnerabilities.")
            return "high"
        else:
            print("[-] No HTTP Request Smuggling vulnerability detected.")
            return "low"

    except Exception as e:
        print(f"[!] Error: {str(e)}")
        return "medium"

def main():
    # Prompt user for target website URL
    target_url = input("Enter your target website URL: ").strip()
    # Check if the URL starts with 'http://' or 'https://'
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url

    # Analyze the vulnerability
    vulnerability_level = check_http_request_smuggling(target_url)
    print(f"Vulnerability Level: {vulnerability_level.upper()}")

if __name__ == "__main__":
    main()
