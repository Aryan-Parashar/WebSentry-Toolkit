import pyfiglet
import webbrowser

# Generate ASCII banner
ascii_banner = pyfiglet.figlet_format("GOOGLE DORK QUERY TARGETING")
print(ascii_banner)

queries = [
    "site:{domain} inurl:login",
    "site:{domain} intitle:index.of",
    "site:{domain} intext:password",
    "site:{domain} filetype:env",
    "site:{domain} ext:log",
    "site:{domain} ext:sql",
    "site:{domain} filetype:txt password",
    "site:{domain} ext:conf",
    "site:{domain} intitle:\"index of /\" passwd",
    "site:{domain} ext:txt | ext:log | ext:cfg | ext:yml",
    "site:{domain} intext:\"index of /\" | inurl:\"index of /\"",
    "site:{domain} inurl:wp-content",
    "site:{domain} ext:log",
    "site:{domain} ext:sql intext:insert into",
    "site:{domain} ext:swf",
    "site:{domain} filetype:sql",
    "site:{domain} filetype:sql password",
    "site:{domain} filetype:sql intext:password | pwd",
    "site:{domain} filetype:sql intext:@gmail.com",
    "site:{domain} filetype:sql intext:@hotmail.com",
    "site:{domain} filetype:sql intext:@yahoo.com",
    "site:{domain} filetype:sql intext:@aol.com",
    "site:{domain} filetype:sql intext:@msn.com",
    "site:{domain} filetype:sql intext:@rediff.com",
    "site:{domain} filetype:sql intext:username | uname",
    "site:{domain} filetype:sql intext:password",
    "site:{domain} filetype:sql intext:@gmail.com",
    "site:{domain} filetype:sql intext:@yahoo.com",
    "site:{domain} filetype:sql intext:@hotmail.com",
    "site:{domain} filetype:sql intext:@rediffmail.com",
    "site:{domain} filetype:sql intext:@rediff.com",
    "site:{domain} filetype:sql intext:@live.com",
    "site:{domain} filetype:sql intext:@outlook.com",
    "site:{domain} filetype:sql intext:@msn.com",
    "site:{domain} filetype:sql intext:password",
    "site:{domain} filetype:sql intext:username",
    "site:{domain} filetype:sql intext:passwd",
    "site:{domain} filetype:sql intext:pwd",
    "site:{domain} filetype:sql intext:email",
    "site:{domain} filetype:sql intext:e-mail",
    "site:{domain} filetype:sql intext:encrypted",
    "site:{domain} filetype:sql intext:enc_password",
    "site:{domain} filetype:sql intext:enctype",
    "site:{domain} filetype:sql intext:password",
    "site:{domain} filetype:sql intext:user",
    "site:{domain} filetype:sql intext:pass",
    "site:{domain} filetype:sql intext:passwd",
    "site:{domain} filetype:sql intext:word",
    "site:{domain} filetype:sql intext:username",
    "site:{domain} filetype:sql intext:pwd",
    "site:{domain} filetype:sql intext:admin",
    "site:{domain} filetype:sql intext:administrator",
    "site:{domain} filetype:sql intext:root",
    "site:{domain} filetype:sql intext:administrator",
    "site:{domain} filetype:sql intext:user",
    "site:{domain} filetype:sql intext:password",
    "site:{domain} filetype:sql intext:pass",
    "site:{domain} filetype:sql intext:passwd",
    "site:{domain} filetype:sql intext:word",
    "site:{domain} filetype:sql intext:username",
    "site:{domain} filetype:sql intext:pwd",
    "site:{domain} filetype:sql intext:admin",
    "site:{domain} filetype:sql intext:root",
    "site:{domain} filetype:sql intext:administrator",
    "site:{domain} inurl:/login.php",
    "site:{domain} inurl:/admin.php",
    "site:{domain} inurl:/login.jsp",
    "site:{domain} inurl:/admin.jsp",
    "site:{domain} inurl:/login.asp",
    "site:{domain} inurl:/admin.asp",
    "site:{domain} inurl:/login.html",
    "site:{domain} inurl:/admin.html",
    "site:{domain} inurl:/login.aspx",
    "site:{domain} inurl:/admin.aspx",
    "site:{domain} inurl:/admin.cgi",
    "site:{domain} inurl:/login.cgi",
    "site:{domain} inurl:/login",
    "site:{domain} inurl:/admin",
    "site:{domain} inurl:/user",
    "site:{domain} inurl:/users",
    "site:{domain} inurl:/moderator",
    "site:{domain} inurl:/moderators",
    "site:{domain} inurl:/adminlogin",
    "site:{domain} inurl:/admin-login",
    "site:{domain} inurl:/adminlogin.jsp",
    "site:{domain} inurl:/adminlogin.html",
    "site:{domain} inurl:/adminlogin.asp",
    "site:{domain} inurl:/adminLogin.jsp",
    "site:{domain} inurl:/adminLogin.html",
    "site:{domain} inurl:/adminLogin.asp",
    "site:{domain} inurl:/administratorlogin.jsp",
    "site:{domain} inurl:/administratorlogin.html",
    "site:{domain} inurl:/administratorlogin.asp",
    "site:{domain} inurl:/admin-login.jsp",
    "site:{domain} inurl:/admin-login.html",
    "site:{domain} inurl:/admin-login.asp",
    "site:{domain} inurl:/admin_panel",
    "site:{domain} inurl:/admin-panel",
    "site:{domain} inurl:/adminpanel",
    "site:{domain} inurl:/admincontrol",
    "site:{domain} inurl:/admin-control",
    "site:{domain} inurl:/admincontrol",
    "site:{domain} inurl:/adminLogin",
    "site:{domain} inurl:/admin_area",
    "site:{domain} inurl:/adminarea",
    "site:{domain} inurl:/admin-login",
    "site:{domain} inurl:/admin-area",
    "site:{domain} inurl:/admin",
    "site:{domain} inurl:/administrator",
    "site:{domain} inurl:/webadmin",
    "site:{domain} inurl:/web_admin",
    "site:{domain} inurl:/web-admin",
    "site:{domain} inurl:/web",
    "site:{domain} inurl:/wp-admin",
    "site:{domain} inurl:/wp-login",
    "site:{domain} inurl:/wp-login.php",
    "site:{domain} inurl:/admincp",
    "site:{domain} inurl:/admincp/login.asp",
    "site:{domain} inurl:/admincp/login.aspx",
    "site:{domain} inurl:/admincp/login.php",
    "site:{domain} inurl:/wp-admin",
    "site:{domain} inurl:/wp-login.php",
    "site:{domain} inurl:/administratorlogin",
    "site:{domain} inurl:/administratorlogin.jsp",
    "site:{domain} inurl:/administratorlogin.html",
    "site:{domain} inurl:/administratorlogin.asp",
    "site:{domain} inurl:/cpanel",
    "site:{domain} inurl:/login",
    "site:{domain} inurl:/login.php",
    "site:{domain} inurl:/login.jsp",
    "site:{domain} inurl:/login.html",
    "site:{domain} inurl:/login.asp",
    "site:{domain} inurl:/login.aspx",
    "site:{domain} inurl:/signin",
    "site:{domain} inurl:/signin.php",
    "site:{domain} inurl:/signin.jsp",
    "site:{domain} inurl:/signin.html",
    "site:{domain} inurl:/signin.asp",
    "site:{domain} inurl:/signin.aspx",
    "site:{domain} inurl:/sign_in",
    "site:{domain} inurl:/sign_in.php",
    "site:{domain} inurl:/sign_in.jsp",
    "site:{domain} inurl:/sign_in.html",
    "site:{domain} inurl:/sign_in.asp",
    "site:{domain} inurl:/sign_in.aspx",
    "site:{domain} inurl:/log_in",
    "site:{domain} inurl:/log_in.php",
    "site:{domain} inurl:/log_in.jsp",
    "site:{domain} inurl:/log_in.html",
    "site:{domain} inurl:/log_in.asp",
    "site:{domain} inurl:/log_in.aspx",
    "site:{domain} inurl:/register",
    "site:{domain} inurl:/register.php",
    "site:{domain} inurl:/register.jsp",
    "site:{domain} inurl:/register.html",
    "site:{domain} inurl:/register.asp",
    "site:{domain} inurl:/register.aspx",
    "site:{domain} inurl:/signup",
    "site:{domain} inurl:/signup.php",
    "site:{domain} inurl:/signup.jsp",
    "site:{domain} inurl:/signup.html",
    "site:{domain} inurl:/signup.asp",
    "site:{domain} inurl:/signup.aspx",
    "site:{domain} inurl:/subscribe",
    "site:{domain} inurl:/subscribe.php",
    "site:{domain} inurl:/subscribe.jsp",
    "site:{domain} inurl:/subscribe.html",
    "site:{domain} inurl:/subscribe.asp",
    "site:{domain} inurl:/subscribe.aspx",
    "site:{domain} inurl:/registration",
    "site:{domain} inurl:/registration.php",
    "site:{domain} inurl:/registration.jsp",
    "site:{domain} inurl:/registration.html",
    "site:{domain} inurl:/registration.asp",
    "site:{domain} inurl:/registration.aspx",
    "site:{domain} inurl:/create_account",
    "site:{domain} inurl:/create_account.php",
    "site:{domain} inurl:/create_account.jsp",
    "site:{domain} inurl:/create_account.html",
    "site:{domain} inurl:/create_account.asp",
    "site:{domain} inurl:/create_account.aspx",
    "site:{domain} inurl:/user",
    "site:{domain} inurl:/user.php",
    "site:{domain} inurl:/user.jsp",
    "site:{domain} inurl:/user.html",
    "site:{domain} inurl:/user.asp",
    "site:{domain} inurl:/user.aspx",
    "site:{domain} inurl:/users",
    "site:{domain} inurl:/users.php",
    "site:{domain} inurl:/users.jsp",
    "site:{domain} inurl:/users.html",
    "site:{domain} inurl:/users.asp",
    "site:{domain} inurl:/users.aspx",
    "site:{domain} inurl:/member",
    "site:{domain} inurl:/member.php",
    "site:{domain} inurl:/member.jsp",
    "site:{domain} inurl:/member.html",
    "site:{domain} inurl:/member.asp",
    "site:{domain} inurl:/member.aspx",
    "site:{domain} inurl:/members",
    "site:{domain} inurl:/members.php",
    "site:{domain} inurl:/members.jsp",
    "site:{domain} inurl:/members.html",
    "site:{domain} inurl:/members.asp",
    "site:{domain} inurl:/members.aspx",
    "site:{domain} inurl:/account",
    "site:{domain} inurl:/account.php",
    "site:{domain} inurl:/account.jsp",
    "site:{domain} inurl:/account.html",
    "site:{domain} inurl:/account.asp",
    "site:{domain} inurl:/account.aspx",
    "site:{domain} inurl:/accounts",
    "site:{domain} inurl:/accounts.php",
    "site:{domain} inurl:/accounts.jsp",
    "site:{domain} inurl:/accounts.html",
    "site:{domain} inurl:/accounts.asp",
    "site:{domain} inurl:/accounts.aspx",
]

