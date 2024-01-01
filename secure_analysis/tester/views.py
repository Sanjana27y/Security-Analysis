# part 2

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from .directory_traversal_tester import test_directory_traversal
from .xxe_tester import test_xxe

from .lfi_tester import test_lfi
from .sessionFixation import test_sessionfix
from .csrf_tester import test_csrf
from .sims_tester import test_security_misconfigurations
from .xss_tester import test_xss
from .models import DTReport, XXEReport, SMisReport, XSSReport, CSRFReport, SessionFixReport, LFIReport
# on 30th 
# Import testing functions


# def index(request):
#     cookies = request.COOKIES
#     return render(request, 'index.html')

# @require_GET
# def test_directory_traversal_endpoint(request):
#     cookies = request.COOKIES

#     if request.method == 'POST':
#         url = request.POST.get('url')
#     else:
#         url = request.GET.get('url')

#     try:
#         # Test Directory Traversal
#         report_dt = test_directory_traversal(url)
#         DTReport.objects.create(url=url, is_vulnerable=report_dt['is_vulnerable'])

#         # Test XXE
#         report_xxe = test_xxe(url)
#         XXEReport.objects.create(url=url, is_vulnerable=report_xxe['is_vulnerable'])

#         # Test SMis
#         report_sims = test_security_misconfigurations(url)  # Adjust this function call based on your actual implementation
#         SMisReport.objects.create(url=url, is_vulnerable=report_sims['is_vulnerable'])

#         # Test SQL injection
#         report_sqli = test_sqli(url)
#         SQLIReport.objects.create(url=url, is_vulnerable=report_sqli['is_vulnerable'])

#         return render(
#             request,
#             'analyser.html',
#             {'result_dt': report_dt, 'result_xxe': report_xxe, 'result_sims': report_sims, 'result_sqli': report_sqli}
#         )
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


#  WORKING WITH THE BELOW UNTILL 6PM 30-12-23
# 


def index(request):
    cookies = request.COOKIES
    return render(request, 'index.html')

@require_GET
def test_directory_traversal_endpoint(request):
    cookies = request.COOKIES
    url = request.GET.get('url')

    try:
        
        
        report_dt = test_directory_traversal(url)
        DTReport.objects.create(url=url, is_vulnerable=report_dt['is_vulnerable'])
        
        # Test XXE
        report_xxe = test_xxe(url)
        XXEReport.objects.create(url=url, is_vulnerable=report_xxe['is_vulnerable'])
        
        # Test SMis 
        report_sims = test_security_misconfigurations(url) 
        SMisReport.objects.create(url=url, is_vulnerable=report_sims['is_vulnerable'])
        
        # # Test for sqli
        # report_sqli = test_sqli(url)
        # SQLIReport.objects.create(url=url, is_vulnerable=report_sqli['is_vulnerable'])
        
        # # Test XSS
        # if request.method == 'POST':
        #    url_to_test = request.POST.get('url')
        xss_results = test_xss(url)
           
        # # for result in xss_results:
        # XSSReport.objects.create(
        #             url=url,
        #             is_vulnerable=True, 
        #             location=xss_results.get('location', ''),
        #             field=xss_results.get('field', ''),
        #             value=xss_results.get('value', '')
        #        )
        location = ''
        field = ''
        value = ''
        for result in xss_results:
           location = result.get('location', '')
           field = result.get('field', '')
           value = result.get('value', '')

        XSSReport.objects.create(
        url=url,
        is_vulnerable=True,
        location=location,
        field=field,
        value=value
    )
        
        # Test for CSRF
        # report_csrf = test_csrf(url)
        # CSRFReport.objects.create(url=url, is_vulnerable=report_csrf['is_vulnerable'])
        report_csrf = test_csrf(url)
        CSRFReport.objects.create(url=url, is_vulnerable=report_csrf['is_vulnerable'])
        
        # Test foe Session FIxation 
        report_sessionfix = test_sessionfix(url)
        SessionFixReport.objects.create(url=url, is_vulnerable=report_csrf['is_vulnerable'])
        
        # Test foe LFI 
        report_lfi = test_lfi(url)
        LFIReport.objects.create(url=url, is_vulnerable=report_lfi['is_vulnerable'])
        
        


        
        return render(request, 'analyser.html', {'result_dt': report_dt, 'result_xxe': report_xxe, 'result_sims': report_sims, 'result_xss': XSSReport, 'result_csrf': report_csrf, 'result_sessionfix': report_sessionfix, 'result_lfi': report_lfi })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# this is when we are implementing xxe also:

