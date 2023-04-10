document.addEventListener('DOMContentLoaded', () => {
    // Select the form and the submit button
    const form = document.querySelector('form');
    const submitButton = form.querySelector('button[type="submit"]');

    // Select the email and password fields
    const emailField = form.querySelector('input[name="email"]');
    const passwordField = form.querySelector('input[name="password"]');
    const confirmPasswordField = form.querySelector('input[name="confirm_password"]');

    // Regular expressions for email and password validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,16}$/;

    // Function to check whether the email is valid
    function isEmailValid(email) {
        return emailRegex.test(email);
    }

    // Function to check whether the password is valid
    function isPasswordValid(password) {
        return passwordRegex.test(password);
    }

    // Function to disable the submit button
    function disableSubmitButton() {
        submitButton.disabled = true;
    }

    // Function to enable the submit button
    function enableSubmitButton() {
        submitButton.disabled = false;
    }

    // Function to check whether all fields are valid and enable/disable the submit button accordingly
    function validateFields() {
        const email = emailField.value;
        const password = passwordField.value;
        const confirmPassword = confirmPasswordField.value;
        const isEmailFieldValid = isEmailValid(email);
        const isPasswordFieldValid = isPasswordValid(password);
        const isConfirmPasswordFieldValid = password === confirmPassword;

        if (isEmailFieldValid && isPasswordFieldValid && isConfirmPasswordFieldValid) {
            enableSubmitButton();
        } else {
            disableSubmitButton();
        }
    }

    // Validate fields on keyup and change events
    emailField.addEventListener('keyup', validateFields);
    passwordField.addEventListener('keyup', validateFields);
    confirmPasswordField.addEventListener('keyup', validateFields);
    confirmPasswordField.addEventListener('change', validateFields);

    // Disable the submit button by default
    disableSubmitButton();

});