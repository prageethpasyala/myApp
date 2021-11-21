

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name2>")
def home(name2):
   return render_template("index.html" , content= name2)
if __name__ == '__main__':
   app.run(debug=True∏)