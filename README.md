# Chronicle Communication Platform

## System Architecture
[Architecture diagram](https://drive.google.com/file/d/1XqRkv4ltWBj-5-_mxwlPVSHzXbB6aaFq/view?usp=sharing) \
Note: The diagram is a high level breakdown of services, but does not include detail on dependencies (i.e. Databases), messaging brokers (i.e. Kafka), and infrastructure (i.e Server, Lambda, etc)
## Running Locally
1. If you would like to test the communication feature to send an email, fill in `sender_email` and `sender_password`
environment variables in `docker-compose.yml`.
2. The email needs to be a valid gmail. Ensure this [account setting](https://myaccount.google.com/lesssecureapps) is set to ALLOW
2. `docker-compose up`\
This will instantiate a local postgres db with sample data and run a flask server on port 5000 .

## API Endpoints
Base API prefix: **/chronicle**
1. Users
    * **GET** **/users**, **/users/{userId}**
    * **POST** **/users**. Sample payload:
        ```
        {
            "firstName": "Greatest",
            "lastName": "Ever",
            "email": "test@gmail.com",
            "phone": "4128004543",
            "companyId": 1,
            "accountId": 1234563349,
            "groupId": 1
        }
        ```
2. Groups
    * **GET** **/groups**, **/groups/{groupId}**
    * **POST** **/groups**. Sample payload:
        ```
        {
            "description": "The main target demographic of Company 1",
            "companyId": 1
        }
        ```
3. Messages
    * **GET** **/messages**, **/messages/{messageId}**
    * **POST** **/messages**. Sample payload:
        ```
        {
            "message": "The main target demographic of Company 1",
            "companyId": 1,
            "groupId": 1,
            "channelType": "EMAIL"
        }
        ```
    * **PUT** **/messages**. Sample payload:
        ```
        {
            "messageId": 1,
            "message": "Hi :first_name,\n\nThis is a test email to remind you your minimum payment is due for :account_id by tomorrow.\n\n- Chronicle",
            "companyId": 1,
            "groupId": 1,
            "channelType": "EMAIL",
            "active": true
        }
        ```
4. Communication - to send specified message to users of the specified group via email
    * **POST** **/communication**. Sample payload:
        ```
        {
            "messageId": 1,
            "companyId": 1,
            "groupId": 1,
            "channelType": "EMAIL"
        }
        ```
     
        