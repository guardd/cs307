import Email
from User import User
user = User(123, "id", "pas", "woo57@purdue.edu", 101001, "M")
Email.send_password_recovery_email(user)
