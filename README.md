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

### Authentication (IN DEVELOPMENT)