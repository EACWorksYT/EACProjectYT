# Import
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # get the selected image
        selected_image = request.form.get('image-selector')

        # Task #2. Receive text
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Task #3. Accept text position
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Task #3. Accepts text color
        selected_color = request.form.get('color-selector')
        selected_font = request.form.get('font-selector')

        return render_template('index.html', 
                               # Displays the selected image
                               selected_image=selected_image, 

                               #Task #2. Display text
                               text_top = text_top,
                               text_bottom = text_bottom,

                               #Task #3. Display color
                               selected_color = selected_color,
                               selected_font = selected_font,
                               
                               # Task #3. Displays the position of the text
                               text_top_y = text_top_y+'px',
                               text_bottom_y = text_bottom_y+'px',

                               )
    else:
        # Displays the first image by default
        return render_template('index.html', selected_image='EACLogoYT.jpg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
