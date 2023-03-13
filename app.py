from Flask import Flask, render_template
app = Flask(__name__)   

db={"number":0}

@app.route('/')
def cookieeee():
    return render_template("Index.html", number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return render_template("Index.html", number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return render_template("Index.html", number=db['number'])
  
app.run(host='127.0.0.1', port=5000)