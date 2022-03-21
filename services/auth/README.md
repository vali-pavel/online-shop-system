### Install
`pipenv shell
pipenv install
`
### Run api
`uvicorn main:app --port 8000 --reload`

### docker
Required variables:
- `SECRET_KEY` Secret key required to sign and decode the auth token 
- `ALGORITHM` used to sign the auth token with a specific algorithm
