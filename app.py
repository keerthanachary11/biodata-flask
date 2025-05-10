from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def biodata():
    # Personal details 
    name = "keerthana chary" 
    age = 19
    university = "Osmania University"  
    course = "Bachelor in Engineering"  
    department = "Artifical Intelligence & Data Science"
    email = "keerthanachary123@gmail.com"  
    social_media = ": linkedin.com/in/k-keerthana-chary-935b762a0"  

    return render_template('biodata.html', name=name, age=age, university=university, 
                           course=course, department=department, email=email, social_media=social_media)

if __name__ == '__main__':
    app.run(debug=True)
