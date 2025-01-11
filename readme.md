# 404B Lesson 6 Class Project - Name Predictor

## Explore the APIs

- Agify.io ([Doc](https://agify.io/)):

  - Predict the **age** of a person based on his/her name.
  - Sample url: <https://api.agify.io?name=harry>
  - Sample result:

    ```json
    {
        "age": 72,
        "count": 26070,
        "name": "harry"
    }
    ```

- Genderize.io ([Doc](https://genderize.io/)):
  - Predict the **gender** of a person based on his/her name.
  - Sample URL: <https://api.genderize.io?name=harry>
  - Sample result:

    ```json
    {
        "count": 177229,
        "gender": "male",
        "name": "harry",
        "probability": 1.0
    }
    ```

- Nationalize.io ([Doc](https://nationalize.io/)):
  - Predict the **nationality** of a person based on his/her name.
  - Sample URL: <https://api.nationalize.io?name=harry>
  - Sample result:

    ```json
    {
        "country": [
                {
                    "country_id": "NL",
                    "probability": 0.087
                },
                {
                    "country_id": "GB",
                    "probability": 0.062
                },
                {
                    "country_id": "AU",
                    "probability": 0.041
                },
                {
                    "country_id": "ID",
                    "probability": 0.04
                },
                {
                    "country_id": "NZ",
                    "probability": 0.035
                }
        ],
        "name": "harry"
    }
    ```

## Your Task

Write a program accepts an input from user (his/her name), send the name to the APIs above and display the result.

## Sample Input

`Your name: felix ⏎`

## Sample Output

`You are probably a 52 years old male from GH.`
