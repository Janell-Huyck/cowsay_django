# cowsay_django
This program is just an enhancement of the "command-line toy" cowsay.  
Cowsay is a classic python module that simply echos back a user's text in the form of a speech-bubble
being said by an ascii-art cow or other animal.

This django app saves the users' "moos" as they are entered into a text box, and renders them in
cowsay, using the cow animal only.  A list of the last ten "moos" can be seen at /history, as 
linked on the index page.

The farm photo is courtesy of Pixabay, and I tried to arrange it so that it looked like the "cow"
that was speaking was standing in the pasture.

This was a cute little project that used the Python subprocess command to retrieve a Cowsay response, and
the \<pre\> and \<\\pre\> HTML tags to render it on the screen.
