from send_email import send_text_email

from message import generate_message

print(generate_message())

send_text_email(subject='An email', content=generate_message())
