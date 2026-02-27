from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from Schema.prediction_response import predictionResponse
from model.predict import model, MODEL_VERSION, predict_output

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "This is insurance premium API"}

# for AWS
@app.get("/health")
def health_check():
    return{
        "status" : "OK",
        "version" : MODEL_VERSION,
        "model_loded" : model is not None
    }

@app.post('/predict', response_model=predictionResponse)
def predict_premium(data: UserInput):

    input_df = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(input_df)

        return JSONResponse(status_code=200, content={
                                            'bmi': round(data.bmi, 2),
                                            'age_group': data.age_group,
                                            'lifestyle_risk': data.lifestyle_risk,
                                            'city_tier': data.city_tier,
                                            'income_lpa': data.income_lpa,
                                            'occupation': data.occupation,

                                            'predicted_category': prediction,
                                                                        
                                            })
    
    except Exception as e:
        return JSONResponse(status_code= 500, content={"message " : "internal servar error"})





