# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import cv2
# import os
# import datetime

# app = Flask(__name__)

# # Secret key for session management
# app.secret_key = "supersecretkey"

# # Session configuration
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

# # Directory to save generated certificates temporarily
# OUTPUT_DIR = os.path.join(os.getcwd(), "output")
# if not os.path.exists(OUTPUT_DIR):
#     os.makedirs(OUTPUT_DIR)

# # Hardcoded credentials
# USER_CREDENTIALS = {
#     "admin": "password123",
# }

# # Login route
# @app.route("/", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#             session["username"] = username
#             return redirect(url_for("index"))
#         else:
#             return render_template("login.html", error="Invalid username or password.")
#     return render_template("login.html")

# # Logout route
# @app.route("/logout")
# def logout():
#     session.pop("username", None)
#     return redirect(url_for("login"))

# # Certificate Generator Home Page
# @app.route('/home')
# def index():
#     if "username" not in session:
#         return redirect(url_for("login"))
#     return render_template("index.html")

# @app.route('/generate', methods=['POST'])
# def generate_certificate():
#     if "username" not in session:
#         return redirect(url_for("login"))
#     try:
#         # Get form data
#         name = request.form.get("name").strip()
#         language = request.form.get("language").strip()
#         template_path = request.files.get("template")
        
#         if not name or not language or not template_path:
#             return "Error: All fields are required.", 400

#         # Save template temporarily
#         template_file = os.path.join(OUTPUT_DIR, "template.jpg")
#         template_path.save(template_file)
        
#         # Generate certificate
#         template = cv2.imread(template_file)
#         if template is None:
#             return "Error: Failed to load template image.", 400

#         # Add text to the certificate
#         dt = datetime.datetime.now()
#         cv2.putText(template, name, (766, 734), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
#         cv2.putText(template, str(dt.date()), (250, 1172), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
#         cv2.putText(template, language, (1238, 786), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

#         # Save generated certificate
#         output_path = os.path.join(OUTPUT_DIR, f"{name}.jpg")
#         if not cv2.imwrite(output_path, template):
#             return "Error: Failed to save the certificate.", 500

#         return send_file(output_path, as_attachment=True)

#     except Exception as e:
#         return f"Error: {e}", 500

# if __name__ == '__main__':
#     app.run(debug=True)


# import os
# import csv
# import cv2
# from flask import Flask, render_template, request, redirect, url_for, session
# import datetime

# app = Flask(__name__)
# app.secret_key = "supersecretkey"

# # Paths for directories
# DATA_FILE = os.path.join("data", "certificates.csv")
# UPLOAD_FOLDER = "uploads"
# CERTIFICATES_FOLDER = "certificates"

# # Ensure necessary directories exist
# os.makedirs("data", exist_ok=True)
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(CERTIFICATES_FOLDER, exist_ok=True)

# # Initialize CSV file with header if it doesn't exist
# def initialize_csv():
#     if not os.path.exists(DATA_FILE):
#         with open(DATA_FILE, mode="w", newline="") as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(["Name", "Email", "Programming Language", "Template Used", "Certificate Path"])
#             print(f"CSV file '{DATA_FILE}' created with headers.")

# initialize_csv()


# @app.route("/", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username == "admin" and password == "password123":
#             session["username"] = username
#             return redirect(url_for("index"))
#         else:
#             return render_template("login.html", error="Invalid username or password.")
#     return render_template("login.html")


# @app.route("/logout")
# def logout():
#     session.pop("username", None)
#     return redirect(url_for("login"))


# @app.route("/home")
# def index():
#     if "username" not in session:
#         return redirect(url_for("login"))
#     return render_template("index.html")


# @app.route("/generate", methods=["POST"])
# def generate_certificate():
#     if "username" not in session:
#         return redirect(url_for("login"))

#     # Get form data
#     name = request.form.get("name")
#     email = request.form.get("email")
#     language = request.form.get("language")
#     template_file = request.files["template"]

#     # Save the uploaded template
#     template_path = os.path.join(UPLOAD_FOLDER, template_file.filename)
#     template_file.save(template_path)

#     # Load the template using OpenCV
#     template = cv2.imread(template_path)

#     # Add text to the certificate
#     dt = datetime.datetime.now()
#     font = cv2.FONT_HERSHEY_COMPLEX
#     font_color = (0, 0, 255)  # Red color
#     thickness = 2

#     # Customize these positions based on your template
#     cv2.putText(template, name, (766, 734), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
#     cv2.putText(template, str(dt.date()), (250, 1172), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
#     cv2.putText(template, language, (1238, 786), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#     # Save the generated certificate
#     output_path = os.path.join(CERTIFICATES_FOLDER, f"{name}.jpg")
#     cv2.imwrite(output_path, template)

#     # Append data to the CSV file
#     with open(DATA_FILE, mode="a", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([name, email, language, template_file.filename, output_path])

#     return f"Certificate generated for {name} with email {email}!"


# if __name__ == "__main__":
#     app.run(debug=True)


import os
import csv
import cv2
import datetime
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Paths for directories
DATA_FILE = os.path.join("data", "certificates.csv")
UPLOAD_FOLDER = "uploads"
CERTIFICATES_FOLDER = "certificates"

# Ensure necessary directories exist
os.makedirs("data", exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CERTIFICATES_FOLDER, exist_ok=True)

# Initialize CSV file with header if it doesn't exist
def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Email", "Programming Language", "Template Used", "Certificate Path"])
            print(f"CSV file '{DATA_FILE}' created with headers.")

initialize_csv()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "password123":
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/home")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_certificate():
    if "username" not in session:
        return redirect(url_for("login"))

    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    language = request.form.get("language")
    template_file = request.files["template"]

    # Save the uploaded template
    template_path = os.path.join(UPLOAD_FOLDER, template_file.filename)
    template_file.save(template_path)

    # Load the template using OpenCV
    template = cv2.imread(template_path)

    # Add text to the certificate
    font = cv2.FONT_HERSHEY_COMPLEX
    font_color = (0, 0, 255)  # Red color
    thickness = 2
    dt = datetime.datetime.now()

    # Customize these positions based on your template
    cv2.putText(template, name, (766, 734), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(template, str(dt.date()), (250, 1172), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(template, language, (1238, 786), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Save the generated certificate
    output_path = os.path.join(CERTIFICATES_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)

    # Append data to the CSV file
    with open(DATA_FILE, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, language, template_file.filename, output_path])

    return f"Certificate generated for {name} with email {email}!"


@app.route("/send-emails", methods=["GET"])
def send_emails():
    try:
        # Read the CSV file
        data = pd.read_csv(DATA_FILE)

        # Email server setup
        server = sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("yashj17033@gmail.com", "Dada@91311")

        from_email = "yashj17033@gmail.com"
        subject = "Your Certificate"

        # Loop through each recipient
        for _, row in data.iterrows():
            name = row["Name"]
            email = row["Email"]
            certificate_path = row["Certificate Path"]

            # Create the email
            message = MIMEMultipart()
            message["Subject"] = subject
            message["From"] = from_email
            message["To"] = email

            # Email body
            body = f"Dear {name},\n\nCongratulations! Please find your certificate attached.\n\nBest regards,\nTeam"
            message.attach(MIMEText(body, "plain"))

            # Attach the certificate
            with open(certificate_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(certificate_path)}",
            )
            message.attach(part)

            # Send the email
            server.sendmail(from_email, email, message.as_string())

        server.quit()
        return "Emails with certificates have been sent successfully!"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
