import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
EMAIL = 'pixeltest281@gmail.com'
PASSWORD = 'ayldxtreeqarmalh'
TECH_TEAM_EMAIL = 'tech.team.pixeltests@gmail.com'  # Replace with the email of your tech team

# Function to send email
def send_feedback_email(to_email):
    # Create a multipart message
    msg = MIMEMultipart()

    # Email details
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = 'Feedback'

    # Email body with HTML content
    body = """
    <html>
    <body>
        <p>Dear Customer,</p>
        <p>Please click on one of the buttons below to provide feedback:</p>
        <a href="https://bespoke-paprenjak-f3d80d.netlify.app/">
            <button onclick="handleFeedback('Solved')" style="background-color: #4CAF50; /* Green */
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 10px;">Solved</button>
        </a>
        <a href="https://poetic-moonbeam-fb136d.netlify.app/" onclick="handleFeedback('Unsolved')">
            <button style="background-color: #f44336; /* Red */
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 10px;">Unsolved</button>
        </a>
        <script>
            function handleFeedback(buttonValue) {
                if (buttonValue === 'Solved') {
                    alert('Thanks for your feedback! Happy to hear your issue is solved.');
                } else {
                    alert('Thanks for your feedback! Our customer support team will reach you soon.');
                    forwardEmail();
                }
            }

            function forwardEmail() {
                // AJAX request to forward the email
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        console.log('Email forwarded to the tech team.');
                    }
                };
                xhttp.open("POST", "forward_email", true);
                xhttp.send();
            }
        </script>
    </body>
    </html>
    """

    # Attach HTML to the email
    msg.attach(MIMEText(body, 'html'))

    # Connect to SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        # Login to the email account
        smtp.login(EMAIL, PASSWORD)
        # Send email
        smtp.send_message(msg)

# Function to forward email to tech team
def forward_email_to_tech_team(from_email):
    # Create a new message
    msg = MIMEMultipart()

    # Email details
    msg['From'] = from_email
    msg['To'] = TECH_TEAM_EMAIL
    msg['Subject'] = 'Feedback from Customer'

    # Email body
    body = f"""
    Hello Tech Team,

    Feedback email received from: {from_email}.

    Please review and take necessary action.

    Regards,
    Pixel Tests
    """

    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        # Login to the email account
        smtp.login(EMAIL, PASSWORD)
        # Send email
        smtp.send_message(msg)

# Send email to the customer
send_feedback_email('thattukollasivakeerthi@gmail.com')

# Forward email to tech team
forward_email_to_tech_team('thattukollasivakeerthi@gmail.com')
