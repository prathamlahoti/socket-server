## Simple socket-based web-server
Application functionality is similar to a simple low-based web-server. It just handles user requests to the server and sends them back a server response
using web-socket components. The file structure is split to:
 1. _settings.py_ script, where HTTP-information for the server are stored;
 2. _templates_ folder, where HTML-views for users are stored;
 3. _views.py_ script is a view manager. This file just reads HTML-views out;
 4. _main.py_ script is our server runner and request handler.
 
**Server components are built via python3.6, So be sure, that you use exactly this version of python or higher(Sorry for my dummy typing)**

`python3.6 main.py` command allows you to run the server. Once server is ran, it's ready to receive all incoming requests.
So you can easily open your browser and test it out, following to [localhost] (http://localhost:5000). However, console request implementation is
also available. Examples are displayed below.

There are 2 available routes in our application to test its functionality(both are GET):
1. `/` - home route;
2. `/post` - post route.

You'll get *404 Page*, following to nonexistent routes. However, it's a part of the process.

To test, how our application reacts to another HTTP-methods, you can use the examples below.

**Be sure, that curl utility is installed on your machine.**

#### Sending request via curl
First of all, we must run the server.

`python3.6 main.py`

`curl -i -X GET http://localhost:50007/` - to send GET-request to the server

`curl -d "" -X POST http://localhost:50007/` - to send empty POST-request

`curl -X DELETE http://localhost:50007/` - to send DELETE-request


