from Utils import SCORES_FILE_NAME as scoresText
from flask import Flask ,render_template


myfile= open(scoresText)
score = myfile.read()


app = Flask(__name__)


@app.route('/')
def about():
    try:
        return render_template('about.html',SCORE = score )
    except:
        return render_template('error.html',ERROR = "error" )

    #return open(scoresText).read(), 200
#
# @app.route('/score')
# def score():
#     return open(scoresText).read(), 200

if __name__ == '__main__':
    #app.run('0.0.0.0', debug=True, port=30001)
    app.run(debug=True, host='0.0.0.0' , port=5002)