from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model_pred=pickle.load(open('insurance_fd.pk','rb'))
ifd=pd.read_csv('clean_dataset.csv')

@app.route('/',methods=['GET','POST'])
def index():
    # 'TypeOfIncident', 'SeverityOfIncident', 'AuthoritiesContacted',
    # 'IncidentState', 'IncidentCity', 'NumberOfVehicles', 'BodilyInjuries',
    # 'Witnesses', 'AmountOfInjuryClaim', 'AmountOfPropertyClaim',
    # 'AmountOfVehicleDamage', 'InsuredGender', 'InsuredEducationLevel',
    # 'InsuredOccupation', 'InsuredHobbies', 'CapitalGains', 'CapitalLoss',
    # 'InsurancePolicyState', 'Policy_CombinedSingleLimit',
    # 'Policy_Deductible', 'PolicyAnnualPremium', 'UmbrellaLimit',
    # 'InsuredRelationship', 'ReportedFraud'
    TypeOfIncident = sorted(ifd['TypeOfIncident'].unique())
    SeverityOfIncident = sorted(ifd['SeverityOfIncident'].unique())
    AuthoritiesContacted = sorted(ifd['AuthoritiesContacted'].unique())
    IncidentState = sorted(ifd['IncidentState'].unique())
    IncidentCity = sorted(ifd['IncidentCity'].unique())
    NumberOfVehicles = sorted(ifd['NumberOfVehicles'].unique())
    BodilyInjuries = sorted(ifd['BodilyInjuries'].unique())
    Witnesses = sorted(ifd['Witnesses'].unique())
    InsuredGender = sorted(ifd['InsuredGender'].unique())
    InsuredEducationLevel = sorted(ifd['InsuredEducationLevel'].unique())
    InsuredOccupation = sorted(ifd['InsuredOccupation'].unique())
    InsuredHobbies = sorted(ifd['InsuredHobbies'].unique())
    InsurancePolicyState = sorted(ifd['InsurancePolicyState'].unique())
    Policy_CombinedSingleLimit = sorted(ifd['Policy_CombinedSingleLimit'].unique())
    UmbrellaLimit = sorted(ifd['UmbrellaLimit'].unique())
    InsuredRelationship = sorted(ifd['InsuredRelationship'].unique())

    return render_template('IFD_1.html',TypeOfIncident=TypeOfIncident, SeverityOfIncident=SeverityOfIncident,
                           AuthoritiesContacted=AuthoritiesContacted, IncidentState=IncidentState,
                           IncidentCity=IncidentCity, NumberOfVehicles=NumberOfVehicles,
                           BodilyInjuries=BodilyInjuries, Witnesses=Witnesses,
                           InsuredGender=InsuredGender, InsuredEducationLevel=InsuredEducationLevel,
                           InsuredOccupation=InsuredOccupation,InsuredHobbies=InsuredHobbies,
                           InsurancePolicyState=InsurancePolicyState,Policy_CombinedSingleLimit=Policy_CombinedSingleLimit,
                           UmbrellaLimit=UmbrellaLimit,InsuredRelationship=InsuredRelationship)

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    TypeOfIncident = request.form.get('TypeOfIncident')
    SeverityOfIncident = request.form.get('SeverityOfIncident')
    AuthoritiesContacted = request.form.get('AuthoritiesContacted')
    IncidentState = request.form.get('IncidentState')
    IncidentCity = request.form.get('IncidentCity')
    NumberOfVehicles = request.form.get('NumberOfVehicles')
    BodilyInjuries = request.form.get('BodilyInjuries')
    Witnesses = request.form.get('Witnesses')
    AmountOfInjuryClaim = request.form.get('AmountOfInjuryClaim')
    AmountOfPropertyClaim = request.form.get('AmountOfPropertyClaim')
    AmountOfVehicleDamage = request.form.get('AmountOfVehicleDamage')
    InsuredGender = request.form.get('InsuredGender')
    InsuredEducationLevel = request.form.get('InsuredEducationLevel')
    InsuredOccupation = request.form.get('InsuredOccupation')
    InsuredHobbies = request.form.get('InsuredHobbies')
    CapitalGains = request.form.get('CapitalGains')
    CapitalLoss = request.form.get('CapitalLoss')
    InsurancePolicyState = request.form.get('InsurancePolicyState')
    Policy_CombinedSingleLimit = request.form.get('Policy_CombinedSingleLimit')
    Policy_Deductible = request.form.get('Policy_Deductible')
    PolicyAnnualPremium = request.form.get('PolicyAnnualPremium')
    UmbrellaLimit = request.form.get('UmbrellaLimit')
    InsuredRelationship = request.form.get('InsuredRelationship')

    print(TypeOfIncident, SeverityOfIncident, AuthoritiesContacted,IncidentState,
          IncidentCity, NumberOfVehicles, BodilyInjuries,Witnesses, AmountOfInjuryClaim,
          AmountOfPropertyClaim, AmountOfVehicleDamage, InsuredGender, InsuredEducationLevel,
          InsuredOccupation, InsuredHobbies, CapitalGains, CapitalLoss,InsurancePolicyState,
          Policy_CombinedSingleLimit,Policy_Deductible, PolicyAnnualPremium, UmbrellaLimit,
          InsuredRelationship)
    prediction = model_pred.predict(
        pd.DataFrame(columns=['TypeOfIncident', 'SeverityOfIncident', 'AuthoritiesContacted','IncidentState',
          'IncidentCity', 'NumberOfVehicles', 'BodilyInjuries','Witnesses', 'AmountOfInjuryClaim',
          'AmountOfPropertyClaim', 'AmountOfVehicleDamage', 'InsuredGender', 'InsuredEducationLevel',
          'InsuredOccupation', 'InsuredHobbies', 'CapitalGains', 'CapitalLoss','InsurancePolicyState',
          'Policy_CombinedSingleLimit','Policy_Deductible', 'PolicyAnnualPremium', 'UmbrellaLimit',
          'InsuredRelationship'],
                            data=np.array([TypeOfIncident, SeverityOfIncident, AuthoritiesContacted,
                                            IncidentState,IncidentCity,NumberOfVehicles,BodilyInjuries,
                                           Witnesses,AmountOfInjuryClaim,AmountOfPropertyClaim,
                                           AmountOfVehicleDamage,InsuredGender,InsuredEducationLevel,
                                           InsuredOccupation,InsuredHobbies,CapitalGains,CapitalLoss,
                                           InsurancePolicyState,Policy_CombinedSingleLimit,
                                           Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,
                                           InsuredRelationship]).reshape(1, 23)))
    print(prediction)
    # return str(np.round(prediction[0],2))
    if prediction[0] == 0:
        return f"The Insurance Claim is Not Fraudulent"
    else:
        return f"The Insurance Claim is Fraudulent"


if __name__=='__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)

# print(python --version)


















