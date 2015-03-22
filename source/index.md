---
title: SalesWhale API Reference v.0.1

---

# Introduction

# APIs
## Users
### Sign Up
- The end point for new user sign up
- Return user's information upon success

#### HTTP Request
`POST /api/users/sign_up`
#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
username | No | Username
email | No | User's email
password | No | Password
password_confirmation | No | Password Confirmation

#### Returned JSON
Name | Description
--------- | -------
username |
email |
authentication_token | Required for later API calls

<aside class="info">
This end point does not require user to login
</aside>

### Show Profile
- The end point that will return information about the user
#### HTTP Request
`GET /api/users/:user_id/profile`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
user_id | No | ID of the user to return

#### Returned JSON
Name | Description
--------- | -------
username |
email |
authentication_token | Required for later API calls


## Session
### Create Session - Login
- The end point to let user login into SalesWhale

#### HTTP Request
`POST /api/sessions/sign_in`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
username | No | Username of the user
password | No | Password to login

#### Returned JSON
Name | Description
--------- | -------
username |
email |
authentication_token | Required for later API calls

<aside class="info">
This end point does not require user to login
</aside>

## Account
## Create Account
- User can create account after login

#### HTTP Request
`POST /api/accounts/create`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
name | No | Name of account to be created

#### Returned JSON
Name | Description
--------- | -------
name | Account Name
owner_id | Id of user who created the account
members | List of members (user_id) under this account

## Info
- Return account information

#### HTTP Request
`POST /api/accounts/info`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
name | No | Name of account to be created

#### Returned JSON
Name | Description
--------- | -------
name | Account Name
owner_id | Id of user who created the account
members | List of members (user_id) under this account
