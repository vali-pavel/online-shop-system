### Install
`pipenv shell
pipenv install
`
### Run api
`uvicorn main:app --port 8001 --reload`

### docker
Required variables:
- `MYSQL_USER` MySql user
- `MYSQL_PASS` MySql password
- `SECRET_KEY` Secret key required to sign and decode the auth token
