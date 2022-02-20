def personal_data(**data):
    print(data)


n = input("Enter your name: ")
s_n = input("Enter your surname: ")
y_of_b = input("Enter your year_of_birth: ")
c_of_r = input("Enter your City_of_residence: ")
em = input("Enter your email: ")
p_n = input("Enter your phone_number: ")


personal_data(name=n, surname=s_n, age=y_of_b, city=c_of_r, email=em, phone=p_n)
