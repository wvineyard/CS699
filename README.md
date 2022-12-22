# CS699

This project primary utilizes jupyter notebooks in VSCode to give students relevant real-time feedback on exercises. It uses jupyter and IPython’s “magic” modules to take a students code, and runs it to check if the solution is correct, and if not, return relevant feedback. Additionally, the foundations have been built to send all submissions to a webserver, so that I may (a) verify problems are well worded and at a level applicable to the students working on it and (b) change feedback areas to be even further relevant, or possibly leverage ML techniques to have more accurate and personalized feedback for the student. 


To run:
1. Running Setup.sh will create a venv and install all current packages. 
2. Open any of the notebooks, and run the first two cells, which loads the extension and adds a name/email to the student. 
3. Run any cell with %%ITS to run the code and get feedback.
