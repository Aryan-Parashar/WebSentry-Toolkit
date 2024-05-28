import requests
from bs4 import BeautifulSoup
import re

# Function to check for CMS Information Disclosure Vulnerabilities
def check_cms_info_disclosure(target_url):
    try:
        print("\n[*] Testing for CMS Information Disclosure Vulnerabilities on:", target_url)
        
        # Fetching the website content
        response = requests.get(target_url)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Parsing the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Finding meta generator tag
            meta_generator = soup.find('meta', {'name': re.compile(r'generator', re.I)})
            
            if meta_generator:
                print("\n[*] Found meta generator tag:")
                print(meta_generator)
                print("\n[!] The website may be disclosing CMS information.")
                print("\n[*] To test this vulnerability, try accessing the following URLs:")
                
                # Define payloads
                payloads = [
                    ("/wp-admin", "CMSD1", "high"),
                    ("/administrator", "CMSD2", "high"),
                    ("/admin", "CMSD3", "medium"),
                    ("/wp-login.php", "CMSD4", "high"),
                    ("/wp-admin/install.php", "CMSD5", "high"),
                    ("/readme.html", "CMSD6", "low"),
                    ("/license.txt", "CMSD7", "low"),
                    ("/install.php", "CMSD8", "medium"),
                    ("/update.php", "CMSD9", "medium"),
                    ("/upgrade.php", "CMSD10", "medium"),
                    ("/includes", "CMSD11", "medium"),
                    ("/core", "CMSD12", "medium"),
                    ("/changelog.txt", "CMSD13", "low"),
                    ("/user/login", "CMSD14", "high"),
                    ("/user/register", "CMSD15", "medium"),
                    ("/config", "CMSD16", "medium"),
                    ("/config.php", "CMSD17", "high"),
                    ("/config.inc.php", "CMSD18", "high"),
                    ("/config.old", "CMSD19", "medium"),
                    ("/config.bak", "CMSD20", "medium"),
                    ("/config.backup", "CMSD21", "medium"),
                    ("/admin/login.php", "CMSD22", "high"),
                    ("/admin/index.php", "CMSD23", "medium"),
                    ("/admin.php", "CMSD24", "medium"),
                    ("/admin/admin.php", "CMSD25", "medium"),
                    ("/cms", "CMSD26", "medium"),
                    ("/admin/cms", "CMSD27", "medium"),
                    ("/admin/cms.php", "CMSD28", "medium"),
                    ("/phpinfo.php", "CMSD29", "high"),
                    ("/info.php", "CMSD30", "high"),
                    ("/phpmyadmin", "CMSD31", "high"),
                    ("/backup", "CMSD32", "medium"),
                    ("/backup.zip", "CMSD33", "medium"),
                    ("/backup.tar", "CMSD34", "medium"),
                    ("/backup.tar.gz", "CMSD35", "medium")
                ]
                
                # Check each payload
                for payload, var_name, metric in payloads:
                    print(f"\n[*] Testing payload {var_name} ({payload}) with metric {metric}...")
                    test_url = target_url.rstrip('/') + payload
                    test_response = requests.get(test_url)
                    if test_response.status_code == 200:
                        print(f"[+] Payload {var_name} injected successfully: {test_url}")
                        print(f"[*] Vulnerability Metric: {metric}")
                        return var_name, payload, metric
                    else:
                        print(f"[-] Payload {var_name} failed: {test_url}")
                print("\n[*] No successful payload found.")
            else:
                print("\n[*] No meta generator tag found. The website does not seem to disclose CMS information.")
        else:
            print("\n[!] Failed to retrieve website content. Status Code:", response.status_code)
    except Exception as e:
        print("\n[!] An error occurred:", str(e))

# Main function
def run_cms_info_disclosure_test():
    print("**CMS Information Disclosure Vulnerability Tester**\n")
    target_url = input("Enter your target website URL: ")
    
    if target_url:
        result = check_cms_info_disclosure(target_url)
        if result:
            var_name, payload, metric = result
            print(f"\nSuccessfully injected payload: {var_name} ({payload}) with vulnerability metric: {metric}")
        else:
            print("\nNo successful payload injection detected.")

# Execute the main function
if __name__ == "__main__":
    run_cms_info_disclosure_test()
