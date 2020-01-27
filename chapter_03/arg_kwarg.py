#args & kwargs
def user_info(name, age=0, city="Tucson"):
    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Janet", 58, "Oklahama City")
user_info("Micah")
user_info(age=56, name="Kadeem")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")