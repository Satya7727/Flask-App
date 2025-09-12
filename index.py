from flask import Flask,render_template,request
import mysql.connector
from mysql.connector import Error

def create_connection():
  connection = mysql.connector.connect(
  host="localhost",
  database="mini_project",
  user="root",
  password="Prince@8423"
)
  return connection

app = Flask(__name__)

# Index page
@app.route("/")
def root():
  return render_template("login.html")

# Login page
@app.route("/login")
def login():
  return render_template("login.html")

# About page
@app.route("/about")
def about():
  return render_template("about.html")

# Regiter page
@app.route("/register")
def register():
  return render_template("signup.html")

# Enquiry page
@app.route("/enquiry")
def enquiry():
  return render_template("Enquiry.html")

# Contact page
@app.route("/contact")
def contact():
  return render_template("contact.html")

# Home page
@app.route("/home")
def home():
   return render_template("Home.html")

# Projects page
@app.route("/projects")
def project():
   return render_template("Project.html")

# Logout
@app.route("/logout")
def logout():
  return render_template("login.html")

@app.route("/enquiry",methods=["POST"])
def enquiry_save():
   conn = create_connection()
   cursor = conn.cursor()
   name = request.form["name"]
   email = request.form["email"]
   property_id = request.form["property_id"]
   message = request.form["message"]
   try:
      query = "INSERT INTO enquiries (name, email,message,property_id) VALUES (%s, %s, %s,%s)"
      values = (name,email,message,property_id)
      cursor.execute(query,values)
      conn.commit()
      return render_template("Home.html")
   except Error as e:
      return f"Error: {e}"
   finally:
      cursor.close()
      conn.close()


# Login request
@app.route("/home", methods=["POST"])
def login_post():
    conn = create_connection()
    cursor = conn.cursor()
    username = request.form["username"]
    password = request.form["password"]

    try:
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return render_template("Home.html")
        else:
            return "Invalid username or password!"
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        conn.close()

# Signup request
@app.route("/signup", methods=["POST"])
def signup():
    conn = create_connection()
    cursor = conn.cursor()
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        return "Passwords do not match!"

    try:
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        cursor.execute(query, values)
        conn.commit()
        return render_template("Home.html")
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__": 
  app.run(debug=True)  