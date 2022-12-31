# MOPS Takehome Assessment: API Integration (python)

### *Summary*

Using python, I wrote a script that fetches data from 3 APIs, formats, manipulates and saves the data to a local data store, then sends the final results to an live endpoint.

### *High level of what the script should do:*

_Script function will be named `lambda_handler`, taking its name from AWS Lambda which we use extensively._

1. Function receives a JSON payload containing an email:
    
    ```json
    {
      "email": "john@acompany.com"
    }
    ```


2. Fetch results from these 3 APIs (see “API Resources” below):
    - agify.io
    - genderize.io
    - nationalize.io
    
3. Store the results in a local data store with the following attributes:
    
    ```
    name (string)
    email (string)
    domain (string)
    topLevelName (string)
    age (integer)
    gender (string)
    nationality (string)
    ```

4. Perform data quality procedures:
    * Remove all individuals named Craig from the database.
    * Update age to 26 and nationality to Bosnia of all individuals named Kyle.
    * Do not include individual data from people with a Verkada email.

5. Query the database to find the first 3 youngest men over the age of 30.

6. Format the results to the provided endpoint in this format:
    
    ```json
    {
      "name": "john",
      "email": "john@acompany.com",
      "domain": "acompany",
      "topLevelName": "com",
      "age": 71,
      "gender": "male",
      "nationality": "IE"
    }
    ```
7. Query the database to find the first 3 youngest men over the age of 30. Format the result in JSON format.

8. Send my name, queried data and database to the endpoint in the payload format below:


```
// api request payload format:
{
  "name": "YourName",
  "queryData": queryDataAsJSON,
  "databaseContents": dataBaseContentsAsJSON
}
```


