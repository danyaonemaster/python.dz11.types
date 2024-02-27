input_login = input("Enter your login : ")
login_u = ("admin", "user", "QA", "Dev", "superuser", "superadmin")
pass_u = (125, 124, 354, 781, 874, 347)

if input_login in login_u:
    index = login_u.index(input_login)
    if input_login == login_u[index]:
        input_password = int(input("Enter your password : "))
        if input_password == pass_u[index]:
            print(f"""
        login : {input_login}
        password : {input_password}
        Access""")
        else:
            print(f"""
        login : {input_login}
        password : {input_password}
        Not Access""")
else:
    print(f"""
    login : {input_login}
    Not Access""")
