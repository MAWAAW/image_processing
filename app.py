import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tif'])

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
currentImage = ''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Fonctions executant nos filtres
def filtreMedian():
    if currentImage != '':
        os.system("python scriptFilters/median.py static/uploads/"+currentImage)

def filtreConvolution():
    if currentImage != '':
        print 'execute filtre convolution...'

# La page de base
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global currentImage
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            currentImage = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('entry.html')

# Views des differents filtres
@app.route('/median', methods=['GET', 'POST'])
def median():
    if request.method == 'POST':
        print 'avant json'
        taille = int(request.json['taille'])
        print type(taille)
        bord = str(request.json['bord'])
        print type(bord)
        print 'apres json'
        #filtreMedian()
    return render_template('med.html', currentImage=currentImage)

@app.route('/convolution', methods=['GET', 'POST'])
def convolution():
    if request.method == 'POST':
        filtreConvolution()
    return render_template('conv.html', currentImage=currentImage)

# Lancement du serveur web
if __name__ == '__main__':
    app.run(debug=True)