def execute_dork_queries(urls):
    for i, url in enumerate(urls):
        webbrowser.open(url)
        print(f"Executing dork query {i + 1}: {url}")

def assign_vulnerability_metric(url):
    if "password" in url or "login" in url or "admin" in url:
        return "high"
    elif "index.of" in url or "env" in url:
        return "medium"
    else:
        return "low"

def main():
    domain = input("Enter your target domain (e.g., example.com): ").strip()
    urls = [f"https://www.google.com/search?q={query.replace('{domain}', domain)}" for query in queries]
    
    metrics = []
    for i, url in enumerate(urls):
        metric = assign_vulnerability_metric(url)
        metrics.append((f"GD{i + 1}", url, metric))
    
    for variable_name, url, metric in metrics:
        print(f"{variable_name}: {url} - Metric: {metric}")

    successful_payload = None
    successful_metric = None
    successful_variable = None
    
    for variable_name, url, metric in metrics:
        if webbrowser.open(url):  # Replace with actual check for successful injection
            successful_payload = url
            successful_metric = metric
            successful_variable = variable_name
            break

    if successful_payload:
        print(f"Successfully injected payload: {successful_payload}")
        print(f"Variable name: {successful_variable}")
        print(f"Vulnerability metric: {successful_metric}")
    else:
        print("No successful injection.")

if __name__ == "__main__":
    main()
