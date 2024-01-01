import requests
from urllib.parse import urlparse

def test_security_misconfigurations(url):
    try:
        # Send an HTTP GET request to get server headers
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        response.raise_for_status()

        # Check Server Header
        server_header = response.headers.get('Server')
        if server_header:
            return {'url': url, 'is_vulnerable': False, 'details': f"The server header is exposed: {server_header}"}

        # Check X-Frame-Options Header
        x_frame_options = response.headers.get('X-Frame-Options')
        if not x_frame_options or x_frame_options.lower() not in ['deny', 'sameorigin']:
            return {'url': url, 'is_vulnerable': False, 'details': "The X-Frame-Options header is not set correctly or not present"}

        # Add more checks for other security misconfigurations as needed

        # If no misconfigurations are detected
        return {'url': url, 'is_vulnerable': True, 'details': 'No security misconfigurations detected'}

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network error)
        return {'url': url, 'is_vulnerable': False, 'details': f'Error: {e}'}

# # Example usage
# user_url = "https://example.com"  # Replace with the user-provided URL
# result = test_security_misconfigurations(user_url)
# print(f"Security checks for URL: {user_url}")
# print(f"Vulnerability: {result['is_vulnerable']}")
# print(f"Details: {result['details']}")


# import requests
# from urllib.parse import urlparse

# def get_domain(url):
#     return urlparse(url).netloc

# def get_server_headers(url):
#     try:
#         response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
#         return response.headers
#     except requests.exceptions.RequestException as e:
#         return None

# def check_server_header(url):
#     headers = get_server_headers(url)
#     if headers:
#         server_header = headers.get('Server')
#         if server_header:
#             return False, f"The server header is exposed: {server_header}"
#     return True, None

# def check_x_frame_options(url):
#     headers = get_server_headers(url)
#     if headers:
#         x_frame_options = headers.get('X-Frame-Options')
#         if not x_frame_options or x_frame_options.lower() not in ['deny', 'sameorigin']:
#             return False, "The X-Frame-Options header is not set correctly or not present"
#     return True, None

# def test_security_misconfigurations(url):
#     try:
#         # Check Server Header
#         server_header = get_server_headers(url).get('Server')
#         if server_header:
#             return {'url': url, 'is_vulnerable': False, 'details': f"The server header is exposed: {server_header}"}

#         # Check X-Frame-Options Header
#         x_frame_options = get_server_headers(url).get('X-Frame-Options')
#         if not x_frame_options or x_frame_options.lower() not in ['deny', 'sameorigin']:
#             return {'url': url, 'is_vulnerable': False, 'details': "The X-Frame-Options header is not set correctly or not present"}

#         # If no misconfigurations are detected
#         return {'url': url, 'is_vulnerable': True, 'details': 'No security misconfigurations detected'}

#     except requests.exceptions.RequestException as e:
#         # Handle request exceptions (e.g., connection error)
#         return {
#             'url': url,
#             'is_vulnerable': False,
#             'details': f'Error during security misconfigurations test: {str(e)}'
#         }

# # if __name__ == "__main__":
# #     # Example usage
# #     user_url = "https://www.example.com"  # Replace with the user-provided URL
# #     result = test_security_misconfigurations(user_url)
# #     print(f"Security checks for URL: {user_url}")
# #     print(f"Is Vulnerable: {result['is_vulnerable']}")
# #     print(f"Details: {result['details']}")




# # import requests
# # from urllib.parse import urlparse

# # def get_domain(url):
# #     return urlparse(url).netloc

# # def get_server_headers(url):
# #     try:
# #         response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
# #         return response.headers
# #     except requests.exceptions.RequestException as e:
# #         return None

# # def check_server_header(url):
# #     headers = get_server_headers(url)
# #     if headers:
# #         server_header = headers.get('Server')
# #         if server_header:
# #             return False, f"The server header is exposed: {server_header}"
# #     return True, None

# # def check_x_frame_options(url):
# #     headers = get_server_headers(url)
# #     if headers:
# #         x_frame_options = headers.get('X-Frame-Options')
# #         if not x_frame_options or x_frame_options.lower() not in ['deny', 'sameorigin']:
# #             return False, "The X-Frame-Options header is not set correctly or not present"
# #     return True, None

# # # def check_custom_security_settings(url):
# # #     # Add your custom security checks here
# # #     # Example: Check for specific security headers or configurations
# # #     # Return False and a message if the check fails

# # #     # Sample custom check (modify or add more checks as needed)
# # #     custom_header = get_server_headers(url).get('Custom-Security-Header')
# # #     if not custom_header:
# # #         return False, "Custom security header is missing"
    
# # #     return True, None

# # def test_security_misconfigurations(url):
# #     try:
# #         # Send an HTTP GET request to get server headers
# #         response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
# #         response.raise_for_status()

# #         # Check Server Header
# #         server_header = response.headers.get('Server')
# #         if server_header:
# #             return {'url': url, 'is_vulnerable': False, 'details': f"The server header is exposed: {server_header}"}

# #         # Check X-Frame-Options Header
# #         x_frame_options = response.headers.get('X-Frame-Options')
# #         if not x_frame_options or x_frame_options.lower() not in ['deny', 'sameorigin']:
# #             return {'url': url, 'is_vulnerable': False, 'details': "The X-Frame-Options header is not set correctly or not present"}

# #         # Add more checks for other security misconfigurations as needed

# #         # If no misconfigurations are detected
# #         return {'url': url, 'is_vulnerable': True, 'details': 'No security misconfigurations detected'}

# #     except requests.exceptions.RequestException as e:
# #         # Handle exceptions (e.g., network error)
# #         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}

# #         # Your existing code for sending an HTTP GET request
# #         # ...

# #         # Check for security misconfigurations
# #         checks = [check_server_header, check_x_frame_options]
# #         results = {}
# #         for check in checks:
# #             is_secure, message = check(url)
# #             results[check.__name__] = is_secure, message
# #         return results

# #     except requests.exceptions.RequestException as e:
# #         # Handle request exceptions (e.g., connection error)
# #         return {
# #             'url': url,
# #             'error': f'Error during security misconfigurations test: {str(e)}'
# #         }

# # # if __name__ == "__main__":
# # #     # Example usage
# # #     user_url = "https://www.example.com"  # Replace with the user-provided URL
# # #     result = test_security_misconfigurations(user_url)
# # #     print(f"Security checks for URL: {user_url}")
# # #     for check, (is_secure, message) in result.items():
# # #         print(f"{check}: {is_secure} {'(' + message + ')' if message else ''}")
