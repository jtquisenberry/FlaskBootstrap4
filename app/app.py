from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from model import Product

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
    return render_template('product.html', products=data)

@app.route('/api/product/<int:id>', methods=['GET', 'POST', 'DELETE'])
def product2(id):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product WHERE id=?", (id,))
        record = cursor.fetchone()
        product = {'id':record[0], 'name':record[1], 'color':record[2], 'quantity':record[3]}
        conn.close()
        return jsonify(product)
    if request.method == 'DELETE':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        result = cursor.execute("DELETE FROM product WHERE id=?", (id,))
        row_count = result.rowcount
        conn.close()
        return jsonify({'success': True})



@app.route('/api/product', methods=['GET'])
def get_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/api/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    color = data['color']
    quantity = data['quantity']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (name, color, quantity) VALUES (?, ?, ?)", (name, color, quantity))
    conn.commit()
    conn.close()
    return jsonify({'success': True})




@app.route('/product0')
def product0():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    data = cursor.fetchall()
    conn.close()
    return render_template('product0.html', data=data, products=[(3, "a", "b", 4)])


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
