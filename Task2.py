

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('invoice_processing_db.sqlite')
cursor = conn.cursor()

# Create a table for storing invoices
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_name TEXT,
        amount REAL,
        status TEXT
    )
''')
conn.commit()

def get_invoices():
    cursor.execute('SELECT * FROM invoices')
    return cursor.fetchall()


@app.route('/')
def display_invoices():
    invoices = get_invoices()
    return render_template('invoices.html', invoices=invoices)


@app.route('/process_invoice/<int:invoice_id>')
def process_invoice(invoice_id):
    # Add processing logic here (e.g., validate data, update status)
    cursor.execute('UPDATE invoices SET status = ? WHERE id = ?', ('Approved', invoice_id))
    conn.commit()
    return redirect(url_for('display_invoices'))


@app.route('/capture_invoice', methods=['GET', 'POST'])
def capture_invoice():
    if request.method == 'POST':
        vendor_name = request.form['vendor_name']
        amount = float(request.form['amount'])

       

       
        cursor.execute('INSERT INTO invoices (vendor_name, amount, status) VALUES (?, ?, ?)',
                       (vendor_name, amount, 'Pending'))
        conn.commit()

        return redirect(url_for('display_invoices'))

    return render_template('capture_invoice.html')

if __name__ == '__main__':
    app.run(debug=True)
