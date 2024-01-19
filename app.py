from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import wget
from src.effects import oreo, mercury, alchemy, wacko, unstable, ore, contour, snicko, indus, spectra, molecule, lynn,\
    download
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'VintageLab'


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


# Home Page of Vintage
@app.route('/')
@app.route('/home')
def home():
    path = 'static/images/trash/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path + x))
    # Sorting as per image upload date and time
    print(uploads)
    # uploads = os.listdir('static/uploads')
    uploads = ['images/trash/' + file for file in uploads]
    uploads.reverse()
    return render_template('home.html', uploads=uploads)


# About Page of Vintage
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html')


app.config['UPLOAD_PATH'] = 'static/images/trash/'


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect("/")


eff_img = ''
effected = ''


@app.route('/effects', methods=['GET', 'POST'])
def effects():
    if request.method == 'POST':
        global eff_img
        global effected
        print("Entered Post")
        if request.form['button'] == 'Upload' and request.form['path'] != '' and request.files['local_file'].filename \
                == '':
            path = request.form['path']
            a = path.split('/')
            previous = os.getcwd()
            eff_img = previous + '/static/images/trash/' + a[len(a) - 1]
            if os.path.isfile(previous + '/static/images/trash/' + a[len(a) - 1]):
                return render_template('effects.html', image_filename='../static/images/trash/' + a[len(a) - 1])
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            image_filename = wget.download(path)
            os.chdir(previous)
            return render_template('effects.html', image_filename='../static/images/trash/' + image_filename)

        elif request.form['button'] == 'Upload' and request.form['path'] == '' and request.files[
            'local_file'].filename != '':
            f = request.files['local_file']
            previous = os.getcwd()
            eff_img = previous + '/static/images/trash/' + f.filename
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            f.save(secure_filename(f.filename))
            os.chdir(previous)
            return render_template('effects.html', image_filename='../static/images/trash/' + f.filename)

        elif request.form['button'] == 'Oreo' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            oreo(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Mercury' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            mercury(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Alchemy' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            alchemy(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Wacko' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            wacko(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Unstable' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            unstable(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Ore' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            ore(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Contour' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            contour(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Snicko' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            snicko(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Indus' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            indus(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Spectra' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            spectra(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        elif request.form['button'] == 'Molecule' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            molecule(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')


        elif request.form['button'] == 'Lynn' and eff_img != '':
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            lynn(eff_img)
            os.chdir(previous)
            if eff_img.count('jpeg') > 0 or eff_img.count("jpg") > 0:
                effected = folder + 'intermediate.jpg'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.jpg')
            elif eff_img.count('png') > 0:
                effected = folder + 'intermediate.png'
                return render_template('effects.html', image_filename='../static/images/trash/intermediate.png')
            else:
                return render_template('effects.html')

        else:
            eff_img = ''
            effected = ''
            flash("Oops Something went wrong !")
            return render_template('effects.html')

    return render_template('effects.html')


# Main function-----
if __name__ == '__main__':
    app.run(debug=False, port=3000)
