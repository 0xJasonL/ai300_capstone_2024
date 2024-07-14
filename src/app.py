from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)

THRESHOLD = 0.2900731077110065

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)

        tenure_months = float(form_input['tenure_months'])
        contract_type  = str(form_input['contract_type'])
        num_dependents  = int(form_input['num_dependents'])
        num_referrals  = int(form_input['num_referrals'])
        total_monthly_fee  = int(form_input['total_monthly_fee'])

        model_inputs = [tenure_months,
                        contract_type,
                        num_dependents,
                        num_referrals,
                        total_monthly_fee
                        ]

        prediction = Model().predict(model_inputs)[1].astype('float')

        if prediction >= THRESHOLD:
            prediction = 'This user is a churn risk.'
        else:
            prediction = 'This user is NOT a churn risk.'
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()

    tenure_months = float(request_data['tenure_months'])
    contract_type  = str(request_data['contract_type'])
    num_dependents  = int(request_data['num_dependents'])
    num_referrals  = int(request_data['num_referrals'])
    total_monthly_fee  = int(request_data['total_monthly_fee'])

    model_inputs = [tenure_months,
                contract_type,
                num_dependents,
                num_referrals,
                total_monthly_fee
                ]

    prediction = Model().predict(model_inputs)[1].astype('float')

    if prediction >= THRESHOLD:
        prediction = 1
        text = 'This user is a churn risk.'
    else:   
        prediction = 0
        text = 'This user is NOT a churn risk.'
    print(prediction)
    return {'success': True,'churn_status':text,'churn_label':prediction}, 200

if __name__ == '__main__':
    app.run(debug=True)
