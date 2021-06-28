In this repository, I've attached the two HW files:
  - exec1.py
  - exec2.py

--------------Explanation of exec1.py:--------------

This file contains the solution for the first HW assignment - "Magic List".
In order to use the class:
1. Create a MagicList() object. For example:
    arr = MagicList()
2. Add values to the list the following way: arr[0] = 2, for example.
3. You may only insert to indexes: 0 - len(arr) as those were the requierements. For example:
    arr = MagicList()
    arr[0] = 23 (correct)
    arr[1] = 10 (correct)
    arr[50] = 1 (incorrect, will raise an exception with an appropriate message)
4. There is no need to install any module.
5. I've left a few code lines that test the class for debugging purposes.


--------------Explanation of exec2.py:--------------

This file contains the solution for the second HW assignment - "API Testing".
In order to run the tests, first, clone the following repository https://github.com/polyrize/interview-server and follow the instructions to run the server.
Also install the following modules:
1. unittest (For the tests)
2. requests (For the API requests)

After connecting the server and installing the modules, you may run the tests by running the python file.

The scenarios I've tested:
1. Correct connection to the API
2. Incorrect connection to API with incorrect username
3. Try to insert a valid PolyData
4. Try to insert invalid empty data
5. Try to insert invalid non-empty data
6. Try to retrieve existing data
7. Try to retrieve non existing data with id -1
8. Try to insert a Polydata with wrong valtype - int

A bug I've found:
- You are able to insert data with wrong valType as shown in test no. 8
