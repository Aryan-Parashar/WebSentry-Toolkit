import asyncio
import aiohttp
import dns.asyncresolver
from colorama import Fore, Style
import pyfiglet
import sublist3r

ascii_banner = pyfiglet.figlet_format("SUBDOMAIN ANALYSIS ENUMERATIONS")
print(ascii_banner)

async def sublist3r_enum(domain):
    try:
        subdomains = await sublist3r.main(domain, 40, None, engines=None, ports=None, silent=True, verbose=False, enable_bruteforce=False)
        print(f"{Fore.GREEN}Subdomains discovered using Sublist3r:{Style.RESET_ALL}")
        for subdomain in subdomains:
            print(subdomain)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

async def crt_sh_enum(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    subdomains = set()
                    for entry in data:
                        name_value = entry['name_value']
                        subdomains.add(name_value)
                    print(f"{Fore.GREEN}Subdomains discovered using crt.sh:{Style.RESET_ALL}")
                    for subdomain in subdomains:
                        print(subdomain)
                else:
                    print(f"{Fore.RED}Failed to fetch data from crt.sh{Style.RESET_ALL}")
    except aiohttp.ClientError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

async def dns_enum(domain):
    resolver = dns.asyncresolver.Resolver()
    try:
        answers = await resolver.resolve(domain, 'A')
        print(f"{Fore.GREEN}Subdomains discovered via DNS resolution:{Style.RESET_ALL}")
        for rdata in answers:
            print(rdata)
    except Exception as e:
        print(f"{Fore.RED}Error during DNS resolution: {e}{Style.RESET_ALL}")

async def main():
    domain = input("Enter the target domain (without 'https://www.'): ").strip()
    print("\nInitiating subdomain enumeration...\n")

    await sublist3r_enum(domain)
    await crt_sh_enum(domain)
    await dns_enum(domain)

if __name__ == "__main__":
    asyncio.run(main())
