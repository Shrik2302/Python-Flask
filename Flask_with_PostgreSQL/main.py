from flask import Flask, jsonify, render_template, Response
from flask_mail import Mail,Message
from fpdf import FPDF
from dotenv import load_dotenv
import psycopg2
import datetime
import os


load_dotenv()

# PostgreSQL Database credentials loaded from the .env file
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")



app = Flask(__name__)
# CORS implemented so that we don't get errors when trying to access the server from a different server location
# CORS(app)
app.config['MAIL_SERVER']=os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False # os.getenv('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = True # os.getenv('MAIL_USE_SSL')

mail = Mail(app)


try:
    con = psycopg2.connect(
        database=DATABASE,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        )

    cur = con.cursor()

    # GET: Fetch all movies from the database
    @app.route('/data')
    def fetch_all_movies():
        cur.execute('SELECT * FROM person')
        rows = cur.fetchall()
        #print(rows)
        return jsonify(rows)


    @app.route('/billOfMaterial')
    def bill_of_material():
        msg = Message('Material List', sender=('Shrikant Mane', os.getenv('SENDER_MAIL')),
                      recipients=[os.getenv('RECIEVER_MAIL')], )
        msg.html = render_template("billOfMaterial.html")
        with app.open_resource("Bill_Of_Material.pdf") as fp:
            msg.attach("Bill_OfMaterial.pdf", "/", fp.read())
        mail.send(msg)
        return "Success"


    @app.route('/download')
    def download():
        msg = Message('Bill Report', sender=('Shrikant Mane', os.getenv('SENDER_MAIL')),
                      recipients=[os.getenv('RECIEVER_MAIL')], )
        msg.html = render_template("Pdf_report.html")
        with app.open_resource("Final_Bill.pdf") as fp:
            msg.attach("Final_Bill.pdf", "/", fp.read())
        mail.send(msg)
        return "Success"


    @app.route('/report')
    def download_report():
        try:
            cur.execute("SELECT *FROM books")
            result = cur.fetchall()
            print(result)
            total = 0
            for data in result:
                total = total + data[4]
            cost = float(total) + 0.00

            headers = [('No', 'Book Name', 'Quantity', 'Unit Price', 'Total Price')]
            result = headers + result
            x = datetime.datetime.now()

            pdf = FPDF()
            pdf.add_page()

            page_width = pdf.w - 2 * pdf.l_margin

            pdf.set_font('Times', 'B', 14.0)
            pdf.cell(page_width, 0.0, 'Report Sample', align='C')
            pdf.ln(10)
            pdf.set_font('Times', 'B', 14.0)
            pdf.cell(page_width, 0.0, 'Customer Name: Shrikant Mane', align='C')
            pdf.ln(10)
            pdf.set_font('Times', 'B', 14.0)
            pdf.cell(page_width, 0.0, "Date: "+ x.strftime('%x'), align='L')
            pdf.ln(10)

            pdf.set_font('Courier', '', 12)

            col_width = page_width / 5

            pdf.ln(1)

            th = pdf.font_size

            for row in result:
                pdf.cell(col_width, th, str(row[0]), border=1)
                pdf.cell(col_width, th, row[1], border=1)
                pdf.cell(col_width, th, str(row[2]), border=1)
                pdf.cell(col_width, th, str(row[3]), border=1)
                pdf.cell(col_width, th, str(row[4]), border=1)
                pdf.ln(th)

            pdf.ln(10)

            pdf.set_font('Times', 'B', 14.0)
            pdf.cell(page_width, 0.0, "Total Cost: " + str(cost), align='R')
            pdf.ln(10)

            pdf.set_font('Times', '', 10.0)
            pdf.cell(page_width, 0.0, '- end of report -', align='C')

            return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                            headers={'Content-Disposition': 'attachment;filename=report.pdf'})

        except Exception as e :
            print(e)

except Exception as e:
    print(e)


@ app.route('/signup')
def index():
    msg = Message('Welcome to Easy Share', sender=('Shrikant Mane', os.getenv('SENDER_MAIL')),
                  recipients=[os.getenv('RECIEVER_MAIL')],)
    msg.html = render_template("Signup.html")
    mail.send(msg)
    return 'sent'


@app.route('/reset')
def reset():
    msg = Message('Reset your password .', sender=('Shrikant Mane', os.getenv('SENDER_MAIL')),
                  recipients=[os.getenv('RECIEVER_MAIL')],)
    msg.html = render_template("New_reset_password.html")
    mail.send(msg)
    return 'Reset password mail send'
