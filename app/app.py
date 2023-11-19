from flask import Flask, render_template, request, redirect
import sqlite3
from product import Product

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    data = cursor.fetchall()
    conn.close()
    return render_template('product.html', data=data, products=[(3, "a", "b", 4)])



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        quantity = request.form['quantity']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('UPDATE Product SET name=?, color=?, quantity=? WHERE id=?', (name, color, quantity, id))
        conn.commit()
        conn.close()
        return redirect('/product')
    else:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Product WHERE id=?', (id,))
        product = c.fetchone()
        conn.close()
        return render_template('update.html', product=product)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM Product WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/product')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        quantity = request.form['quantity']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO Product (name, color, quantity) VALUES (?, ?, ?)', (name, color, quantity))
        conn.commit()
        conn.close()
        return redirect('/product')
    else:
        return render_template('add.html')

@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product WHERE id=?", (id,))
    data = cursor.fetchone()
    conn.close()
    return render_template('view.html', product=data)




if __name__ == '__main__':
    app.run(debug=True)