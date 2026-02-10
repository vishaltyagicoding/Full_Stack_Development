from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def create_session(request):
    request.session['username'] = 'Vishal'
    request.session['email'] = 'alberttyagi123@gmai.com'
    return HttpResponse("Session created successfully.")

def get_session(request):
    username = request.session['username']
    email = request.session['email']
    return HttpResponse("Username: " + username + " Email: " + email)

def delete_session(request):
     # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse("Session data deleted successfully.")
    request.session.flush() # This will delete all session data
    return HttpResponse("All session data deleted successfully.")

# redirect to create session page
def home(request):
    return redirect('create_session')
