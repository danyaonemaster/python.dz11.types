input_login = input("Enter your login : ")
login_u = ("admin", "user", "QA", "Dev", "superuser", "superadmin")
pass_u = (125, 124, 354, 781, 874, 347)


if input_login in login_u:
    input_password = int(input("Enter your password : "))
    if login_u.index(input_login) == pass_u.index(input_password):
        print(f"""
    login : {input_login}
    password : {input_password}
    Access""")
else:
    print(f"""
    login : {input_login}
    Not Access""")
