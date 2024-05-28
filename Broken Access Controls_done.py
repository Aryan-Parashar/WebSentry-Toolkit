import subprocess

def perform_security_tests(url):
    print("[*] Performing security tests for:", url)

    # Defining security test commands
    security_commands = [
        "curl -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X POST -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X PUT -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X OPTIONS -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X TRACE -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X HEAD -s -o /dev/null -w '%{http_code}' " + url,
        "curl -X CONNECT -s -o /dev/null -w '%{http_code}' " + url,
        "wget -q --method=HEAD -O /dev/null " + url,
        "nc -z -v " + url + " 80",
        "sqlmap -u " + url + " --batch --random-agent",
        "nmap -p 1-65535 " + url,
        "nikto -h " + url,
        "dirb " + url,
        "wpscan --url " + url,
        "gobuster dns -d " + url + " -w /usr/share/wordlists/dirbuster/dns-Jhaddix.txt",
        "amass enum -d " + url,
        "wfuzz -c --hc 404 -w /usr/share/wordlists/wfuzz/general/common.txt " + url + "/FUZZ",
        "hydra -L /usr/share/wordlists/metasploit/http_default_userpass.txt -P /usr/share/wordlists/metasploit/http_default_pass.txt " + url + " http-get /",
        "git clone --recursive " + url,
        "svn checkout " + url,
        "testssl.sh " + url,
        "nikto -host " + url,
        "uniscan -u " + url + " -qweds",
        "whatweb " + url,
        "dotdotpwn -m http -h " + url,
        "sslscan --no-failed " + url,
        "nmap -sV --script=banner " + url,
        "nmap --script=http-enum " + url,
        "sqlmap -u " + url + " --forms --batch --random-agent",
        "nikto -host " + url + " -Tuning 10",
        "dirsearch -u " + url + " -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -e html,php,asp,aspx,jsp,do,action,xml",
        "wafw00f " + url,
        "nuclei -target " + url + " -t /path/to/nuclei-templates",
        "snmp-check " + url,
        "smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/unix_users.txt -t " + url,
        "ike-scan " + url,
        "sqlmap -u " + url + " --forms --batch --random-agent",
        "sqlmap -u " + url + " --crawl=1",
        "nmap -sV --version-intensity 5 " + url,
        "nmap --script=http-methods " + url,
        "nikto -host " + url + " -ssl",
        "sslscan --no-failed --http " + url,
        "nmap -sV --script=http-headers " + url,
        "gobuster dir -u " + url + " -w /usr/share/wordlists/dirb/common.txt",
        "gobuster dir -u " + url + " -w /usr/share/wordlists/dirb/common.txt -x php,html,txt",
        "wpscan --url " + url + " --enumerate ap",
        "wpscan --url " + url + " --enumerate vp",
        "nikto -host " + url + " -Tuning 10",
        "nikto -host " + url + " -Plugins -ssl",
        "nikto -host " + url + " -Plugins +auth",
        "nikto -host " + url + " -Plugins +vuln",
        "nikto -host " + url + " -Plugins +xss",
        "dirsearch -u " + url + " -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 100",
        "nuclei -target " + url + " -t /path/to/nuclei-templates -severity high,medium",
        "nuclei -target " + url + " -t /path/to/nuclei-templates -severity critical",
        "nmap --script=http-security-headers " + url,
        "smtp-user-enum -M RCPT -U /usr/share/wordlists/metasploit/unix_users.txt -t " + url,
        "smtp-user-enum -M EXPN -U /usr/share/wordlists/metasploit/unix_users.txt -t " + url,
        "ike-scan -A " + url
    ]

    # Defining vulnerabilities for each payload
    vulnerabilities = {
        "BAC1": "SQL Injection High vulnerability",
        "BAC2": "Cross-Site Scripting (XSS) Medium vulnerability",
        "BAC3": "Command Injection High vulnerability",
        "BAC4": "Directory Traversal Medium vulnerability",
        "BAC5": "Broken Authentication High vulnerability",
        "BAC6": "Sensitive Data Exposure High vulnerability",
        "BAC7": "Cross-Site Request Forgery (CSRF) Medium vulnerability",
        "BAC8": "Insecure Deserialization High vulnerability",
        "BAC9": "Security Misconfiguration High vulnerability",
        "BAC10": "XML External Entity (XXE) Injection High vulnerability",
        "BAC11": "Access Control Vulnerability Medium vulnerability",
        "BAC12": "Server-Side Request Forgery (SSRF) High vulnerability",
        "BAC13": "File Upload Vulnerability Medium vulnerability",
        "BAC14": "Session Fixation Medium vulnerability",
        "BAC15": "Clickjacking Medium vulnerability",
        "BAC16": "Cross-Origin Resource Sharing (CORS) Misconfiguration Medium vulnerability",
        "BAC17": "Unvalidated Redirects and Forwards Medium vulnerability",
        "BAC18": "Content Security Policy (CSP) Bypass Medium vulnerability",
        "BAC19": "HTTP Parameter Pollution (HPP) Medium vulnerability",
        "BAC20": "Server-Side Template Injection (SSTI) High vulnerability",
        "BAC21": "Insecure Direct Object Reference (IDOR) High vulnerability",
        "BAC22": "Cross-Site Script Inclusion (XSSI) Medium vulnerability",
        "BAC23": "Remote Code Execution (RCE) High vulnerability",
        "BAC24": "XML Injection Medium vulnerability",
        "BAC25": "Server-Side Request Forgery (SSRF) High vulnerability",
        "BAC26": "File Inclusion Vulnerability Medium vulnerability",
        "BAC27": "Session Hijacking High vulnerability",
        "BAC28": "Brute Force Attack Medium vulnerability",
        "BAC29": "LDAP Injection High vulnerability",
        "BAC30": "Cross-Site Script Inclusion (XSSI) Medium vulnerability"
    }
    

    # Initializes variables for successful payload and its vulnerability
    successful_payload = None
    vulnerability_metric = None

    # Performing security tests
    for command, payload in zip(security_commands, vulnerabilities.keys()):
        print("Command:", command)
        result = subprocess.run(command, shell=True)
        if result.returncode == 0:
            print("Payload {} executed successfully. Vulnerability: {}".format(payload, vulnerabilities[payload]))
            successful_payload = payload
            vulnerability_metric = vulnerabilities[payload]

    # Prints the successful payload along with its vulnerability metric
    if successful_payload:
        print("Successful Payload:", successful_payload)
        print("Vulnerability Metric:", vulnerability_metric)
    else:
        print("No payload executed successfully.")

# URL Input Command
target_url = input("Enter the target website URL: ")

# Performing security tests
perform_security_tests(target_url)

