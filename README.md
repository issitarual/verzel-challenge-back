# Verzel Back-End Challenge
## About 🔎
This is an API project for a car store website.
### Database diagram
![Untitled (2)](https://github.com/issitarual/verzel-challenge-back/assets/81389078/d2fdebb4-6992-4d69-87f4-78aef153349d)
### Implemented features ✅
- [x] Create user
- [x] Get users
- [x] Get user by id
- [x] Update user
- [x] Delete user
- [x] Create car
- [x] Get cars
- [x] Get car by id
- [x] Update car
- [x] Delete car
- [x] Create order
- [x] Get order
- [x] Create token
### Future improvements 🔮
- [ ] Add created_at and updated_at fields
- [ ] Add validations
- [ ] Add tests

## Technologies
The following tools and frameworks were used in the construction of the project:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## How to run
1. Clone this repository
2. Clone the [front-end repository](https://github.com/issitarual/verzel-challenge-front)
3. Follow instructions to run [front-end](https://github.com/issitarual/verzel-challenge-front)
4. Create a database using the ``dump.sql`` file inside the ``dump``
```bash
cd verzel-challenge-back
uvicorn main:app --reload
```
5. Access [Swagger UI](http://127.0.0.1:8000/docs#/) and create your admin user with POST/users route as the example:
```bash
{
  "email": "string",
  "password": "string",
  "name": "string",
  "isUserAdmin": true
}
```
Obs: The front-end application only creates not admin users. So, if you want to create, delete, or update a car, you'll have to create the user using the [Swagger UI](http://127.0.0.1:8000/docs#/) or another Rest API Client.
