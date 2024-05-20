# c4_logo_putter
Add the C4ADS logo to all the images in a directory. 

Steps: 

1. You will have to download this code into a directory, and in that same directory, have all the images saved in a folder called 'logoless'. Make sure that the images are directly inside 'logoless' and not in a folder inside logoless.
2. Run `chmod +x run_add_logo.sh`
3. Depending on if you want to add the logo with the tagline or not, you will have to run the command:
`python add_logo.py logoless --tagline` if you want the tagline or
`python add_logo.py logoless` if you don't want it. 
