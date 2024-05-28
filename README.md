#    USER CREDENTIAL MANAGEMENT SYSTEM 

The Credential Management System (CMS) is a comprehensive software solution designed to streamline the management of user credentials within an application or system. In today's digital landscape, where user authentication and security are paramount, the CMS serves as a crucial component in ensuring the integrity and confidentiality of user data. 

The CMS encompasses various functionalities, including user registration, username retrieval, and password reset. Through an intuitive and user-friendly interface, users can securely create accounts, retrieve forgotten usernames, and reset passwords, thereby minimizing the risk of unauthorized access and enhancing user experience.

# Introduction

The project begins with users filling out their details in the personal registration form. After submission, users can register for an account. Upon successful registration, users proceed to the login screen, where they can input their credentials to access the platform's features. Forgot password and username functionalities are available for users who need to retrieve or reset their login credentials, enhancing security and user access control.

# Skills

**Tkinter**  
**Python**  
**SQL**  
**Password Hashing**


# Key features of the Credential Management System include:

**User registration:** Allows new users to create accounts securely.  
**Username retrieval:** Enables users to recover their usernames using recovery email addresses or other predefined methods.  
**Password reset:** Facilitates the secure resetting of passwords in case of forgotten or compromised credentials.  
**Security enhancements:** Implements robust security measures, such as hashing of passwords so that only the user knows it.

# Overview of creating personal registration form
[Personal Registration form](https://github.com/vineeth191004/Login-Credentials-of-a-user/blob/main/Personal_Registration_form.py) code is a Python script for creating a personal registration form GUI using the Tkinter library. Below is a breakdown and analysis of the code:

1. **Importing Necessary Modules**:
   - The script imports required modules such as Tkinter for GUI, PIL (Python Imaging Library) for image manipulation, messagebox for displaying alerts, pymysql for database connectivity, and re for regular expression operations.

2. **Creating Tkinter Window**:
   - The `Tk()` method is used to create a Tkinter window with the title "Personal Registration Form" and a fixed size.

3. **Defining Functions**:
   - `bck()`: This function is called when the back button is clicked. It destroys the current window and imports the "Login_screen" module.
   - `submit()`: This function is invoked when the submit button is clicked. It validates the user inputs and inserts data into the database if all conditions are met.
   - `show1()`, `hide1()`, `show2()`, `hide2()`: These functions are used for showing and hiding password characters and are linked to corresponding check buttons.

4. **Database Operations**:
   - The `submit()` function includes logic to connect to a MySQL database using pymysql, validate user inputs, create a database and table if they don't exist, and insert registration data into the table.

5. **GUI Layout**:
   - Various Tkinter widgets such as Labels, Entries, Radiobuttons, OptionMenu, and Buttons are used to design the registration form.
   - Widgets are placed within a Frame to organize and manage the layout effectively.

6. **Input Validation**:
   - Input validation is performed using conditional statements and regular expressions to ensure that the user enters valid data.

7. **Password Security**:
   - Password strength is checked to ensure it meets certain criteria (length, inclusion of digits, uppercase letters, and lowercase letters).
   - Passwords are hashed using MD5 before storing them in the database.

8. **Check Buttons for Password Visibility**:
   - Check buttons are provided to toggle the visibility of the password fields.

9. **Mainloop**:
   - The `mainloop()` method is called to run the Tkinter event loop, allowing the user to interact with the GUI.

It provides a basic registration form with input validation and database integration. It can be further enhanced with additional features such as email verification, stronger password hashing algorithms, and improved error handling.

![Screenshot 2024-03-19 005934](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/6cd811d8-7352-47af-968a-77118f857fdf)

![image](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/ce9f06d5-02f4-4f51-9a73-26de3117dafe)

![image](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/dc976ca2-8d79-42f5-b53f-a1889b8a79dd)


# Overview of Login screen 

This Python script [Login_Screen](https://github.com/vineeth191004/Login-Credentials-of-a-user/blob/main/Login_screen.py) represents a simple login screen GUI application created using the Tkinter library. Here's an overview of its functionality:

1. **Login Screen Interface**:
   - The application displays a login screen with fields for entering email and password.
   - It also provides options for creating a new account, resetting the password, and recovering the username.

2. **Email and Password Validation**:
   - It checks if the email and password fields are filled before attempting to log in.
   - Password strength is verified to ensure it meets certain criteria, such as length and character types.

3. **Database Connectivity**:
   - The application connects to a MySQL database for authentication purposes. It queries the database to check if the entered email and password match any records.

4. **Forgot Password Functionality**:
   - Users can request a password reset by clicking the "forgot password" button. An email containing the new password is sent to the registered email address.

5. **Base64 Encoding**:
   - The script encodes the email and password using Base64 before sending them over the network for added security.

6. **Error Handling**:
   - It provides error messages for incorrect login credentials and password strength requirements.

7. **Navigation**:
   - Upon successful login, the application navigates to the next page, represented by the "Management_system" module.

8. **UI Customization**:
   - The GUI is customized with background colors, images, and button styles to enhance the user experience.

This Login_screen is linked to a personal registration form, likely for a larger system where users can register accounts and then log in using the provided credentials. It incorporates security measures such as password hashing and Base64 encoding to protect user information. Additionally, it offers functionality for password recovery and new account creation. Overall, it provides a basic yet functional login interface for users.

![image](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/de4b8f4c-25bd-444e-9845-4efa8b348e1c)

# Overview of Forgot Username and password

**Forgot Username Functionality**:

 - Users can recover their forgotten username by providing associated information, such as school name, University name.
-  A verification process is typically involved to confirm the user's identity.
- Upon successful verification, the username is sent to the user's registered email address or displayed on-screen.

**Forgot Password Functionality**:

- Users who forget their password can initiate a password reset process.
- This process usually involves verifying the user's identity through school name, university name or security questions.
- After successful verification, users can set a new password securely.

- ![image](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/8bb38cf9-96e6-4137-b00d-e642e0fadace)

- ![image](https://github.com/vineeth191004/Login-Credentials-of-a-user/assets/142156630/00a2113a-a1ce-4837-b581-1976810bb6cb)








