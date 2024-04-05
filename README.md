# Security-Analysis
Analyze the security of a website by identifying potential vulnerabilities just by entering the website URL
Vulnerabilities that can be detected are:
1. CSRF
2. Directory Traversal
3. XSS
4. XML- External Entity
5. Local File Inclusion
6. Session Fixation 
7. Security Misconfiguration

## Project Setup
Follow the below steps to run the project.

1. Clone this repository
2. Run the commands:
   ```
   cd secure_analysis
   ```
   ```
   python manage.py runserver
   ```
3. After getting message like "Starting development server at http://127.0.0.1:8000/", go to the link to launch the website.
4. Enter the url to be analysed and hit Submit. The next page will show the results of that particular url.
