# c4_logo_putter
Add the C4ADS logo to all the images in a directory. 

Steps: 

1. You will have to download this code into a directory, and in that same directory, have all the images saved in a folder called 'logoless'. Make sure that the images are directly inside 'logoless' and not in a folder inside logoless.
2. Find out the location of where you downloaded and unzipped the file by clicking on 'get info' and copying the path. Open Terminal, write `cd` and paste the path. Then hit enter.
3. Paste `chmod +x run_add_logo.sh` and hit enter. Then paste `./run_add_logo.sh` and hit enter. You may have to enter your password and follow other installation instructions. This will run a file that will install Python and other related software needed for doing this.
4. Depending on if you want to add the logo with the tagline or not, you will have to run the command:
`python add_logo.py logoless --tagline` if you want the tagline or
`python add_logo.py logoless` if you don't want it. 
