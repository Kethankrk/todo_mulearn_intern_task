# Todo REST API
API for managing todo items

## Version: 1.0.0

### /api/login/

#### POST
##### Summary:

Login route to get refresh and access token

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |

### /api/register

#### POST
##### Summary:

Register a new user

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 500 | Internal server error |

### /api/todo

#### GET
##### Summary:

Get all todos for the authenticated user

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query | ID of the todo to retrieve (optional) | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### POST
##### Summary:

Create a new todo

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### DELETE
##### Summary:

Delete a todo

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### PATCH
##### Summary:

Update a todo

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

### /api/make-done

#### POST
##### Summary:

Mark a todo as done

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |
