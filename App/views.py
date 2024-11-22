from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def sai(request):
    return HttpResponse('He is a very Talented and Hardworking guy')
def chandu(request):
    return HttpResponse("<h1>This is an Heading of the project</h1>")
def project(request):
    return HttpResponse("<h1><marquee>WEB DEVELOPER</marquee></h1>")
def image(request):
    return HttpResponse("<img src="">")
def form(request):
    return HttpResponse('''
                        <h1>Registration form</h1>
                        <marquee>Aplication form for web Developement</marquee>
                        <h2>Name: Saichandu</h2>
                        <h2>MobileNo: 8688637574</h2>
                        <h2>Email:vaddlasaicahndu@gmail.com</h2>
                        <h2>Course:Python full stack Developer</h2>
                        <h2>college:Loyola Institute of Technology and Management</h2>
                        <h2>Branch:Electronics and communication Engineering</h2>
                        "Registration Successfull"
                        <p>Your Application is submitted successfully...........</p>''')
    
def im(request):
    return HttpResponse('<marquee><img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gettyimages.in%2Fphotos%2Fborder-gavaskar-trophy&psig=AOvVaw0jlIM5JDGmtbrVQgitKGyi&ust=1732341630075000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCODo4O-f74kDFQAAAAAdAAAAABAK" width="200px" height="200px"></marquee>')

def response(request):
    return HttpResponse('''<h1 style=color:blue;background-color:yellow;padding:20px;text-align:center;border:2px solid transparent;>This is an Heading of the Django framewok<h2>
                        <marquee><img  src="https://c.ndtvimg.com/2024-06/i4qd5esk_virat-kohli-rohit-sharma_625x300_30_June_24.jpeg?im=FeatureCrop,algorithm=dnn,width=806,height=605" width="100%" height="1000px" ></marquee>''')