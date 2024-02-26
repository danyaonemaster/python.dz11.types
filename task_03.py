input_login = input("Enter your login : ")
input_password = int(input("Enter your password : "))
login_u = ("admin", "user", "QA", "Dev", "superuser", "superadmin")
pass_u = (125, 124, 354, 781, 874, 347)

for login,password,i in zip(login_u, pass_u, range(len(login_u))):
    if login == input_login and password == input_password:
        exit(f"""
    login : {input_login}
    password : {input_password}
    Access""")
else:
    exit(f"""
    login : {input_login}
    password : {input_password}
    Not Access""")
