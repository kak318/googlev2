from flask import Flask, render_template, request

app = Flask('app')
r = ['hello']

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/s', methods=['GET', 'POST'])
def res():
  data = request.form['q']
  ts = []
  for i in range(len(r)):
    print(r[i])
    q = data in r[i]
    if q:
      ts.append(str(r[i]))
  print(ts)

  rnum = len(ts)

  return render_template("res.html", rnum=rnum, q=data, ts=ts)

app.run(host='0.0.0.0', port=8080, debug=False)