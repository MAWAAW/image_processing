import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tif'])

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
imageCourante = ''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Fonctions executant nos filtres
def filtreMedian():
    if imageCourante != '':
        os.system("python scriptFilters/median.py static/uploads/"+imageCourante)

def filtreConvolution():
    if imageCourante != '':
        print 'execute filtre convolution...'

# La page de base
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global imageCourante
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            imageCourante = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('entry.html')

# Views des differents filtres
@app.route('/median', methods=['GET', 'POST'])
def median():
    if request.method == 'POST':
        filtreMedian()
    return render_template('med.html', imageCourante=imageCourante)

@app.route('/convolution', methods=['GET', 'POST'])
def convolution():
    if request.method == 'POST':
        filtreConvolution()
    return render_template('conv.html', imageCourante=imageCourante)

# Lancement du serveur web
if __name__ == '__main__':
    app.run(debug=True)

