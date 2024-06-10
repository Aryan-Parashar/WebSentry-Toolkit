# WebSentry-Toolkit



WebSentry-Toolkit is a comprehensive collection of scripts designed to perform vulnerability assessments and penetration testing of web applications. This toolkit focuses on the OWASP Top 10 and works on an MITM attack model, providing a range of tests to identify and mitigate security issues.

## Features

- **Broken Access Controls**
- **Brute Force Attacks**
- **CSV Injection**
- **Cache Poisoning**
- **Client-side Template Injection**
- **Content Management System Disclosure**
- **Content Security Policy (CSP) Vulnerability Check**
- **Cookie Theft**
- **Cross-Origin Resource Sharing (CORS) Vulnerabilities**
- **Cross Site Scripting (XSS)**
- **Custom Header Vulnerabilities**
- **DOM Clobbering**
- **Directory Listing**
- **XSLT Injection**
- **Google Dork Queries**
- **HTML Injection**
- **HTML5 Cross-Origin Messaging**
- **HTTP Request Smuggling**
- **HTTP Security Headers Analysis**
- **Information Disclosure**
- **Insecure Authentication**
- **LaTeX Injection**
- **Local File Inclusion**
- **Missing Security Headers**
- **OS Command Injections**
- **Open Ports Scanning**
- **Open Redirection**
- **Parameter Pollution**
- **Path Traversal**
- **Potential Data Leakage**
- **Potential Debug Endpoints**
- **Potential Unencrypted Data**
- **Sensitive Data Exposure**
- **Server-Side Request Forgery (SSRF)**
- **Server-Side Template Injection**
- **Session Fixation**
- **Session Hijacking**
- **Spider Link Parameter Input**
- **SQL Injections SQLi**
- **Subdomain Analysis and Enumeration**
- **Unprotected API Endpoints**
- **Web Application Firewall Evasion**
- **XML External Entity (XXE) Injection**

## Installation

To use the WebSentry-Toolkit, clone the repository and install the necessary dependencies.

bash
git clone https://github.com/Aryan-Parashar/WebSentry-Toolkit.git
cd WebSentry-Toolkit
pip install -r requirements.txt

# Usage

Each script in the toolkit can be executed individually to test specific vulnerabilities. Below are examples and detailed workings of some specific scripts:

## Script: BrokenAccessControls_done.py

This script checks for broken access controls in a web application by attempting to access restricted resources without proper authorization.

### Steps Involved:

1. **Input URLs**: The script takes a list of URLs to test for broken access controls.
2. **Send Requests**: It sends HTTP requests to these URLs without proper authentication tokens.
3. **Analyze Responses**: The responses are analyzed to check if access is granted improperly.
4. **Log Findings**: Any URLs that allow unauthorized access are logged for further investigation.

## Script: CSVInjection_done.py

This script tests for CSV injection vulnerabilities by submitting malicious payloads in CSV file formats to web applications.

### Steps Involved:

1. **Input Data**: The script takes a list of input fields to test for CSV injection.
2. **Send Malicious Payloads**: It submits payloads designed to exploit CSV injection vulnerabilities.
3. **Analyze Responses**: The responses are checked to see if the payloads executed as commands.
4. **Log Findings**: Any vulnerabilities found are logged for further action.

## References for Payloads

### Broken Access Controls

- OWASP SQL Injection
- OWASP XSS
- OWASP Command Injection
- OWASP Path Traversal
- OWASP Broken Authentication
- OWASP Sensitive Data Exposure
- OWASP CSRF
- OWASP Insecure Deserialization
- OWASP Security Misconfiguration
- OWASP XXE
- OWASP Insecure Direct Object References
- OWASP SSRF
- OWASP File Upload
- OWASP Session Fixation
- OWASP Clickjacking
- OWASP CORS
- OWASP Unvalidated Redirects and Forwards
- OWASP CSP
- OWASP HTTP Parameter Pollution
- OWASP Server Side Template Injection
- OWASP Cross-Site Script Inclusion
- OWASP Code Injection
- OWASP XML Injection
- OWASP File Inclusion
- OWASP Session Hijacking
- OWASP Brute Force Attack
- OWASP LDAP Injection

### Cache Poisoning

- OWASP Secure Headers
- MDN HTTP Headers
- RFC 7234
- Akamai Blog on Cache Poisoning
- PortSwigger Web Security Academy
- Practical Web Cache Poisoning
- Imperva on Cache Poisoning Attacks

### Open Ports

- Netwrix Blog on Open Port Vulnerabilities

### Google Dork Queries

- GHD - Google Hacking Database

### CRLF Injection

- OWASP Testing Guide: CRLF Injection
- PayloadsAllTheThings - CRLF Injection
- PortSwigger Web Security Academy
- Exploit Database
- PayloadBox XSS Payload List

### Additional References

- HackTricks - XSLT Server-Side Injection
- Awesome WAF
- HackTricks - Web API Pentesting
- PayloadBox SSTI Payloads
- SSRF Testing
- Command Injection Payload List
- LaTeX Injection Payloads
- Offensive Payloads - HTML Injection Payloads

