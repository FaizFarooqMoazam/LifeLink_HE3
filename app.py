from flask import Flask, render_template, g, request, jsonify
import sqlite3  

  
app = Flask(__name__)  
  
DATABASE = 'db/resources.db'
TABLE = "table01"  
  
def get_db():  
    db = getattr(g, '_database', None)  
    if db is None:  
        db = g._database = sqlite3.connect(DATABASE)  
    return db  
  
@app.teardown_appcontext  
def close_connection(exception):  
    db = getattr(g, '_database', None)  
    if db is not None:  
        db.close()


def get_colors(sql_data):
    with_colors = []
    for entry in sql_data:
        as_list = list(entry)
        calc = entry[6] / 4294950
        if (calc < 6.5):
            icon = "r"
        elif calc < 10.5 and calc > 6.5:
            icon = "y"
        else:
            icon = "g"
        as_list.append(icon)
        with_colors.append(as_list)

    return with_colors

@app.route('/')
def home():  
    return "Hello, World!"  


  
@app.route('/data')  
def get_data():
    db = get_db()  
    cur = db.cursor()  
    cur.execute('SELECT * FROM table01')  
    data = cur.fetchall()  
    data_w_colors = get_colors(data)
    return render_template('data.html', data=data_w_colors)  


@app.route('/search')  
def search():  
    query = request.args.get('query')  
      
    conn = sqlite3.connect(DATABASE)  
    c = conn.cursor()  
      
    c.execute("SELECT * FROM table01 WHERE name LIKE ?", ('%' + query + '%',))  
    data = c.fetchall()  
      
    conn.close()  
      
    return jsonify(data)
  
if __name__ == '__main__':  
    app.run(debug=True)  
