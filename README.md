# EF Test Note Taking REST API 

This repo contains the code and instructions for a REST API for a simple note taking application as part of the EF Coding challenge.

#### TechStack
The backend is coded entirely in Python. The key framework used is Flask, a micro framework to allow for quick an flexible design of micro services. 

All dependencies can be seen in the file `requirements.txt`.

Data is stored in a *noSQL*-esque DB called tinyDB, a document-oriented DB for python. 

---

## Files and Structure

- Dir: App => contains all application relevant files
- Dir: DB => contains the `db.json` file that serves as the database for tinyDB
- File: main.py => envokes the application
- File: config.py => contains config details on paths, etc.
- File: API_query.ipynb => Jupyter notebook providing code snippits to perform core interactions with API
- .flaskenv => constains runtime parameters to start the app


## SETUP

To get started...
1. clone the repo into your local directory
2. install all dependencies from `requirements.txt`
3. execute `flask run` via command line

**OR**

Deploy run and deploy the docker image


## How to use the API
No authentication is required for this API

#### Endpoints

`/api/v1`or `/`   
**Allowed Methods**: GET   
**Returns**: JSON object with `msg` and description of API   



`/api/v1/note/create/`   
**Description**: Creates a new note   
**Allowed Methods**: POST   
**Payload required**: content, title (optional, defaults to "New Note")      
**Returns**: JSON object with `msg` and *note id*, or `msg` with error


`/api/v1/note/get/`   
**Description**: Retrievs a single note for specific id
**Allowed Methods**: GET   
**Payload required**: id  
**Returns**: JSON object with note object, or `msg` with error


`/api/v1/note/list/`   
**Description**: lists all notes availale in DB
**Allowed Methods**: GET   
**Payload required**: None  
**Returns**: JSON object with all notes in DB, or `msg` with error


`/api/v1/note/edit/`   
**Description**: Edits a single note with new content
**Allowed Methods**: POST   
**Payload required**: id, content, title(optional)  
**Returns**: JSON object with `msg` of success or error


`/api/v1/note/delete/`   
**Description**: Deletes a note from the DB
**Allowed Methods**: DELETE   
**Payload required**: id  
**Returns**: JSON object with `msg` of success or error

