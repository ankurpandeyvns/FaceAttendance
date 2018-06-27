from flask import *
#from func import recognizer
from camera import *
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    data = ''
    try:
        if request.method == "POST":
            if request.form.get["click"] == "click":
                redi('/there')
    except Exception as e:
        data = str(e)
    return render_template('index.html')

@app.route('/a')
def getthere():
    return 'Working'

def redi(a):
    a += 'abd'
    return redirect(a)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)