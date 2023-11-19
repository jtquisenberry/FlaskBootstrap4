from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

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


if __name__ == '__main__':
    app.run(debug=True)
