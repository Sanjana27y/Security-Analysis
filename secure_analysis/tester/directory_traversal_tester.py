# import os

# def test_directory_traversal(tester_directory, requested_path):
#     # Convert the requested path to an absolute path
#     absolute_path = os.path.abspath(requested_path)
    
#     # Check if the requested path is within the tester directory
#     if os.path.commonprefix([tester_directory, absolute_path]) != tester_directory:
#         return True  # Directory traversal detected
#     return False  # No directory traversal



# ******************************************************************************# import requests
# from django.views.decorators.csrf import csrf_protect
# import os, requests


# @csrf_protect

# def test_directory_traversal(tester_directory, requested_path):
#     # Convert the requested path to an absolute path
#     absolute_path = os.path.abspath(requested_path)
    
#     # Check if the requested path is within the tester directory
#     if os.path.commonprefix([tester_directory, absolute_path]) != tester_directory:
#         return True  # Directory traversal detected
#     return False  # No directory traversal

# # Example usage:
# tester_directory = '/path/to/your/tester/directory'
# user_input_path = '/files/../important_file.txt'

# if test_directory_traversal(tester_directory, user_input_path):
#     print('Directory traversal detected!')
# else:
#     print('No directory traversal detected.')
# # ******************************************************************************
# def test_directory_traversal(url):
#     payloads = [
#         '../../../../etc/passwd',
#         '../../../../etc/hosts',
#         'http://www.owasp.org/malicioustxt'
#         # Add more payloads based on your knowledge of the system
#     ]

#     for payload in payloads:
#         test_url = f"{url}?file={payload}"
#         response = requests.get(test_url)

#         print(f"Testing: {test_url}")

#         if "root:" in response.text or "127.0.0.1.8000" in response.text:
#             print(f"Vulnerable to directory traversal: {test_url}")
#         else:
#             print(f"Not vulnerable to directory traversal: {test_url}")

# if __name__ == "__main__":
#     user_url = input("Enter the URL to test: ")
#     test_directory_traversal(user_url)

#  ********** writing this code on 20/12/23 7pm ************

# import urllib.parse

# def test_directory_traversal(url):
#     try:
#         # Parse the URL
#         parsed_url = urllib.parse.urlparse(url)

#         # Check for directory traversal in the path
#         if ".." in parsed_url.path:
#             return {'url': url, 'is_vulnerable': True, 'details': 'Directory traversal detected'}

#         # Check for directory traversal in query parameters
#         for param, value in urllib.parse.parse_qs(parsed_url.query).items():
#             if isinstance(value, list):
#                 value = value[0]  # Take the first value if it's a list
#             if ".." in value or "%2e%2e" in value:
#                 return {'url': url, 'is_vulnerable': True, 'details': f'Directory traversal detected in parameter: {param}'}

#         # No directory traversal detected
#         return {'url': url, 'is_vulnerable': False, 'details': 'No directory traversal detected'}

#     except Exception as e:
#         # Handle exceptions (e.g., invalid URL)
#         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}
import urllib.parse

def test_directory_traversal(url):
    try:
        # Parse the URL
        parsed_url = urllib.parse.urlparse(url)

        # Check for directory traversal in the path
        path_parts = parsed_url.path.split('/')
        if any(part in path_parts for part in ['..', '..', '..%c0%af', '..%c1%9c', '%2e%2e%2f', '%2e%2e/', '..%2f']):
            return {'url': url, 'is_vulnerable': True, 'details': 'Directory traversal detected in the path'}

        # Check for directory traversal in query parameters
        for param, value in urllib.parse.parse_qs(parsed_url.query).items():
            if isinstance(value, list):
                value = value[0]  # Take the first value if it's a list
            if any(part in value for part in ['..', '..', '..%c0%af', '..%c1%9c', '%2e%2e%2f', '%2e%2e/', '..%2f']):
                return {'url': url, 'is_vulnerable': True, 'details': f'Directory traversal detected in parameter: {param}'}

        # Check for absolute path traversal
        if any(part in parsed_url.path for part in ['/', '\\']):
            return {'url': url, 'is_vulnerable': True, 'details': 'Absolute path traversal detected in the path'}

        # Check for OS-specific patterns
        if any(part in parsed_url.path for part in ['/', '\\']) and any(part in parsed_url.path.lower() for part in [':', '%3a']):
            return {'url': url, 'is_vulnerable': True, 'details': 'OS-specific path traversal detected'}

        # No directory traversal detected
        return {'url': url, 'is_vulnerable': False, 'details': 'No directory traversal detected'}

    except Exception as e:
        # Handle exceptions (e.g., invalid URL)
        return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}


# import urllib.parse

# def test_directory_traversal(url):
#     try:
#         # Parse the URL
#         parsed_url = urllib.parse.urlparse(url)

#         # Check for directory traversal in the path
#         path_parts = parsed_url.path.split('/')
#         if any(part.startswith('..') or part.endswith('..') for part in path_parts):
#             return {'url': url, 'is_vulnerable': True, 'details': 'Directory traversal detected in the path'}

#         # Check for directory traversal in query parameters
#         for param, value in urllib.parse.parse_qs(parsed_url.query).items():
#             if isinstance(value, list):
#                 value = value[0]  # Take the first value if it's a list
#             if any(part.startswith('..') or part.endswith('..') for part in value.split('/')):
#                 return {'url': url, 'is_vulnerable': True, 'details': f'Directory traversal detected in parameter: {param}'}

#         # Check for OS-specific patterns
#         if any(part.startswith('/') or part.startswith('\\') for part in path_parts):
#             return {'url': url, 'is_vulnerable': True, 'details': 'OS-specific path traversal detected'}

#         # Check for absolute path traversal patterns (OWASP examples)
#         absolute_path_traversal_patterns = [
#             '/etc/passwd',
#             '/../../../../etc/shadow',
#             '../../../../some dir/some file',
#             '/var/www/html/get.php',
#             '/var/www/html/admin/get.inc',
#         ]
#         if any(pattern in parsed_url.path for pattern in absolute_path_traversal_patterns):
#             return {'url': url, 'is_vulnerable': True, 'details': 'Absolute path traversal detected'}

#         # No directory traversal detected
#         return {'url': url, 'is_vulnerable': False, 'details': 'No directory traversal detected'}

#     except Exception as e:
#         # Handle exceptions (e.g., invalid URL)
#         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}

# # Example usage:
# # user_url = "http://testsite.com/get.php?f=/var/www/html/get.php"
# # result = test_directory_traversal(user_url)
# # print(result)




