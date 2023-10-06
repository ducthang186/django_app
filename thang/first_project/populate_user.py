import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django 
django.setup()

# FAKE POP SCRIPT
import faker
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(number_user):
       for _ in range(number_user):
            firstname = fakegen.first_name()
            lastname = fakegen.last_name()
            email = fakegen.email()

            user = User(firstname = firstname,lastname = lastname,email =email)
            user.save()

# số lượng người dùng
number_user = 3
# goi hàm tạo dữ liệu
populate(number_user)
