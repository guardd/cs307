import mailslurp_client
from User import User
import random
# create a mailslurp configuration
def send_password_recovery_email(user): #note : gmail doesnt work with this shit
#returns : the code generated for the email
    firstdigit = random.randint(1, 9)
    code = "" + str(firstdigit)
    for x in range(5):
        code = code + str(random.randint(0, 9))


    configuration = mailslurp_client.Configuration()
    configuration.api_key['x-api-key'] = "fad70e9b7a0127f76862a66d290f3178a18ad386b843125c6730048604b2ec6d"
    with mailslurp_client.ApiClient(configuration) as api_client:
    # create an inbox
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox_1 = inbox_controller.create_inbox()
        opts = mailslurp_client.SendEmailOptions()
        opts.to = [user.get_email()]
        opts.subject = "Password Recovery from The Crystal Ball"
        opts.body = "This is a password recovery email from the crystal ball.\nIf you didn't request password recovery, please ignore.\n The code for password recovery is " + code  + "\nFrom The Crystal Ball"
        opts.is_html = False
        inbox_controller.send_email(inbox_1.id, send_email_options=opts)
