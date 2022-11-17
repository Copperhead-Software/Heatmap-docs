API
===

This is a fairly standard HTTP api. All you need is one request, pretty simple.

elements of each request:

``user``
just your username, pretty simple

``password``
just your password. as of v1, this is plaintext in the link and not encrypted. 

``UID``
this is your Unique ID, which we assign when you register.

``activity``
this is what activity your request will be sending. this will usually be your button name or link destination.

gateways:

``/dump/?UID=UID``
this is the gateway we use to populate the desktop app. you can get all the data populated by your users from here.

``/login/?user=USERNAME&password=PASSWORD``
this is the gateway we use to login. it will return a UID if the login is successful.

