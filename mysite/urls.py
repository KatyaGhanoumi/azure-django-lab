from django.http import HttpResponse
from django.urls import path

def home (request) :
    return HttpResponse ("""
                         <html>
                         <head><title> Azure Django Lab </title></head>
                         <body>
                            <h1>Hello from Azure! </h1>
                            <p>This app is running on Azure App Service. </p>
                            <p> Deployed automatically by GitHub Actions CI/CD pipeline.</p>
                            <p><strong> Pipeline is working! </strong></p>
                         </body>
                         </html>
                        """)
urlpatterns = [
    path ('', home ) ,
    ]