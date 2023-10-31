# Password validator 
The code within this repository checks basic password validation based on the password being inputted. 
A valid password should meet the following criteria:

1. Have more than 8 characters
2. Contains a capital letter
3. Contains a lowercase
4. Contains a number
5. Contains an underscore

### Running the password_validator.py
To run the password_validator.py first change directory into the `validator` folder e.g. `cd src/validator` and run the following command `python password_validator.py` you will now be prompted to enter a password. If the password does not meet the criteria mentioned above a message will be printed stating the password is incorrect and if the password does meet the criteria mentioned above a message will be printed stating the password is correct.

### Running the tests using pytest
To run the pytests change directory into the `tests` folder e.g. `cd src/tests` and run the following command `pytest password_validator.py`