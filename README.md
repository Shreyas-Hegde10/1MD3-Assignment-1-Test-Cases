# 1MD3 Assignment 1 - Test Cases

This repository contains **Pytest test cases** for all five functions in the **1MD3 Assignment #1**. These tests are designed to help students validate their implementations and ensure their code works correctly under various scenarios. This repo is a work in progress so please let me know if I've made any mistakes or not. 


---

## Included Test Functions

The test file covers the following functions:

1. **`is_valid_number(num)`**  
   Checks whether a given string represents a valid number (integer or decimal).  

2. **`is_valid_term(term)`**  
   Checks whether a string represents a valid algebraic term.  

3. **`approx_equal(x, y, tol)`**  
   Determines if two numbers are approximately equal within a specified tolerance.  

4. **`degree_of(term)`**  
   Verifies if the degree of a given algebraic term was provided correctly

5. **`get_coefficient(term)`**  
   Checks if the coefficient was obtained correctly  

Each function is tested against **valid inputs, invalid inputs, edge cases, and boundary cases** to ensure robustness.

---

## 🛠 Usage

1. **Install pytest using a terminal.**
```
pip install pytest
```

2. **Change the import statements to your respective file name and functions.** 

3. **Run the test file in the same project folder as your assignment file.**
```
pytest <name of your test file>
```

4. **After running the test file, the number of failed cases and passed cases should be outputted at the end of the test scenario.**
<img width="675" height="49" alt="image" src="https://github.com/user-attachments/assets/702b242b-a031-443d-97a7-ea4718d29e5c" />
