from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("index.html" )  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        f.save(f.filename)
        em = "sad"
        if em == "sad":
            return render_template("success.html", name = f.filename)
        elif em == "Happy":
            return render_template("Happy.html", name = f.filename)
        
  
if __name__ == '__main__':  
    app.run(debug = True)  