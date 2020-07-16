from flask import Flask,render_template,request
from diabetes import prediction

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():

	if request.method == "POST":
		Pregnancies = request.form['Pregnancies']
		Glucose = request.form['Glucose']
		BloodPressure = request.form['BloodPressure']
		SkinThickness = request.form['SkinThickness']
		Insulin	 = request.form['Insulin']
		Bmi    = request.form['Bmi']
		DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
		Age   = request.form['Age']

		diabetes = prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age)

		return render_template('prediction.html',diabetes=diabetes)
	return render_template('prediction.html')


if __name__ == "__main__":
	app.run(debug=True)















































































