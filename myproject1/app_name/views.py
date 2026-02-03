from django.shortcuts import render

# Create your views here.
class ILoveYouPython():
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    blogs = [
        {'id': 1232, 'title': 'First Post', 'content': 'Content of the first post'},
        {'id': 2343, 'title': 'Second Post', 'content': 'Content of the second post'},
        {'id': 3890, 'title': 'Third Post', 'content': 'Content of the third post'},
    ]
    context = {
        "blogs":blogs,
        'message': 'Welcome to the Home Page!',
        'developer': ILoveYouPython('Vishal', 23),
        "empty_value": None,
        "bold_p_tag": "<b>This is Bold</b>",
        "title": "my second temLate post",
        "number": 2,
        "price": 100,
        "current_date":
        "29-01-2026",
        "my_list": ["Vishal", "Tyagi", "From", "USA"],
        
    }
    return render(request, 'app_name/home.html', context)