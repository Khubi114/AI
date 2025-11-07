import requests
import json

BASE_URL = httplocalhost8000

def test_health()
    Test health check
    response = requests.get(f{BASE_URL}health)
    print(Health Check, response.json())

def test_predict()
    Test prediction endpoint
    test_data = {
        inputText This is a suspicious message that needs analysis,
        numericFeature 42.5
    }
    
    response = requests.post(
        f{BASE_URL}predict,
        json=test_data
    )
    
    if response.status_code == 200
        print(Prediction Result)
        print(json.dumps(response.json(), indent=2))
    else
        print(fError {response.status_code})
        print(response.json())

def test_model_info()
    Test model info endpoint
    response = requests.get(f{BASE_URL}model-info)
    print(Model Info, response.json())

if __name__ == __main__
    print(=== Testing API ===n)
    
    test_health()
    print(n)
    
    test_model_info()
    print(n)
    
    test_predict()