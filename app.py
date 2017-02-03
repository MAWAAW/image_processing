import os
import os.path
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tif'])
CURRENT_IMAGE = ''
NUM_IMAGE = 0

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Fonctions executant nos filtres
def filtreMedian(image_name,size,style,mode,noise_dosage,num):
    if image_name != '':
        os.system('python scriptFilters/median.py static/uploads/'+image_name+' '+str(size)+' '+style+' '+str(noise_dosage)+' '+mode+' '+str(num))
        print 'MEDIAN=> TAILLE:'+str(size)+' STYLE:'+style+' MODE:'+mode+' BRUIT:'+str(noise_dosage)

def filtreConvolution(image_name,size,style,num):
    if CURRENT_IMAGE != '':
        os.system('python scriptFilters/moyenneur.py static/uploads/'+image_name+' '+str(size)+' '+ style+' '+str(num))
        print 'MOYENNEUR=> TAILLE:' + str(size) + ' STYLE:' + style

def filtreGaussian(image_name,size,style,num):
    if CURRENT_IMAGE != '':
        os.system('python scriptFilters/gaussian.py static/uploads/'+image_name+' '+str(size)+' '+style+' '+str(num))
        print 'GAUSSIAN=> TAILLE:' + str(size) + ' STYLE:' + style

def filtreLee(image_name,size,style,num,mode,noise_dosage):
    if CURRENT_IMAGE != '':
        os.system('python scriptFilters/lee.py static/uploads/' + image_name + ' ' + str(size) + ' ' + style+' '+str(num)+' '+mode+' '+str(noise_dosage))
        print 'LEE=> TAILLE:' + str(size) + ' STYLE:' + style

# La page d'acceuil
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global NUM_IMAGE
    print NUM_IMAGE
    global CURRENT_IMAGE
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            CURRENT_IMAGE = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    else:
        #global NUM_IMAGE
        if NUM_IMAGE > 5:
            for fileName in os.listdir(UPLOAD_FOLDER):
                if fileName != CURRENT_IMAGE:
                    os.remove(UPLOAD_FOLDER + "/" + fileName)
            NUM_IMAGE = 0
        return render_template('index.html', currentImage=CURRENT_IMAGE)

# View du filtre median
@app.route('/median', methods=['GET', 'POST'])
def median():
    global NUM_IMAGE
    if request.method == 'POST':
        size = int(request.json['size'])
        style = str(request.json['style'])
        mode = str(request.json['mode'])
        noise_dosage = float(request.json['noise_dosage'])
        NUM_IMAGE = NUM_IMAGE + 1
        filtreMedian(CURRENT_IMAGE, size, style, mode, noise_dosage, NUM_IMAGE)
        return jsonify({'image_name':CURRENT_IMAGE.split(".")[0], 'image_num':NUM_IMAGE,'image_extension':CURRENT_IMAGE.split(".")[1]})
    return render_template('med.html', currentImage=CURRENT_IMAGE)

# View du filtre du moyenneur
@app.route('/convolution', methods=['GET', 'POST'])
def convolution():
    global NUM_IMAGE
    if request.method == 'POST':
        size = int(request.json['size'])
        style = str(request.json['style'])
        NUM_IMAGE = NUM_IMAGE + 1
        filtreConvolution(CURRENT_IMAGE, size, style, NUM_IMAGE)
        return jsonify({'image_name': CURRENT_IMAGE.split(".")[0], 'image_num':NUM_IMAGE, 'image_extension': CURRENT_IMAGE.split(".")[1]})
    return render_template('conv.html', currentImage=CURRENT_IMAGE)

# View du filtre de gaussian
@app.route('/gaussian', methods=['GET', 'POST'])
def gaussian():
    global NUM_IMAGE
    if request.method == 'POST':
        size = int(request.json['size'])
        style = str(request.json['style'])
        NUM_IMAGE = NUM_IMAGE + 1
        filtreGaussian(CURRENT_IMAGE, size, style, NUM_IMAGE)
        return jsonify({'image_name': CURRENT_IMAGE.split(".")[0], 'image_num':NUM_IMAGE, 'image_extension': CURRENT_IMAGE.split(".")[1]})
    return render_template('gaussian.html', currentImage=CURRENT_IMAGE)

# View du filtre de lee
@app.route('/lee', methods=['GET', 'POST'])
def lee():
    global NUM_IMAGE
    if request.method == 'POST':
        print 'POST LEEEEEEEE'
        size = int(request.json['size'])
        style = str(request.json['style'])
        mode = str(request.json['mode'])
        noise_dosage = float(request.json['noise_dosage'])
        NUM_IMAGE = NUM_IMAGE + 1
        filtreLee(CURRENT_IMAGE, size, style, NUM_IMAGE, mode, noise_dosage)
        return jsonify({'image_name': CURRENT_IMAGE.split(".")[0], 'image_num':NUM_IMAGE, 'image_extension': CURRENT_IMAGE.split(".")[1]})
    return render_template('lee.html', currentImage=CURRENT_IMAGE)

# Lancement du serveur web
if __name__ == '__main__':
    app.run(debug=True)

# Nettoyage du dossier uploads quand on ferme le serveur
for fileName in os.listdir(UPLOAD_FOLDER):
    os.remove(UPLOAD_FOLDER+"/"+fileName)
