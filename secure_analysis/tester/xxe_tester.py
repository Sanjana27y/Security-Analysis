import requests
from defusedxml import ElementTree as DET

def test_xxe(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_string = response.text

        # Check for XXE vulnerability
        tree = DET.fromstring(xml_string)

        # Check for external entities in the DTD
        dtd_content = tree.docinfo.internalDTD
        if dtd_content and 'external-entity' in dtd_content:
            return {'url': url, 'is_vulnerable': True, 'details': 'XXE vulnerability detected (DTD external entity)'}

        # Check for external entities in the document content
        entities = tree.findall('.//external-entity')
        if entities:
            return {'url': url, 'is_vulnerable': True, 'details': 'XXE vulnerability detected (document content)'}

        # No XXE vulnerability detected
        return {'url': url, 'is_vulnerable': False, 'details': 'No XXE vulnerability detected'}

    except Exception as e:
        # XXE vulnerability detected
        return {'url': url, 'is_vulnerable': True, 'details': f'XXE vulnerability detected: {str(e)}'}



# import requests
# from defusedxml import ElementTree as DET

# def test_xxe(url):
#     try:
#         response = requests.get(url)
#         xml_content = response.text

#         # Check for basic XXE
#         is_basic_xxe = is_basic_xxe_vulnerable(xml_content)

#         # Check for other XXE vulnerabilities
#         is_resource_exhaustion_xxe = is_resource_exhaustion_xxe_vulnerable(xml_content)
#         is_data_extraction_xxe = is_data_extraction_xxe_vulnerable(xml_content)
#         is_ssrf_xxe = is_ssrf_xxe_vulnerable(xml_content)
#         is_file_retrieval_xxe = is_file_retrieval_xxe_vulnerable(xml_content)
#         is_blind_xxe = is_blind_xxe_vulnerable(xml_content)

#         # Aggregate results
#         is_vulnerable = any([is_basic_xxe, is_resource_exhaustion_xxe, is_data_extraction_xxe,
#                              is_ssrf_xxe, is_file_retrieval_xxe, is_blind_xxe])

#         details = {
#             'Basic XXE': is_basic_xxe,
#             'Resource Exhaustion XXE': is_resource_exhaustion_xxe,
#             'Data Extraction XXE': is_data_extraction_xxe,
#             'SSRF XXE': is_ssrf_xxe,
#             'File Retrieval XXE': is_file_retrieval_xxe,
#             'Blind XXE': is_blind_xxe
#         }

#         return {'url': url, 'is_vulnerable': is_vulnerable, 'details': details}

#     except Exception as e:
#         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}

# def is_basic_xxe_vulnerable(xml_content):
#     try:
#         DET.fromstring(xml_content)
#         return False
#     except Exception as e:
#         return True

# Implement other XXE vulnerability checks similar to is_basic_xxe_vulnerable
# ...



# import requests
# from defusedxml import ElementTree as DET

# def test_xxe(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         xml_string = response.text

#         # Check for XXE vulnerability
#         tree = DET.fromstring(xml_string)
#         entities = tree.findall('.//external-entity')

#         if entities:
#             return {'url': url, 'is_vulnerable': True, 'details': 'XXE vulnerability detected'}
#         else:
#             return {'url': url, 'is_vulnerable': False, 'details': 'No XXE vulnerability detected'}
#     except Exception as e:
#         # XXE vulnerability detected
#         return {'url': url, 'is_vulnerable': True, 'details': f'XXE vulnerability detected: {str(e)}'}



# import xml.etree.ElementTree as ET
# from defusedxml import ElementTree as DET
# from defusedxml.common import DefusedXmlException
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import XXEReport  # Make sure to import your XXE model

# def is_xxe_vulnerable(xml_string):
#     try:
#         # Use defusedxml to parse XML safely
#         DET.fromstring(xml_string)
#     except DefusedXmlException:
#         return True
#     return False

# def parse_xml(xml_string):
#     try:
#         root = ET.fromstring(xml_string)
#         for child in root:
#             print(child.tag, child.attrib)
#     except ET.ParseError:
#         print("Error: Not well-formed.")

# def test_xxe(url):
#     try:
#         xml_string = open(url, 'r').read()
#         if is_xxe_vulnerable(xml_string):
#             # Store XXE test result in the database
#             XXEReport.objects.create(url=url, is_vulnerable=True)
#             return {'url': url, 'is_vulnerable': True, 'details': 'XXE vulnerability detected'}
#         else:
#             # Store non-vulnerable result in the database
#             XXEReport.objects.create(url=url, is_vulnerable=False)
#             return {'url': url, 'is_vulnerable': False, 'details': 'No XXE vulnerability detected'}
#     except Exception as e:
#         return {'url': url, 'is_vulnerable': False, 'details': f'Error: {str(e)}'}

# # View function for XXE testing endpoint
# def test_xxe_endpoint(request):
#     url = request.GET.get('url')

#     try:
#         xxe_report = test_xxe(url)
#         return render(request, 'analyser.html', {'xxe_result': xxe_report})
#     except Exception as e:
#         return JsonResponse({'error': 'Internal Server Error'}, status=500)
