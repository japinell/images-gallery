# Image Gallery Application

## Project Goal

This is a full-stack web application developed with React and Python and deployed to docker containers that allows a user to retrieve images from https://unsplash.com by entering a search criteria. The application allows saving, deleting, and retrieving the image metadata from a MongoDB database.

On the frontend, the application is built with React and react-bootstrap and axios packages for building the user interaction. The backend is built with Python and flask, request,and pymongo packages to interact with the MongoDB database.

## User Story

```
AS A photography enthusiast
I WANT to find images from unsplash.com by entering a search keyboard
SO THAT I can use them as inspiration for my photography projects
```

## Acceptance Criteria

```
WHEN I open the web application
THEN I am provided with a search form
WHEN I input the search criteria and click the search button
THEN I am presented with images matching my search criteria
WHEN I click on the save button
THEN The image's metadata is saved to a database for future retrieval
WHEN I click on the delete button
THEN The image's metadata is deleted from the database
WHEN I refresh the web application next time
THEN The application loads the images which metadata I saved before
```

## Collaborators

- `Jose A Pinell` @ https://github.com/japinell

This project is inspired on Bogdan Stashchuk's "Full Stack Web Development Bootcamp with Reach and Python" found in https://www.oreilly.com.

## Copyright

All licenses in this repository are copyrighted by the respective authors listed above. Contact the authors if you want a copy of the repository.
