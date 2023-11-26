from app import app
from fpdf import FPDF
from config import mysql
from flask import Response, render_template
import MySQLdb.cursors

@app.route('/')
def upload_form():
    return render_template('download.html')


@app.route('/download/report/pdf')
def download_report():

    cursor = None
    try:

        #conn = mysql.connect()
        #cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute("SELECT *FROM user_info")
        result = cursor.fetchall()

        pdf = FPDF()
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'Employee Data', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width / 4

        pdf.ln(1)

        th = pdf.font_size

        for row in result:
            pdf.cell(col_width, th, str(row['id']), border=1)
            pdf.cell(col_width, th, row['name'], border=1)
            pdf.cell(col_width, th, row['email'], border=1)
            pdf.cell(col_width, th, row['password'], border=1)
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- end of report -', align='C')

        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                        headers={'Content-Disposition': 'attachment;filename=employee_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        #conn.close()


if __name__ == "__main__":
    app.run()