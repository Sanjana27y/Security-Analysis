import requests
from bs4 import BeautifulSoup

xss_results = []

def test_xss(url):
    # Step 1: Fetch the HTML content of the given URL
    response = requests.get(url)
    html_content = response.text
    
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Step 3: Find all input fields, attributes, and scripts in the HTML
    input_fields = soup.find_all('input')
    attributes = soup.find_all(lambda tag: tag.attrs)
    scripts = soup.find_all('script')
    
    # Step 4: Check for potential XSS vulnerabilities in input fields
    
    for input_field in input_fields:
        input_value = input_field.get('value')
        
        # Check for potential XSS in input values
        if input_value and '<script>' in input_value:
            xss_results.append({
                'field': str(input_field),
                'value': input_value,
                'location': 'input field'
            })
    
    # Step 5: Check for potential XSS vulnerabilities in attributes
    for attribute in attributes:
        for attr_name, attr_value in attribute.attrs.items():
            # Check for potential XSS in attribute values
            if '<script>' in attr_value:
                xss_results.append({
                    'field': str(attribute),
                    'value': attr_value,
                    'location': f'attribute: {attr_name}'
                })
    
    # Step 6: Check for potential XSS vulnerabilities in script tags
    for script in scripts:
        script_content = str(script.string)
        
        # Check for potential XSS in script content
        if '<script>' in script_content:
            xss_results.append({
                'field': str(script),
                'value': script_content,
                'location': 'script tag content'
            })

    # Step 7: Return the list of potential XSS vulnerabilities
    return xss_results

# # Example usage:
# url_to_test = 'https://example.com'
# results = detect_xss(url_to_test)

# if results:
#     print(f'Potential XSS vulnerabilities found in {url_to_test}:')
#     for vulnerability in results:
#         print(f'Location: {vulnerability["location"]}')
#         print(f'Field: {vulnerability["field"]}')
#         print(f'Value: {vulnerability["value"]}')
#         print('-' * 30)
# else:
#     print(f'No potential XSS vulnerabilities found in {url_to_test}')



#import os
# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup as bs
# from urllib.parse import urljoin

# def get_all_forms(url):
#     soup = bs(requests.get(url).content, "html.parser")
#     return soup.find_all("form")

# def get_form_details(form):
#     details = {}
#     action = form.attrs.get("action").lower()
#     method = form.attrs.get("method", "get").lower()
#     inputs = []
#     for input_tag in form.find_all("input"):
#         input_type = input_tag.attrs.get("type", "text")
#         input_name = input_tag.attrs.get("name")
#         inputs.append({"type": input_type, "name": input_name})
#     details["action"] = action
#     details["method"] = method
#     details["inputs"] = inputs
#     return details

# def submit_form(form_details, url, value):
#     target_url = urljoin(url, form_details["action"])
#     inputs = form_details["inputs"]
#     data = {}
#     for input in inputs:
#         if input["type"] == "text" or input["type"] == "search":
#             input["value"] = value
#             input_name = input.get("name")
#             input_value = input.get("value")
#             if input_name and input_value:
#                 data[input_name] = input_value
#         if form_details["method"] == "post":
#             return requests.post(target_url, data=data)
#         return requests.get(target_url, params=data)
    
# def scan_xss(url):
#     forms = get_all_forms(url)
#     print(f"[+] Detected {len(forms)} forms on {url}.")
#     for form in forms:
#         form_details = get_form_details(form)
#         for payload in xss_payloads:
#             response = submit_form(form_details, url, payload)
#             if payload in response.content.decode():
#                 print( f"[!] XSS Detected on {url}")
#                 print( f"[*] Form details:")
#                 pprint(form_details)
#                 break



# import requests
# from pprint import pprint
# from django.http import request as django_request
# from bs4 import BeautifulSoup as bs
# from urllib.parse import urljoin
# # from .beautifulsoup import get_all_forms, get_form_details, submit_form
# # In xss_tester.py
# from .beautifulsoup import get_all_forms, get_form_details, submit_form

# def test_xss(url):
#     # """
#     # Given a `url`, it prints all XSS vulnerable forms and 
#     # returns True if any is vulnerable, False otherwise
#     # """
#     # get all the forms from the URL
#     forms = get_all_forms(url)
#     print(f"[+] Detected {len(forms)} forms on {url}.")
    
#     js_script = "<script>alert('hi')</script>"
    
#     # returning value
#     is_vulnerable = False
    
#     # iterate over all forms
#     for form in forms:
#         form_details = get_form_details(form)
        
#         # Check for XSS vulnerability
#         if test_xss_vulnerability(form_details, url, js_script):
#             print(f"[+] XSS Detected on {url}")
#             print("[*] Form details:")
#             pprint(form_details)
#             is_vulnerable = True
#             # won't break because we want to print available vulnerable forms
    
#     return is_vulnerable

# def test_xss_vulnerability(form_details, url, payload):
#     # """
#     # Test a specific form for XSS vulnerability
#     # """
#     # Submit the form with the XSS payload
#     response = submit_form(form_details, url, payload)
    
#     if response is not None:
#         # Decode the content to a string
#         content = response.content.decode()
        
#         # Check if the payload is present in the response content
#         if payload in content:
#             return True
    
#     return False



# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup as bs
# from urllib.parse import urljoin
# from .beautifulsoup import get_all_forms, get_form_details, submit_form, data, target_url

# def scan_xss(url):
#     # """
#     # Given a `url`, it prints all XSS vulnerable forms and 
#     # returns True if any is vulnerable, False otherwise
#     # """
#     # get all the forms from the URL
#     forms = get_all_forms(url)
#     print(f"[+] Detected {len(forms)} forms on {url}.")
#     js_script = "<Script>alert('hi')</scripT>"
#     # returning value
#     is_vulnerable = False
#     # iterate over all forms
#     for form in forms:
#         form_details = get_form_details(form)
#         content = submit_form(form_details, url, js_script).content.decode()
#         if js_script in content:
#             print(f"[+] XSS Detected on {url}")
#             print(f"[*] Form details:")
#             pprint(form_details)
#             is_vulnerable = True
#             # won't break because we want to print available vulnerable forms
#     return is_vulnerable