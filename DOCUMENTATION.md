# API Documentation

This document provides detailed information about the REST API for managing people resources.

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
   - [Create a New Person](#create-a-new-person)
   - [Retrieve Person Details](#retrieve-person-details)
   - [Update Person Details](#update-person-details)
   - [Delete a Person](#delete-a-person)
3. [Standard Request and Response Formats](#standard-request-and-response-formats)
4. [Sample API Usage](#sample-api-usage)
5. [Known Limitations and Assumptions](#known-limitations-and-assumptions)
6. [Setting Up and Deploying the API](#setting-up-and-deploying-the-api)

## Introduction
This API allows you to perform CRUD operations on people resources. You can create, retrieve, update, and delete person records.

## Endpoints

### Create a New Person

- HTTP Method: POST
- URL: /api/people/
- Request Body:
  json
  {
      "name": "New Person",
      "email": "new@example.com",
      "gender": "male",
      "address": "123 Test St"
  }

Expected Response:
Status Code: 201 CREATED

Response Body (Sample):
json
{
    "id": 4,
    "name": "New Person",
    "email": "new@example.com",
    "gender": "male",
    "address": "123 Test St"
}


### Retrieve Person Details

HTTP Method: GET
URL: /api/people/<id>/

Expected Response:
Status Code: 200 OK

Response Body (Sample):
json

{
    "id": 4,
    "name": "New Person",
    "email": "new@example.com",
    "gender": "male",
    "address": "123 Test St"
}


### Update Person Details

HTTP Method: PUT
URL: /api/people/<id>/

Request Body:
json

{
    "name": "Updated Name",
    "email": "updated@example.com",
    "gender": "female",
    "address": "456 Updated St"
}

Expected Response:
Status Code: 201 CREATED

Response Body (Sample):
json

{
    "id": 4,
    "name": "Updated Name",
    "email": "updated@example.com",
    "gender": "female",
    "address": "456 Updated St"
}


### Delete a Person

HTTP Method: DELETE
URL: `/api/people/<id>/`

Expected Response:
Status Code: 204 No Content


### Standard Request and Response Formats
All API requests and responses follow the JSON format.


### Sample API Usage
Here are some sample API usage scenarios:

Creating a new person.
Retrieving person details by ID.
Updating person details.
Deleting a person
