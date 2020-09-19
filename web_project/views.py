# Views.py controls what is being seen in the browser
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from web_project.models import InsertData
from .forms import urlForm
import requests
import urllib
import json

# The sql function below contain all about the sql injection page

def home_page(request):
 
    context = {
        "feedback": "Feedback"
    }

    return render(request, "home.html", context)


def scanurl(request):
    """ This View contains all about the sql injection """


    form = urlForm(request.POST or None)
    context = {
        "form": form,
        "feedback": "Feedback",
    }

    if request.method == 'POST':
        search_id = request.POST.get('url', None)

        if form.is_valid():

            # the request module is been use to get the header flag
            head = requests.get(search_id).headers

            # This line tests the url for sql injection vulnurability
            response = requests.get(search_id+"%27").text
            printout = ' is vulnerable to SQL injection'

            url = search_id
            url.split("/")[2:]
            array = url.split("/")[0:3]
            str1 = '/'.join(array)

            if 'You have an error in your SQL syntax;' in response:

                if 'MsSQL' in response:
                    form = urlForm(request.POST or None)
                    resp = 'Found database type: MSSQL'
                    context = {
                        "form": form,
                        
                        "head": head,
                        'httpheader': True,

                        "resp": resp,
                        "MsSQL": True,
                        "result": printout,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    insert_data(request, url, resp, context)
                    return render(request, "scanurl.html", context)

                elif 'MySQL' in response:
                    resp = 'Found database type: MYSQL'
                    context = {
                        "form": form,
                        
                        "head": head,
                        'httpheader': True,

                        "resp": resp,
                        "MySQL": True,
                        "result": printout,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    insert_data(request, url, resp, context)
                    return render(request, "scanurl.html", context)

                elif 'MariaDB' in response:
                    resp = 'Found database type: MariaDB'
                    context = {
                        "form": form,
                        
                        "head": head,
                        'httpheader': True,
                        
                        "resp": resp,
                        "MariaDB": True,
                        "result": printout,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    insert_data(request, url, resp, context)
                    return render(request, "scanurl.html", context)

                else:
                    resp = 'can not find the type of database used'
                    context = {
                        "form": form,

                        "head": head,
                        'httpheader': True,

                        "resp": resp,
                        "notvulnerable": True,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    return render(request, "scanurl.html", context)

            else:
                printout = " is NOT vulnerable to SQL injection"

                context = {
                    "form": form,

                    "head": head,
                    'httpheader': True,
                    
                    'notvulnerable': True,
                    "feedback": "Feedback",
                    "link": str1,
                    "result": printout
                }
                return render(request, "scanurl.html", context)
    return render(request, "scanurl.html", context)


def scanform(request):
    """ this view check for the form parameter """

    form = urlForm(request.POST or None)
    context = {
        "feedback": "Feedback",
        "form": form,
    }

    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        url = search_id

        if form.is_valid():

            # the request module is been use to get the header flag
            head = requests.get(search_id).headers

            from requests.auth import HTTPBasicAuth
            url = search_id
            req1 = requests.get(url)
            # sql query is been sent to the login form
            req = requests.get(url, auth=HTTPBasicAuth(
                '1\'or\'1\'=\'1', '1\'or\'1\'=\'1'))

            if req1.text != req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is NOT vulnerable to SQL Injection'
                context = {
                    "form": form,

                    "head": head,
                    'httpheader': True,

                    "notvulnerable": True,
                    "getresult": getresult,
                    "feedback": "Feedback",
                    "link": str1,
                }
                print('NOT vulnerable to SQL Injection')
                return render(request, "scanform.html", context)

            elif "invalid" in req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable to SQL Injection'
                context = {
                    "form": form,
                    
                    "head": head,
                    'httpheader': True,
                    
                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback": "Feedback",
                }
                return render(request, "scanform.html", context)

            elif "incorrect" in req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable to SQL Injection'
                context = {
                    "form": form,
                    
                    "head": head,
                    'httpheader': True,

                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback": "Feedback",
                }
                return render(request, "scanform.html", context)

            elif "Wrong" in req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable to SQL Injection'
                context = {
                    "form": form,

                    "head": head,
                    'httpheader': True,

                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback": "Feedback",
                }
                return render(request, "scanform.html", context)

            elif "error login" in req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable to SQL Injection'
                context = {
                    "form": form,

                    "head": head,
                    'httpheader': True,

                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback": "Feedback",
                }
                return render(request, "scanform.html", context)

            else:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is vulnerable to SQL Injection'
                context = {
                    "form": form,

                    "head": head,
                    'httpheader': True,

                    "vulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback": "Feedback",
                }
                insert_data(request, search_id, getresult, context)
                return render(request, "scanform.html", context)
    return render(request, "scanform.html", context)


def xss(request):
    form = urlForm(request.POST or None)

    context = {
        "form": form,
        "feedback": "Feedback",
    }

    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        url = search_id
        url.split("/")[2:]
        array = url.split("/")[0:3]
        str1 = '/'.join(array)
        
        # javascript code is been supply
        if form.is_valid():

             # the request module is been use to get the header flag
            head = requests.get(search_id).headers

            payloads = ['<script>alert(1);</script>', '<BODY ONLOAD=alert(1)>']
            for payload in payloads:
                req = requests.post(url+payload)
                if payload in req.text:
                    resp = " is vulnerable to XSS\r\n"
                    context = {
                        "form": form,

                        "head": head,
                        'httpheader': True,

                        "getresult": resp,
                        "vulnerable": True,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    print("Parameter vulnerable to XSS\r\n")
                    print("Attack string: "+payload)
                    insert_data(request, url, resp, context)
                    return render(request, "xss.html", context)
                else:
                    resp = " is NOT vulnerable to XSS\r\n"
                    context = {
                        "form": form,

                        "head": head,
                        'httpheader': True,

                        "getresult": resp,
                        "notvulnerable": True,
                        "link": str1,
                        "feedback": "Feedback",
                    }
                    print("Parameter NOT vulnerable to XSS\r\n")
                    return render(request, "xss.html", context)
    return render(request, "xss.html", context)



def insert_data(request, url, resp, context):
        saved_data=InsertData()
        saved_data.url=url
        saved_data.result=resp
        saved_data.context=context
        saved_data.save()

def show_data(request):
    resultsdisplay=InsertData.objects.all()
    return render(request, "view.html",{'InsertData':resultsdisplay})