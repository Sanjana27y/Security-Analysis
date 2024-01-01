# csrf_checker/csrf_analyzer/csrf_checker.py
import requests
from bs4 import BeautifulSoup

def test_csrf(url):
    try:
        # Step 1: Send a GET request to the target URL
        response = requests.get(url)
        response.raise_for_status()

        # Step 2: Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 3: Look for anti-CSRF tokens in the HTML form(s)
        forms = soup.find_all('form')
        for form in forms:
            # Check if the form contains an anti-CSRF token (commonly named csrf_token)
            csrf_token_input = form.find('input', {'name': 'csrfmiddlewaretoken'})
            if csrf_token_input:
                csrf_token_value = csrf_token_input.get('value')
                # You may want to validate the CSRF token more thoroughly depending on the website
                if csrf_token_value:
                    # print(f"CSRF Token found in form: {url}")
                    return {'url': url, 'is_vulnerable': True, 'details': 'CSRF Token found in the path'}

        # If no CSRF token is found, consider it not vulnerable
        # print(f"No CSRF Token found in form: {url}")
        return {'url': url, 'is_vulnerable': False, 'details': ' No CSRF Token found in the path'}

    except requests.exceptions.RequestException as e:
        # print(f"Error accessing URL: {e}")
        return {'url': url, 'is_vulnerable': False, 'details': ' No CSRF Token found in the path'}

