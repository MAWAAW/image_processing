import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tif'])
CURRENT_IMAGE = ''

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Fonctions executant nos filtres
def filtreMedian(image_name,size,style):
    if image_name != '':
        os.system("python scriptFilters/median.py static/uploads/"+image_name)
        print 'TAILLE:'+str(size)+' STYLE:'+style

def filtreConvolution():
    if CURRENT_IMAGE != '':
        print 'execute filtre convolution...'

# La page d'acceuil
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global CURRENT_IMAGE
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            CURRENT_IMAGE = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('index.html')

# View du filtre median
@app.route('/median', methods=['GET', 'POST'])
def median():
    if request.method == 'POST':
        size = int(request.json['size'])
        style = str(request.json['style'])
        filtreMedian(CURRENT_IMAGE, size, style)
        return jsonify({'image_name':CURRENT_IMAGE})
    return render_template('med.html', currentImage=CURRENT_IMAGE)

# View du filtre de convolution 2D
@app.route('/convolution', methods=['GET', 'POST'])
def convolution():
    if request.method == 'POST':
        filtreConvolution()
    return render_template('conv.html', currentImage=CURRENT_IMAGE)

# Lancement du serveur web
if __name__ == '__main__':
    app.run(debug=True)

# Nettoyage du dossier uploads quand on ferme le serveur
for fileName in os.listdir(UPLOAD_FOLDER):
    os.remove(UPLOAD_FOLDER+"/"+fileName)
