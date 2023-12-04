let password = document.getElementById('password');
// console.log(password);
let generateBtn = document.getElementById('generateBtn');
let copyBtn = document.getElementById('copyBtn');
// console.log(copyBtn);

//Function to generate 12 random password

function generatePassword(){
    let characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // set a value for length of our password
    let passwordLength = 12;

    // Declare an empty string that will store our password.
    let passwordString = "";

    // Loop through our characters string 12 times
    for (let i = 0; i < passwordLength; i++){
        // Get a random character from the list of possible characters and add it to our password string.
        // passwordString += characters.charAt(Math.floor(Math.random() * characters.length));
        let randomNumber = Math.floor(Math.random() * characters.length)
        // Add the character at the index of our random number chooses to our password.
        passwordString += characters.substring(randomNumber, randomNumber +1);
        // console.log(passwordString);
    }
    // Set the value of our password box to the randomly generated password
    password.value = passwordString;
}

    // generatePassword()

function copyPassword() {
    // Copying the value of the passwordstring to oiut clipboard
    navigator.clipboard.writeText(password.value)
    // Inform the user of the password been copied to the clipboard
    alert("Password copied to clipboard");
}

// Calling the generate password function on click
generateBtn.addEventListener('click', generatePassword)

// Calling the copy password function on click
copyBtn.addEventListener('click', copyPassword)
