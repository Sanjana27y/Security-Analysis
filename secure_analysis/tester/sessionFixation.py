import requests

def test_sessionfix(url):
    try:
        # Step 1: Make a request to the site to obtain initial cookies
        session = requests.Session()
        response = session.get(url)

        # Check if the response contains cookies
        if response.cookies:
            initial_cookies = response.cookies

            # Step 2: Perform authentication (assuming there is a login page)
            # You may need to adjust the login endpoint and parameters based on the actual application
            login_data = {'username': 'your_username', 'password': 'your_password'}
            response = session.post(url + '/login', data=login_data)

            # Step 3: Check if a new session identifier is issued upon successful authentication
            if 'Set-Cookie' in response.headers:
                new_cookies = response.cookies

                if initial_cookies != new_cookies:
                    # print("The application issues a new session identifier upon authentication.")
                    # print("The website may not be prone to session fixation vulnerability.")
                    return {'url': url, 'is_vulnerable': False, 'details': 'Not prone to session fixation. The application issues a new session identifier upon authentication.'}

                else:
                    # print("No new session identifier issued upon authentication.")
                    # print("The website may be prone to session fixation vulnerability.")
                    return {'url': url, 'is_vulnerable': True, 'details': 'Prone to session fixation. No new session identifier issued upon authentication.'}

            else:
                # print("No Set-Cookie header found in the authentication response.")
                # print("Unable to determine session fixation vulnerability status.")
                return {'url': url, 'is_vulnerable': False, 'details': 'No Set-Cookie header found in the authentication response.Unable to determine session fixation vulnerability status.'}


        else:
            print("No cookies received in the initial request. Unable to proceed.")
            return {'url': url, 'is_vulnerable': False, 'details': 'No cookies received in the initial request. Unable to proceed.'}

    
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

# # Example usage
# user_input_url = input("Enter the URL to test for session fixation vulnerability: ")
# test_session_fixation_vulnerability(user_input_url)
