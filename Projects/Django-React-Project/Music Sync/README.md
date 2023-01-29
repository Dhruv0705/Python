# Music Sync
## A Full Stack Web Application for Collaborative Music Playing

Music Sync is a full stack web application that allows a group of users to experience a unified music experience. The system is developed using Python and Django for the backend, JavaScript and React for the frontend, and utilizing the Spotify Web API for music options.

### Features:

- Create and join rooms for group listening
- Room host feature for controlling music and providing access codes to guests
- Voting system for song skipping and guest control settings
- Utilizes the Spotify Web API for searching and controlling music playback
- OAuth authentication through the Authorization Code Flow for access to user's Spotify data
- REST principles and JSON data format for API requests

With Music Sync, users can experience an engaging and interactive music experience with friends, utilizing the latest technology for seamless control of music, anywhere in the world.

### Tech Stack:

- Backend: Python & Django, Django Rest Framework
- Frontend: JavaScript, React, Webpack & Babel, React Router, Material UI Components
- Spotify API - Authorization Code Flow for access to user's Spotify data

### Installation: 

To install the necessary components for Music Sync, run the following commands in the terminal:

- npm install @mui/icons-material --legacy-peer-deps
- npm install @mui/material @emotion/react @emotion/styled --legacy-peer-deps
- npm install @babel/core @babel/preset-env @babel/preset-react babel-loader react react-dom react-router-dom webpack webpack-cli
- npm install @emotion/react @emotion/styled

### Spotify API Integration: 

Music Sync utilizes the Spotify Web API for music options. To access Spotify data, the application uses OAuth authentication through the Authorization Code Flow. This flow involves redirecting the user to Spotify to authorize the application, then exchanging the authorization code for an access token, and optionally, a refresh token. The access token is used to make authorized requests to the Spotify API, while the refresh token can be used to obtain new access tokens.

### Best Practices: 

In terms of security, it is recommended to store the access and refresh tokens in a secure way, and to implement a token expiration mechanism. The Spotify API documentation provides detailed information on the available endpoints, sample code, and best practices for using the API.

### Conclusion: 

Music Sync is a collaborative music playing system that allows a group of people to control the music being played through unity, regardless of their local host. It utilizes the Spotify Web API to integrate a wide range of music options, and includes features such as room hosting, voting, and control settings. It also provides an engaging and interactive music experience for groups to enjoy together, utilizing the latest technology to allow users to come together and control the music seamlessly, regardless of their location.




Django Rest Framework
API Endpoints - send information to and create new entries in database
Webpack & Babel
React Router
URL Endpoints
POST Request
Material UI Components
Django Sessions
Update Django Models
React Components 
React Default Props
React Callbacks
Spotify API - Authorize,  Use Authorization , Access Token, API Request
Spotify Web API


installed components:

npm install @mui/icons-material --legacy-peer-deps
npm install @mui/material @emotion/react @emotion/styled --legacy-peer-deps
npm install @babel/core @babel/preset-env @babel/preset-react babel-loader react react-dom react-router-dom webpack webpack-cli
npm install @emotion/react @emotion/styled

This system allows for a unified music experience for a group of users, with features such as room hosting, voting and control settings. This system was designed to provide an engaging and interactive music experience for groups to enjoy music together utilizing the latest technology.
Developed and implemented a collaborative music playing system, allowing a group of people to control the music being played through unity, regardless of their local host. Utilized Spotify's 3rd party API to integrate a wide range of music options.
Implemented a "room host" feature which allows one person to control the music and give out a code for others to join the room and listen in.
Incorporated a voting system for guests to skip songs, and provided the host with the ability to set controls for guests.
Created an engaging and interactive music experience for groups, utilizing the latest technology to allow users to come together and control the music seamlessly, regardless of their location.
Users will be able to leave, join, create a room 
The Spotify Web API allows developers to access Spotify's music and user data, such as searching for music, retrieving information about a user's playlists, and controlling playback. The API uses REST principles and returns data in JSON format. It requires authentication via an OAuth token, which can be obtained through the Authorization Code Flow or Implicit Grant Flow. The API also includes a Web Playback SDK for building web-based Spotify players. The documentation provides detailed information on the available endpoints, sample code, and best practices for using the API. The user grants permission for an application to access their Spotify data. The flow involves redirecting the user to Spotify to authorize the application, then exchanging the authorization code for an access token, and optionally, a refresh token. The access token is used to make authorized requests to the Spotify API, while the refresh token can be used to obtain new access tokens.

Spotify:
React JS to build a simple web application that interacts with the Spotify API. This will include creating a React component that allows the user to search for songs and albums, and displaying the results in a list.
building a full-featured web application that interacts with the Spotify Web API using Django and React.
cover the best practices of securing the access and refresh tokens, such as storing them in a secure way and implementing a token expiration mechanism.

Control user music , fast forward, pause, whateveer we want contorl over the music requireing two things from spotify 
register web application with spotify using spotify api in where every user using the application that grants access 
we authenticate our application with spotify then the user authenercitate our application
Application 

