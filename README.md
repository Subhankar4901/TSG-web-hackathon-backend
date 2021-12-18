# TSG Website Hackathon 2021

[![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)&nbsp;&nbsp;[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)&nbsp;&nbsp;[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)&nbsp;&nbsp;[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

---

## Description

This repository is  dedicated to the backend development of [TSG website hackathon 2021](https://www.facebook.com/149405445074499/posts/5141129255902068/?sfnsn=wiwspmo).\
Problem statement : [Drive link](https://drive.google.com/file/d/1Hmfomj7pa0o8AZonzxC0O0GNTPU0PjgW/view?fbclid=IwAR3blZJKVqI7TEWhgyeEpWbDzsE45Qd4RtYsEMozzhE77MimnCQs-y66Pio)

---

## Contribution

Make a new branch for each issue and then open pull request to check if there is any conflict.
Then merge.

---

## APIs

The list of APIs are -
(also present in the thunderclient collection file in this repo)

```
1. /login/student/sendotp -
	desc: sends otp to spec email.
	request: {"email": ""}
	response: {"message": ""}

2. /login/official/auth -
	desc: auth login via username and password, returns message with token and user type on successful login.
	request: {	"username": "tsg_official","password":"123#abc%$pq"}
	response:
	upon successful login, status code 200
	{
		"message": "user authenticated",
		"token": "",
		"user_type": 4
	}
	upon unsuccessful login attempt, status code 401
	{
		"message": ""
	}

	token data format:
	{
		"id": 14,
		"type": 4,
		"username": "tsg_official"
	}

3. complaints/getcomplaints -
	desc : GET request that returns list of complaints according to access level.
	Params
	token : the JWT token with the following payload
	{
		"id": 15,
		"type": 3,
		"username": "soc_governor"
	}
	
	Response 
	Successful try (Status 200)
	{
		"complaints": [
				{
					"attachment": null,
					"date": "Wed, 15 Dec 2021 14:08:56 GMT",
					"description": "Can I create a complain",
					"id": 1, 
					"remarks": "pending",
					"userid": 17
				},
				{
					"attachment": null,
					"date": "Wed, 15 Dec 2021 12:13:29 GMT",
					"description": "I can't set events",
					"id": 2,
					"remarks": "In Review",
					"userid": 15
				}
			],
		"message": "Success"
	}
	
	Failure try (status 401)
	{
		"message": "Unauthorised"
	}
	here id in response is the complain id.
4. 

```

---

## Format of files 

The files should be sent as encoded string in the request body.

```
	with open("test.pdf", "rb") as pdf_file:
	    encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")
```

The files are returned as string buffers. To get the files back, do the following -
	
	with open("file.pdf", "wb") as f:
		buff = base64.b64decode(file.encode('utf-8'))
		f.write(buff)
	

---

## Our backend Team

| Name | Position | Contact |
| :----: |:----: |:----:|
|[Subhankar Halder](https://github.com/Subhankar4901)| Backend Developer |[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/subhankar.haldar.75839)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/subhankar-halder-8797131b1/)|
|[Ashutosh Patkar](https://github.com/Holmes7) | Backend Developer |[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/profile.php?id=100009143155236)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashutosh-patkar/)|
|[Shobhit Gupta](https://github.com/shobhit10058) | Fullstack Developer |[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/Shobhit10058/)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shobhit-gupta-437790191/)|
|[Anurag Singh](https://github.com/Godzilla5111)|Frontend developer|[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/profile.php?id=100038065373916)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anurag5111/)|
|[Aryan Singh](https://github.com/ary1733)|Fullstack Developer|[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/profile.php?id=100001841974713)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mr-aryan/)|
|[Adarsh](https://github.com/adarshares)|Fullstack Developer|[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/adarsh.ares.39566)|
