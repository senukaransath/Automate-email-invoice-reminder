import pandas as pd
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Email Configuration from .env file
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL")
SENDER_PASSWORD = os.getenv("PASSWORD")


# Read Excel Data
def read_excel_data(filename):
    df = pd.read_excel(filename, engine="openpyxl")
    return df

# Send Email


def send_email(receiver_email, name, invoice_no, amount, due_date):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = f"⏳ Payment Reminder : Invoice {invoice_no} - Due Soon!"

        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
            <div style="padding: 20px; background-color: #f8f8f8; border-radius: 10px;">
                <h2 style="color: #d9534f;">🚨 Payment Reminder - Invoice {invoice_no}</h2>
                <p>Dear <strong>{name}</strong>,</p>

                <p>We hope you're doing well! This is a friendly reminder that your payment of  
                <strong style="color: #28a745;">Rs. {amount:,.2f}</strong>  
                for Invoice <strong>{invoice_no}</strong> is due on  
                <strong style="color: #d9534f;">{due_date}</strong>.</p>

                <p>Kindly make the payment at your earliest convenience to avoid any late fees.</p>

                <hr style="border: 0; height: 1px; background: #ccc;">
                <h3 style="color: #5bc0de;">📝 Invoice Details</h3>
                <ul>
                    <li><strong>Invoice Number:</strong> {invoice_no}</li>
                    <li><strong>Amount Due:</strong> Rs. {amount:,.2f}</li>
                    <li><strong>Due Date:</strong> {due_date}</li>
                </ul>

                <p>If you have already made the payment, please ignore this message.</p>

                <p>For any questions, feel free to contact us.</p>

                <p style="margin-top: 20px;">Thank you for your prompt attention to this matter.</p>

                <p style="color: #555;"><strong>Best regards,</strong><br>
                <strong>Senux PVT Ltd</strong><br>
                📧 support@senux.com | 📞 +94 7XX XXX XXX</p>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(body, "html"))  # Use HTML email format

        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()

        print(f"🚀 Reminder email sent to {receiver_email}")

    except Exception as e:
        print(f"❌ Error sending email to {receiver_email}: {e}")


# Main Function
def main():
    excel_file = "invoice_data.xlsx"  # Ensure this file is in the same directory
    df = read_excel_data(excel_file)

    # Get today's date in mm/dd/yyyy format
    today = datetime.today().strftime('%m/%d/%Y')

    for index, row in df.iterrows():
        # Convert reminder_date to string and format it
        reminder_date = row["reminder_date"]
        if isinstance(reminder_date, datetime):
            reminder_date = reminder_date.strftime(
                '%m/%d/%Y')  # Convert datetime to string

        # Check if today matches the reminder date and the invoice is unpaid
        if row["has_paid"].strip().lower() == "no" and reminder_date == today:
            send_email(
                row["email"],
                row["name"],
                row["invoice_no"],
                row["amount"],
                row["due_date"]
            )


if __name__ == "__main__":
    main()
