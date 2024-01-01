# sql_injection_detector.py
# sqli_tester.py
# import subprocess
# import os

# def test_sqli(url):
#     # Adjust this function based on your SQL injection testing logic
#     # For simplicity, we'll use SQLmap for demonstration purposes

#     sqlmap_path = os.path.join('C:', 'Users', 'yeluk', 'Desktop', 'drdo 7', 'secure_analysis', 'tester', 'sqlmap.py')
    
#     # Run SQLmap command and capture the output
#     output = subprocess.check_output(['python2.7', sqlmap_path, '-u', url])

#     # Process the SQLmap output to determine vulnerability
#     is_sqli_vulnerable = b"sql injection" in output.lower()

#     return {'is_vulnerable': is_sqli_vulnerable}



# import subprocess

# def test_sqli(url):
#     try:
#         output = subprocess.check_output(['pwd'])
#         print(output)
#         return "sql injection" in output.lower()
#     except subprocess.CalledProcessError:
#         return False



# # import requests

# # def test_sqli_vulnerability(url):
# #     # Basic SQL injection payload
# #     payload = "' OR '1'='1' -- "

# #     # Construct the URL with the SQL injection payload
# #     target_url = f"{url}?parameter={payload}"

# #     try:
# #         # Send the GET request
# #         response = requests.get(target_url)

# #         # Check if the response contains an indication of a successful injection
# #         if "success" in response.text.lower():
# #             return {'url': url, 'is_vulnerable': True, 'details': 'SQL injection vulnerability detected'}
# #         else:
# #             return {'url': url, 'is_vulnerable': False, 'details': 'No SQL injection vulnerability detected'}
    
# #     except requests.exceptions.RequestException as e:
# #         # Handle exceptions (e.g., network error)
# #         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}

# # # Example usage:
# # # user_url = "https://www.example.com"  # Replace with the user-provided URL
# # # result = test_sqli_vulnerability(user_url)
# # # print(f"SQL Injection test for URL: {user_url}")
# # # print(f"Is Vulnerable: {result['is_vulnerable']}")
# # # print(f"Details: {result['details']}")
