from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def	index():

	
	return render_template('sample.html')

@app.route('/<name>')
def	index2(name):
    
    for i in range(len(str(name))-1):
        if(not name[i].isalnum() and (name[i] != '_')):
            if(not name[i+1].isalnum() and name[i+1] != '_'):
                
                return error_403()
    path = os.path.abspath('.')+"/pages/" + str(name)
    if (os.path.exists(path)):
 
        file = open(path)
        Read = file.read()
        file.close()
        return Read
        	
    else:
        return error_404()
    

@app.errorhandler(404)
def error_404():
	
	return render_template('404.html',name = 404)

@app.errorhandler(403)
def error_403():
	
	return render_template('403.html', name = 403)




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

	