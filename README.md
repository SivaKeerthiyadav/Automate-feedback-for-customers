# Automate-feedback-for-customers
sending the feedback form to the customer through gmail and retreiving the feedback using python


# Feedback Email System

This project consists of Python scripts to send feedback emails to customers and forward their responses to a technical support team. It uses the `smtplib` library to handle email sending through SMTP.

## Project Structure

- `main.py`: The main script containing functions to send feedback emails to customers and forward emails to the technical support team.
- `README.md`: This file, explaining the project setup and usage.

## Prerequisites

- Python 3.x installed on your machine
- An email account with SMTP access (Gmail is used in this example)
- The following Python libraries:
  - `smtplib`
  - `email.mime.multipart`
  - `email.mime.text`

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/feedback-email-system.git
    cd feedback-email-system
    ```

2. **Install the required Python libraries**:

    ```sh
    pip install -r requirements.txt
    ```

    Note: You may need to create a `requirements.txt` file with the following content:

    ```txt
    smtplib
    email
    ```

3. **Configure email credentials**:

    Open `main.py` and replace the placeholders with your email credentials:

    ```python
    EMAIL = 'your-email@gmail.com'
    PASSWORD = 'your-email-password'
    TECH_TEAM_EMAIL = 'tech.team.email@example.com'
    ```

4. **Set up the forwarding email script**:

    Ensure that your email service provider allows less secure apps or generate an app-specific password if using Gmail.

## Usage

1. **Sending Feedback Email**:

    Modify the `to_email` parameter in the `send_feedback_email` function call at the bottom of `main.py` to the recipient's email address.

    ```python
    send_feedback_email('customer-email@example.com')
    ```

    This function sends an email to the customer with options to provide feedback.

2. **Forwarding Email to Tech Team**:

    Modify the `from_email` parameter in the `forward_email_to_tech_team` function call at the bottom of `main.py` to the customer's email address.

    ```python
    forward_email_to_tech_team('customer-email@example.com')
    ```

    This function forwards the feedback to the technical support team's email address.

## Code Explanation

### `send_feedback_email(to_email)`

This function sends an email to the customer with buttons for providing feedback. The email contains HTML content with two buttons: "Solved" and "Unsolved". Clicking these buttons will alert the customer with a message. The "Unsolved" button initiates an AJAX request to forward the email to the tech team.

### `forward_email_to_tech_team(from_email)`

This function forwards the feedback email to the technical support team. It creates a plain text email with details about the feedback received from the customer and sends it to the tech team.

## Important Notes

- Ensure your email provider's SMTP server settings are correct. This example uses Gmail's SMTP server (`smtp.gmail.com`).
- Make sure to handle sensitive information such as email credentials securely. Avoid hardcoding them in your scripts.
- Modify the HTML and JavaScript in the email body as needed to suit your requirements.

## License

This project is licensed under the MIT License.

