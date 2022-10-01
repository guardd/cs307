from Email import Email
from User import User
email = Email()
user = User(123, "id", "pas", "woo57@purdue.edu", 101001, "M")
email.send_password_recovery_email(user)
