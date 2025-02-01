# 🚀 Invoice Reminder Automation (Windows & Gmail-Based)
Automate **email reminders for pending invoices** using **Python, Gmail SMTP, and Excel data**.  
Easily manage **invoice follow-ups** and **automate payment reminders** without manual effort.

## 📌 Features
✅ **Automated Email Reminders** – Sends invoice payment reminders based on the **reminder date**  
✅ **Excel Integration** – Reads customer invoice details from an **Excel file**  
✅ **Gmail SMTP Support** – Uses **Gmail SMTP** to send emails  
✅ **Secure Credentials Handling** – Uses **`.env` file** for storing sensitive data  
✅ **Windows Compatible** – Designed for **Windows users**  
✅ **Future Improvement Ready** – Can be automated to **run on startup**  

---

## 🎯 Purpose
This script helps businesses **automate invoice reminders** by:  
📩 **Checking an Excel file** for pending payments  
📆 **Sending emails on the correct reminder date**  
💰 **Reminding clients to pay before due dates**  

Say goodbye to **manual follow-ups**! 🚀

---

## 📂 Excel File Structure (`invoice_data.xlsx`)
Your Excel file should be formatted as follows:

| Email                  | Name      | Invoice No | Amount (Rs.) | Due Date  | Reminder Date | Has Paid |
|------------------------|-----------|------------|-------------|------------|---------------|-----------|
| example@email.com     | John Doe  | INV-1001   | 2500.00     | 2025-02-10 | 2025-02-07    | no        |
| client@domain.com     | Alice Lee | INV-1002   | 5000.00     | 2025-02-15 | 2025-02-10    | yes       |

📌 **Important Notes**:  
- `Reminder Date` → The script **sends an email only on this date**.  
- `Has Paid` → If set to `"no"`, the script will send a reminder.  

---

## 💾 Installation & Setup
### **1️⃣ Install Dependencies**
Ensure **Python 3.8+** is installed, then run:

```sh
pip install pandas openpyxl smtplib python-dotenv
```

### **2️⃣ Setup `.env` File (Credentials)**
Since **email credentials are sensitive**, we use a `.env` file to store them **securely**.

#### 📌 **Create a `.env` file** in the project folder and add:
```ini
EMAIL=your-email@gmail.com
PASSWORD=your-app-password
```
❌ **Do NOT share or upload `.env` to GitHub!** (It is ignored in `.gitignore`)

---

## ▶️ How to Run the Script
1. **Ensure `invoice_data.xlsx` is correctly formatted**  
2. Open **Command Prompt** and navigate to the project folder:
   ```sh
   cd path/to/your/project
   ```
3. Run the script:
   ```sh
   python email_sender.py
   ```
✅ If invoices match today's **reminder date**, emails will be sent.

---

## 🚀 Automating on Windows Startup
To **run this script automatically on startup**, follow these steps:

### **1️⃣ Using Task Scheduler**
1. Open **Task Scheduler** in Windows.
2. Click **Create Basic Task**.
3. Set **Trigger** → **At Startup** (or a fixed time daily).
4. Set **Action** → **Start a program**.
5. Browse and select **`python.exe`** as the program.
6. Add script path:  
   ```sh
   C:\path\to\your\script\email_sender.py
   ```
7. Click **Finish** and **Enable Task**.

📌 **This will run the script automatically when your computer starts!** 🚀

---

## 🔮 Future Improvements
🔹 **Attach PDF Invoices** to emails  
🔹 **Track Email Status** (Sent, Delivered, Opened)  
🔹 **Log Sent Emails in Excel**  
🔹 **Send SMS Reminders** for non-email customers  
🔹 **Deploy on a Cloud Server** for 24/7 automation  

---

## 📝 License
This project is **open-source** – feel free to modify and improve!  
⭐ If you found this useful, **give it a star on GitHub!** 🚀

