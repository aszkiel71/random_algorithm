import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    try:
        # Tworzenie wiadomości e-mail
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Treść wiadomości
        message.attach(MIMEText(body, 'plain'))

        # Dodawanie załącznika (jeśli istnieje)
        if attachment_path:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={filename}'
            )
            message.attach(part)

        # Konfiguracja serwera SMTP (np. Gmail)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Wysyłanie wiadomości
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("E-mail został wysłany pomyślnie.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Przykład użycia
if __name__ == "__main__":
    sender_email = "twoj_email@gmail.com"
    sender_password = "twoje_haslo"  # Uwaga: używaj zmiennych środowiskowych dla bezpieczeństwa
    recipient_email = "odbiorca@example.com"
    subject = "Przykładowy e-mail"
    body = "Cześć! To jest testowy e-mail wysłany w Pythonie."
    attachment_path = "sciezka/do/pliku.txt"  # Zmień na ścieżkę do pliku lub ustaw na None

    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)
