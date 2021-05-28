# csit314-project
Create an automated test of a software

Requirements:
- Develop a software testing tool
- follow Test Driven Development methodology
- tool must support automated:
    - execution of the software under test
    - randomly generated test cases
    - predefined test cases
    - result checking
    - test report generation

Software tested:
API being tested is https://api.mathjs.org

How to run the testing tool:
```
# Install the python package manager pip to satisfy our dependancies
python -m pip install --upgrade pip

# Run pip install on the requirments file
pip install -r requirements.txt
          
# Run the python code
python main.py > test-report.txt
```
