
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='suryaashokan57@gmail.com',
    to_emails='btechsurya671@gmail.com',
    subject='alert message - update your stock immediatly',
    html_content='<strong>update your product quanty.</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)



