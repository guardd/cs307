import mailslurp_client
from User import User
import random
# create a mailslurp configuration
class Email():
    def __init__(self):
        import mailslurp_client
        from User import User
        import random
        self.configuration = mailslurp_client.Configuration()
        self.configuration.api_key['x-api-key'] = "a8af51cd52b73a71e78dd7c3a53b798179c5326868e3a567d3b01ec6650f8fad"
        with mailslurp_client.ApiClient(self.configuration) as api_client:
            self.inbox_controller = mailslurp_client.InboxControllerApi(api_client)
            self.inbox_1 = self.inbox_controller.create_inbox()

    def send_password_recovery_email(self, user): #note : gmail doesnt work with this shit
                                                #returns : the code generated for the email
        opts = mailslurp_client.SendEmailOptions()
        opts.to = [user.get_email()]
        opts.subject = "Password Recovery from The Crystal Ball"
        opts.body = "This is a password recovery email from the crystal ball.\nIf you didn't request password recovery, please ignore.\n Your password is: " + user.password  + "\nAfter logging in again, please reset your password.\nFrom The Crystal Ball"
        opts.is_html = False
        self.inbox_controller.send_email(self.inbox_1.id, send_email_options=opts)
        print("password recovery email sent")

    def send_email_verify_email(self, email):
        firstdigit = random.randint(1, 9)
        code = "" + str(firstdigit)
        for x in range(5):
            code = code + str(random.randint(0, 9))

        opts = mailslurp_client.SendEmailOptions()
        opts.to = [email]
        opts.subject = "Email verification from The Crystal Ball"
        opts.body = "This is an email verification from the crystal ball.\nIf you didn't request an email verification, please ignore.\n The code for email verification is " + code  + "\nFrom The Crystal Ball"
        opts.is_html = False
        self.inbox_controller.send_email(self.inbox_1.id, send_email_options=opts)
        return code

    
