import requests




def predict(name) -> dict:
    response = requests.get(f"https://api.agify.io?name={name}")
    response2 = requests.get(f'https://api.genderize.io?name={name}')
    response3 = requests.get(f'https://api.nationalize.io?name={name}')
    return {"age": response.json(), "gender": response2.json(), "nationality": response3.json()}



name = input("Your name?")
prediction = {}
prediction = predict(name)
result1 = prediction['age']['age']
result2 = prediction['gender']["gender"]
probabilitylist = prediction["nationality"]["country"]
maxVal = 0
maxKey = ""
for prob in probabilitylist:
    if prob["probability"] > maxVal:
        maxKey = prob["country_id"]
        maxVal = prob["probability"]

result3 = maxKey  




print(f'You are probably a {result1}-year-old who is {result2} and is from {result3}')