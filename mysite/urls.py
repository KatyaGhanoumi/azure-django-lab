from django.http import HttpResponse
from django.urls import path

def home (request) :
    return HttpResponse ("""
                         <html>
                         <head><title> Azure Django Lab </title></head>
                         <body style ="font-family: Arial; padding: 40px;">
                            <h1 style="color: #0066cc;">> Version 2 - Updated Automatically!</h1>
                            <p>This change was deployed with zero manual server work.</p>
                            <p>The CI/CD pipeline handled everything.</p>
                         </body>
                         </html>
                        """)
urlpatterns = [
    path ('', home ) ,
]