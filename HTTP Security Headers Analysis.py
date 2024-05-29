import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HTTP SECURITY HEADER ANALYSIS")
print(ascii_banner)

def analyze_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n[*] Analyzing {url}")

        print("\n[*] Retrieved Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")

        vulnerability_detected = False

        # Dictionary containing recommended security headers and values
        security_headers = {
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "SAMEORIGIN",
            "X-XSS-Protection": "1; mode=block",
            "Content-Security-Policy": "default-src 'self';",
            "Referrer-Policy": "no-referrer",
            "Feature-Policy": "geolocation 'self'; midi 'none'; sync-xhr 'self'",
            "Expect-CT": "max-age=86400, enforce",
            "Permissions-Policy": "geolocation=(self), microphone=()",
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "Surrogate-Control": "no-store",
            "X-Download-Options": "noopen",
            "X-Permitted-Cross-Domain-Policies": "none",
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Embedder-Policy": "require-corp",
            "Cross-Origin-Resource-Policy": "same-origin",
            "Content-Type": "text/html; charset=UTF-8",
            "Content-Language": "en",
            "Content-DPR": "1.0",
            "Content-Encoding": "gzip",
            "Content-Security-Policy-Report-Only": "default-src 'self';",
            "Timing-Allow-Origin": "*",
            "X-DNS-Prefetch-Control": "off",
            "Report-To": "{\"group\":\"default\",\"max_age\":31536000,\"endpoints\":[{\"url\":\"https://example.com/report\"}],\"include_subdomains\":true}",
            "NEL": "{\"report_to\":\"default\",\"max_age\":31536000,\"include_subdomains\":true}",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
            "Access-Control-Expose-Headers": "Content-Length,Content-Range",
            "Public-Key-Pins": "pin-sha256=\"base64+primary==\"; pin-sha256=\"base64+backup==\"; max-age=5184000; includeSubDomains",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
            "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; object-src 'none';",
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "X-XSS-Protection": "1; mode=block",
            "Expect-CT": "max-age=86400, enforce, report-uri=\"https://example.com/report\"",
            "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Feature-Policy": "fullscreen 'self'; payment 'none'",
            "Clear-Site-Data": "\"cache\", \"cookies\", \"storage\", \"executionContexts\"",
            "Cross-Origin-Resource-Policy": "same-site",
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Embedder-Policy": "require-corp"
        }

        # Check for missing or misconfigured security headers
        for header, recommended_value in security_headers.items():
            if header not in headers:
                print(f"\n[!] Missing security header: {header}")
                vulnerability_detected = True
            elif headers[header] != recommended_value:
                print(f"\n[!] Misconfigured security header: {header}. Recommended: {recommended_value}")
                vulnerability_detected = True
        
        if not vulnerability_detected:
            print("\n[+] No missing or misconfigured security headers found. The website seems well-protected.")
        else:
            print("\n[-] The website might be vulnerable to HTTP Security Headers Misconfiguration.")
            print("\n[!] Recommendations:")
            print("- Consider adding or updating the missing or misconfigured security headers.")
            print("- Adhere to security best practices to mitigate common web vulnerabilities.")
            print("- Regularly review and adjust security configurations.")

    except requests.RequestException as e:
        print(f"\n[!] An error occurred: {str(e)}")

def main():
    # Prompt user for target website URL
    target_url = input("Enter the URL of the website you want to analyze: ").strip()
    # Check if the URL starts with 'http://' or 'https://'
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url

    # Analyze the security headers
    analyze_security_headers(target_url)

if __name__ == "__main__":
    main()
