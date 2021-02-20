How to Use:

Add your raw protobuf from the network request to a file called test.txt.

I used Fiddler to get this using the HexView window. Make sure to disable "Show Headers" and "Show Offsets".
Then Select All and "Save Selected Bytes" to test.txt.

Request is as follows and was loaded for me on first app opening:

POST /api/1/syncSessionsProto HTTP/1.1

You can use a rooted Android device with XPosed and SSL Unpinning but likely just a device with the
Fiddler Root Cert and the Fiddler as a proxy would work too.

Next run main.py and it will convert the raw protobuff into a readable file. This can take a while. 
For a 30MB file I have taken multiple minutes. 

This will output a file buf1.txt which is a decoded protobuf in human readible form. This can get very large.
The 30MB input decoded to about 150MB so assume a similar 5x expansion. The library was included here as some
edits were made to decrease file size and to handle GPS coordinated properly.

Next run protobufparse.py to convert this into a set of GPX files. It will make a separate .gpx per session.