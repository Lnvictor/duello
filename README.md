# duello

Knowledge battle Web Application written in django framework


## Setup

You can install the dependencies with poetry...
```bash
poetry update
```
Then set the following settings in your .env file
```py
# DATABASE Configuration
# DATABASE_URL=
DEBUG=
SECRET_KEY=

# JWT Configuration
JWT_PUBLIC_KEY=
JWT_EXPIRES_IN=3600
```

Then set the JWT_PRIVATE_KEY as a environment variable (doesnt works in .env because \n)
```bash
export JWT_PRIVATE_KEY=<YOUR_PRIVATE_KEY>
```

Apply the database migrations

```bash
python manage.py migrate
```

Populate users roles

```bash
python manage.py populate_user_roles
```

Running...

```
python manage.py runserver
```

## Routes

Brief API routes Definitions

### Authentication
The authentication flow was developed using Two Factor authentication. So first of all, you have to register a 
user to login in the platform:

 - /auth/signup [POST]

    Payload: 
    ```json
        {
            "user_name": "Victor",
            "user_last_name": "Pereira",
            "user_email": "vh141299@gmail.com",
            "password": "your_password"
        }
    ```

Then to be an active user, you have to verify your email, you can do this sendind a token for your email by the following endpoint:

- /auth/send_confirmation_email [POST]

    Payload:
    ```json
        {
            "destinatary":"your_mail@host.com"
        }
    ```

After this, you will receive a token in your email, to verify your user you must send a request to the following endpoint: 

- /auth/verify_code [POST]
    Paayload
    ```json
        {
            "user_mail": "<user_mail>"
            "code": "<code_received>"
        }
    ```

Finally, you can login [You can login even without verfify the email, to get acess_token and use in mail_verification requests]:

- /auth/login [POST]
    Payload: 
    ```json
        "user_name": "username",
        "password": "password"
    ```


### Cages

[####### IN DEVELOPMENT #######]