# import logging
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from .directory_traversal_tester import test_directory_traversal
# from .xxe_tester import test_xxe  # Assuming you have a module for XXE testing
# from .models import DTReport, XXEReport

# logger = logging.getLogger(__name__)

# def index(request):
#     # Your view logic goes here
#     return render(request, 'index.html')

# @require_GET
# def test_directory_traversal_endpoint(request):
#     cookies = request.COOKIES
#     url = request.GET.get('url')

#     try:
#         report = test_directory_traversal(url)

#         # Save the results in the DTReport model
#         DTReport.objects.create(url=url, is_vulnerable=report['is_vulnerable'])

#         return render(request, 'analyser.html', {'result': report})
#     except Exception as e:
#         logger.error(f'Error during directory traversal test: {e}')
#         return JsonResponse({'error': 'Internal Server Error'}, status=500)

# @require_GET
# def test_xxe_endpoint(request):
#     cookies = request.COOKIES
#     url = request.GET.get('url')

#     try:
#         report = test_xxe(url)

#         # Save the results in the XXEReport model
#         XXEReport.objects.create(url=url, is_vulnerable=report['is_vulnerable'])

#         return render(request, 'analyser.html', {'result': report})
#     except Exception as e:
#         logger.error(f'Error during XXE test: {e}')
#         return JsonResponse({'error': 'Internal Server Error'}, status=500)



# #  trail for static:
# from django.http import JsonResponse
# from .directory_traversal_tester import test_directory_traversal
# from django.shortcuts import render

# def index(request):
#     # Your view logic goes here
#     return render(request, 'index.html')

# def test_directory_traversal_endpoint(request):
#     # For testing purposes, return a static JSON response
#     data = {'url': 'http://example.com', 'is_vulnerable': True, 'details': 'Test result'}
#     return JsonResponse(data)


# import logging
# import traceback  # Import the traceback module
# # #  the below code is the latest- 20/12/23*******
# logger = logging.getLogger(__name__)
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from .directory_traversal_tester import test_directory_traversal
# from .models import DTReport

# def index(request):
#     cookies = request.COOKIES
#     return render(request, 'index.html')

# @require_GET
# def test_directory_traversal_endpoint(request):
#     cookies = request.COOKIES
#     url = request.GET.get('url')

#     try:
#         report = test_directory_traversal(url)
#         DTReport.objects.create(url=url, is_vulnerable=report['is_vulnerable'])

#         # Render the 'analyser.html' template with the results
#      #    return JsonResponse(report)
#         return render(request, 'analyser.html', {'result': report})
          
#     except Exception as e:
#         logger.error(f'Error during directory traversal test: {e}')
#         traceback.print_exc()

#         return JsonResponse({'error': str(e)}, status=500)

#         return JsonResponse(report)
#     except Exception as e:
#         logger.error(f'Error during directory traversal test: {e}')
#         return render(request, 'analyser.html')


# ************************************************
# import logging
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from .directory_traversal_tester import test_directory_traversal
# from .models import DirectoryTraversalReport

# logger = logging.getLogger(__name__)

# def index(request):
#     cookies = request.COOKIES
#     return render(request, 'index.html')

# @require_GET
# def test_directory_traversal_endpoint(request):
#     cookies = request.COOKIES
#     url = request.GET.get('url')

#     try:
#         report = test_directory_traversal(url)
#         DirectoryTraversalReport.objects.create(url=url, is_vulnerable=report['is_vulnerable'])
        
#         return JsonResponse({'url': url, 'is_vulnerable': report['is_vulnerable']})   
#      # return JsonResponse(report)
#     except Exception as e:
#         logger.error(f'Error during directory traversal test: {e}')
#         return render(request, 'analyser.html')
#      #    return JsonResponse({'error': 'Internal Server Error'}, status=500)
           

# import logging
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from .directory_traversal_tester import test_directory_traversal
# from .models import DirectoryTraversalReport  # Add this import

# # Create your views here.
# def index(request):
#      cookies = request.COOKIES
#      return render(request, 'index.html')

# # def tester(request):
# #     return render(request, 'analyser.html')

# @require_GET
# def test_directory_traversal_endpoint(request):
#      cookies = request.COOKIES
#      url = request.GET.get('url')
     
#      try:
#           report = test_directory_traversal(url)
#           DirectoryTraversalReport.objects.create(url=url, is_vulnerable = report['is_vulnerable'])
          
#           return JsonResponse(report)
#      except Exception as e:
#           logger.error(f' Error during directory traversal teste: {e}')
#           return JsonResponse({'error': 'Internal Server Error'}, status = 500)