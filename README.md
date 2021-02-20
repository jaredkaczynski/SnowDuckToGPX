How to Use:

Add your raw protobuf from the network request to a file called test.txt.

I used Fiddler to get this using the HexView window. Make sure to disable "Show Headers" and "Show Offsets".
Then Select All and "Save Selected Bytes" to test.txt.

Next run main.py and it will convert the raw protobuff into a readable file. This can take a while. 
For a 30MB file I have taken multiple minutes.

This will output a file buf1.txt which is a decoded protobuf in human readible form.

Next run protobufparse.py to convert this into a set of GPX files. It will make a separate .gpx per session.