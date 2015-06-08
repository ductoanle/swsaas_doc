---
title: SalesWhale API Reference v.0.1

---

# Introduction

# APIs

## Requirements
- All request must have `client` to define where the request coming from (iOS/Android/Web). This requirement only applicable to requests under the `api` scope
- For request that require authorization, a combine of `authentication_token`, `timestamp` and `signature` will be required. Each `client` will be given a `secret` which can then be used to generate signature (combination of authentication_token, timestamp, secret and request url) for each request to API. The API can return stale timestamp for request that send timestamp earlier or later than 5 mins of the current time in server - a correct timestamp will be returned together with the stale timestamp error.


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

```shell
curl -d "username=test_user&email='test@saleswhale.io&password=asdfgh&password_confirmation=asdfgh" http://api.saleswhale.io/api/users/sign_up
```

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

### Accept Invite
- Add user as collaborator of an account
- Return status 201 on success

#### HTTP Request
`POST /api/accept_invite`

#### Query Parameters
Parameter | Optional | Description
----------|----------|-----------
invite_token | No | token to identify the invitation

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

```shell
curl -d "username=jonsnow&password=asdfgh" http://api.saleswhale.io/api/sessions/sign_in
```

<aside class="info">
This end point does not require user to login
</aside>

## Account
### Create Account
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

### Account Info
- Return account information

#### HTTP Request
`POST /api/accounts/:account_id/info`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
account_id | No | unique id of the account

#### Returned JSON
Name | Description
--------- | -------
name | Account Name
members | List of members (user_id and role) under this account

### Invite new user
- Return status 201 on success, error otherwise

#### HTTP Request
`POST /api/accounts/:account_id/invite`

#### Query Parameters
Parameter | Optional | Description
--------- | ------- | -----------
account_id | No | unique id of the account
name | No | name of the person to invite
email | No | email to check if the user already exist in saleswhale or to send invite email

## Google Auth

### Onboarding

#### HTTP Request
`/auth/google`
- Upon user allows permissions, will redirect back to onboarding page
- Pulling user's contact in the background