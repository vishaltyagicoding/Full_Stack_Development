import os
import django
import sys
from datetime import date
from faker import Faker
from datetime import timedelta
import random
import uuid

# Clear terminal
os.system('cls')

# Add your project directory to the Python path
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject5.settings')
django.setup()

# Now import your models
from app1.models import Students

# Your code here
def view_students():
    # Get all students
    all_students = Students.objects.all()




    # Get field names dynamically
    field_names = [field.name for field in Students._meta.get_fields()]
    print(f"Columns: {field_names}")
    print("-" * 50)




    # Print each student's data
    for student in all_students:
        row_data = []
        for field_name in field_names:
            value = getattr(student, field_name)
            # Format date fields
            if hasattr(value, 'strftime'):
                value = value.strftime('%Y-%m-%d') 
            row_data.append(value)
        # print(row_data)



    # order_by function return data in asending order
    # print("\n\nStudents ordered by name:")
    # ordered_students = Students.objects.all().order_by('name').values()
    # print(ordered_students)



    # chaing of fillter function
    # print("\n\nStudents older than 20:")
    # for greather then you can use age__gt = 24
    # filtered_students = Students.objects.filter(age__lt=24).order_by('age').values()
    # print(filtered_students)



    # filter function return data on specific condition
    # print("\n\nStudents from New York:")
    # filtered_students = Students.objects.filter(city="New Tina").values()
    # print(filtered_students)



    # exclude function it's just apposite of fillter function exclude function all data other then you pass data one exclude function like...
    # print("\n\nStudents not older than 20:")
    # excluded_students = Students.objects.exclude(age__gt=20).values()
    # print(excluded_students)



    # count function return total numbers of records in db
    total_students = Students.objects.count()
    print(f"\nTotal number of students: {total_students}")



def random_date_2000_to_today():
    # Define start and end dates
    start_date = date(2000, 1, 1)
    end_date = date.today()
    # Calculate days between dates
    days_between = (end_date - start_date).days
    # Generate random number of days
    random_days = random.randint(0, days_between)
    # Add random days to start date
    random_date = start_date + timedelta(days=random_days)
    return random_date



# add data on selected columns
def add_data():
    cities = ["New York", "London", "Tokyo", "Paris", "Sydney", "Berlin"]

    for i, student in enumerate(Students.objects.all()):
        cities = ["New York", "London", "Tokyo"]
        student.city = cities[i % len(cities)]  # Cycle through cities
        student.save()



# add all columns data on database
def add_dummy_data(number_of_rows = 10):
    # first way
    # dummy_data = [
    #     {"name": "Alice Johnson", "age": 22, "email": "alice@example.com", "enrolled_date": date.today ,"city": "New York"},
    #     {"name": "Bob Smith", "age": 24, "email": "bob@example.com", "enrolled_date": date.today ,"city": "London"},
    #     {"name": "Charlie Brown", "age": 21, "email": "charlie@example.com", "enrolled_date": date.today ,"city": "Tokyo"},
    #     {"name": "Diana Prince", "age": 23, "email": "diana@example.com", "enrolled_date": date.today ,"city": "Paris"},
    #     {"name": "Ethan Hunt", "age": 25, "email": "ethan@example.com", "enrolled_date": date.today ,"city": "Sydney"},
    # ]

    # for data in dummy_data:
    #     Students.objects.create(**data)

    # second way
    fake = Faker()
    start_date = date.today()
    # Add 10 random students
    for i in range(number_of_rows):
        unique_email = f"{fake.user_name()}_{uuid.uuid4().hex[:8]}@example.com"
        Students.objects.create(
            name=fake.name(),
            age=fake.random_int(min=18, max=30),
            email=unique_email,
            enrolled_date=fake.date_between(start_date='-24y', end_date='today'),
            city=fake.city(),
            
        )

    print("Added 10 random students")


# delete all data in database
# this is dangerous use be careful
def delete_all_data():
    deleted_count, _ = Students.objects.all().delete()
    print(f"Deleted {deleted_count} students")



print(f"Updated {Students.objects.count()} students")
if __name__ == "__main__":
    # delete_all_data()
    # add_data()
    add_dummy_data(100)
    view_students()