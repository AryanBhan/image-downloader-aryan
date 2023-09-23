# An Web App Build for Developer by Aryan Bhan
#     You Can Search and Download as per Dimension
from flask import Flask, render_template, send_file,request
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    global response
    global url
    global name
    error_message=None
    name="dog"
    url="https://loremflickr.com/640/400/dog"
    if request.method=='POST':
        name=request.form['name']
        if ' ' in name:
            name=name.replace(' ','')
        if not name.isalpha():
            error_message="Enter a valid image name, Else default Image will be Shown!!"
            name="dog"
        else:
            name=name.lower()
            dimention=request.form['dimention']
            dilimiters=[',','x',' ']
            for i in dilimiters:
                if i in dimention:
                    dili=i
                    break
            if ',' in dimention or 'x' in dimention or ' ' in dimention:
                x,y=dimention.split(dili)
            else:
                x,y='640','400'
        
            url=f"https://loremflickr.com/{x}/{y}/{name}"
        
    response = requests.get(url)
    return render_template('base.html',name=name,error_message=error_message)

@app.route('/get_image')
def get_image():
    return send_file(BytesIO(response.content), mimetype='image/jpeg')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
