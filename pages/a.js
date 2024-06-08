const contentCache = {
           flashcard: `
                <!DOCTYPE html>
            <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        textarea,
        select {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px; /* Increase font size */
        }

        button[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 10px;
            }
        }

        .rich-text-input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            min-height: 100px;
            font-family: Arial, sans-serif;
        }

        /* Toast Message */
        .toast {
            visibility: hidden;
            max-width: 200px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 2px;
            padding: 16px;
            position: fixed;
            z-index: 1;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
        }

        /* Loader */
         .loader {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        animation: spin 1s linear infinite;
        position: absolute;
        right: 50%;
        margin-right: -15px; /* Adjust to half of the width */
        top: 50%;
        margin-top: -15px; /* Adjust to half of the height */
        display: none; /* Initially hidden */
        z-index: 1;
    }

    /* Adjust button position */
    button[type="submit"] {
        position: relative;
    }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">

        <form id="postForm">
            <label for="slide1">front:</label>
            <textarea contenteditable="true" id="slide1" name="slide1" class="rich-text-input" placeholder="Start typing here..."></textarea>

            <label for="slide2">back:</label>
            <textarea contenteditable="true" id="slide2" name="slide2" class="rich-text-input" placeholder="Start typing here..."></textarea>

            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="riddle">Riddle</option>
                <option value="fact">Fact</option>
                <option value="news">News</option>
            </select>

            <button type="submit">Submit</button>
        </form>
    </div>

    <!-- Toast Message -->
    <div class="toast" id="toast"></div>

    <!-- Loader -->
    <div class="loader" id="loader"></div>

    <script>
    document.getElementById('postForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Show loader
        document.getElementById('loader').style.display = 'block';

        // Get input values
        var slide1Value = document.getElementById('slide1').value;
        var slide2Value = document.getElementById('slide2').value;
        var categoryValue = document.getElementById('category').value;

        var data = {"lang":"ENGLISH", "cat": categoryValue, "texts": [slide1Value, slide2Value], "template": "flash" };

        // Send POST request
        fetch('https://playchat.live/storiez/post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('API response:', data);

            // Hide loader
            document.getElementById('loader').style.display = 'none';

            // Show toast message
            var toast = document.getElementById('toast');
            toast.innerHTML = 'API call successful!';
            toast.style.visibility = 'visible';

            // Hide toast message after 3 seconds
            setTimeout(function(){
                toast.style.visibility = 'hidden';
            }, 3000);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            // Hide loader in case of error
            document.getElementById('loader').style.display = 'none';
            // Handle errors here
        })
        .finally(() => {
            // After the API call is completed, allow the form submission
            event.target.submit();
        });
    });
</script>


</body>
</html>

            `,
            poll: `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create a Poll</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 600px;
            margin: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: 500;
            margin-bottom: 5px;
            color: #555;
        }

        input[type="text"],
        textarea {
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            background-color: #f2f2f2;
            transition: border 0.3s;
        }

        input[type="text"]:focus,
        textarea:focus {
            border-color: #007bff;
        }

        button[type="button"],
        button[type="submit"] {
            padding: 12px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        button[type="button"]:hover,
        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        .option {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .option input[type="text"] {
            flex: 1;
            margin-right: 10px;
        }

        .option button {
            flex-shrink: 0;
            padding: 8px 12px;
            font-size: 14px;
        }

        .add-option-button {
            margin-bottom: 20px;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 10px;
                padding: 15px;
            }
            input[type="text"],
            textarea {
                font-size: 14px;
            }
            button[type="button"],
            button[type="submit"] {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">

        <form id="pollForm">
            <label for="question">Poll Question:</label>
            <textarea id="question" name="question" rows="3" placeholder="Enter your poll question here..."></textarea>

            <label for="options">Options:</label>
            <div id="options">
                <div class="option">
                    <input type="text" name="option" placeholder="Option 1">
                    <button type="button" onclick="removeOption(this)">Remove</button>
                </div>
                <div class="option">
                    <input type="text" name="option" placeholder="Option 2">
                    <button type="button" onclick="removeOption(this)">Remove</button>
                </div>
            </div>
            <button type="button" class="add-option-button" onclick="addOption()">Add Option</button>

            <button type="submit">Create Poll</button>
        </form>
    </div>

    <script>
        function addOption() {
            const optionsDiv = document.getElementById('options');
            const newOptionDiv = document.createElement('div');
            newOptionDiv.classList.add('option');
            newOptionDiv.innerHTML = \`
                <input type="text" name="option" placeholder="Option \$\{optionsDiv.children.length + 1\}">
                <button type="button" onclick="removeOption(this)">Remove</button>
            \`;
            optionsDiv.appendChild(newOptionDiv);
        }

        function removeOption(button) {
            button.parentElement.remove();
            updatePlaceholders();
        }

        function updatePlaceholders() {
            const options = document.querySelectorAll('#options .option input[type="text"]');
            options.forEach((input, index) => {
                input.placeholder = \`Option \$\{index + 1\}\`;
            });
        }

        document.getElementById('pollForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const question = document.getElementById('question').value;
            const options = Array.from(document.getElementsByName('option')).map(option => option.value).filter(value => value.trim() !== '');

            if (!question || options.length < 2) {
                alert('Please enter a question and at least two options.');
                return;
            }

            const pollData = {
                question: question,
                options: options,
                "template": "poll",
                "cat": "poll",
                "lang": "ENGLISH",
                "loc": "INDIA"
            };

            // Replace the URL below with the actual endpoint for your API
            fetch('https://playchat.live/storiez/post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pollData)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Poll created:', data);
                // Handle the response here, e.g., display a success message or redirect
            })
            .catch(error => {
                console.error('Error creating poll:', error);
                // Handle the error here, e.g., display an error message
            });
        });
    </script>
</body>
</html>


            `,
            slides: `
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post API Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        textarea,
        select {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px; /* Increase font size */
        }

        button[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 10px;
            }
        }

        .rich-text-input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            min-height: 100px;
            font-family: Arial, sans-serif;
        }
        /* Loader */
        .loader {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            position: absolute;
            right: 50%;
            margin-right: -15px; /* Adjust to half of the width */
            top: 50%;
            margin-top: -15px; /* Adjust to half of the height */
            display: none; /* Initially hidden */
            z-index: 1;
        }

        /* Adjust button position */
        button[type="submit"] {
            position: relative;
        }

        /* Toast Message */
        .toast {
            visibility: hidden;
            max-width: 200px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 2px;
            padding: 16px;
            position: fixed;
            z-index: 1;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
    <div class="container">

        <form id="postForm">
            <label for="slide1">Slide 1:</label>
            <input type="text" id="slide1" name="slide1">

            <label for="slide2">Slide 2:</label>
            <textarea contenteditable="true" id="slide2" name="slide2" class="rich-text-input" placeholder="Start typing here..."></textarea>

            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="insight">Insight</option>
                <option value="fact">Fact</option>
                <option value="news">News</option>
            </select>

            <button type="submit">Submit</button>
        </form>
    </div>

    <!-- Loader -->
    <div class="loader" id="loader"></div>

    <!-- Toast Message -->
    <div class="toast" id="toast"></div>

    <script>
        // Function to handle paste event and preserve multiline content
        function handlePaste(event) {
            event.preventDefault();
            var text = (event.originalEvent || event).clipboardData.getData('text/plain');
            document.execCommand('insertText', false, text);
        }

        // Function to pick a random element from the array
        function getRandomElement(arr) {
            const randomIndex = Math.floor(Math.random() * arr.length);
            return arr[randomIndex];
        }

        document.getElementById('postForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Show loader
            document.getElementById('loader').style.display = 'block';

            // Get input values
            var slide1Value = document.getElementById('slide1').value;
            var slide2Value = document.getElementById('slide2').value;
            var categoryValue = document.getElementById('category').value;

            var data = {"lang": "ENGLISH", "loc": "INDIA", "cat": categoryValue, "texts": [slide1Value, slide2Value], "template": "slides" };

            // Send POST request
            fetch('https://playchat.live/storiez/post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('API response:', data);

                // Hide loader
                document.getElementById('loader').style.display = 'none';

                // Show toast message
                var toast = document.getElementById('toast');
                toast.innerHTML = 'API call successful!';
                toast.style.visibility = 'visible';

                // Hide toast message after 3 seconds
                setTimeout(function(){
                    toast.style.visibility = 'hidden';
                }, 3000);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Hide loader in case of error
                document.getElementById('loader').style.display = 'none';
                // Handle errors here
            });
        });

    </script>
</body>
</html>

            `,
            image: `
               <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Image with Heading</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        textarea,
        select {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px; /* Increase font size */
        }

        button[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 10px;
            }
        }

        .rich-text-input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            min-height: 100px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div class="container">

        <form id="postForm">
            <label for="slide1">Heading:</label>
            <input type="text" id="slide1" name="slide1">

            <label for="slide2">Image URL:</label>
            <textarea contenteditable="true" id="slide2" name="slide2" class="rich-text-input" placeholder="Start typing here..."></textarea>

            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="insight">Insight</option>
                <option value="quote">Quote</option>
                <option value="fact">Fact</option>
                <option value="news">News</option>
            </select>

            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        // Function to handle paste event and preserve multiline content
        function handlePaste(event) {
            event.preventDefault();
            var text = (event.originalEvent || event).clipboardData.getData('text/plain');
            document.execCommand('insertText', false, text);
        }

        document.getElementById('postForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Get input values
            var slide1Value = document.getElementById('slide1').value;
            var slide2Value = document.getElementById('slide2').value;
            var categoryValue = document.getElementById('category').value;

            // Create data object
            var data = {"lang":"ENGLISH", "cat": categoryValue,"texts": [slide1Value, slide2Value], "template": "img"};

            // Send POST request
            fetch('https://playchat.live/storiez/post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('API response:', data);

                // Handle API response here
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Handle errors here
            });
        });


    </script>
</body>
</html>

            `,
            imageUpload: `
                          <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Image with Heading</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        textarea,
        select {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px; /* Increase font size */
        }

        input[type="file"] {
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 10px;
            }
        }

        .rich-text-input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            min-height: 100px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Add Image with Heading</h1>
        <form id="postForm">
            <label for="slide1">Heading:</label>
            <input type="text" id="slide1" name="slide1">
            <label for="imageUpload">Upload Image:</label>
            <input type="file" id="imageUpload" name="imageUpload" accept="image/*">

            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="insight">Insight</option>
                <option value="quote">Quote</option>
                <option value="fact">Fact</option>
                <option value="news">News</option>
            </select>

            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        document.getElementById('postForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Get input values
            var slide1Value = document.getElementById('slide1').value;
            var categoryValue = document.getElementById('category').value;

            // Get the uploaded image file
            const file = document.getElementById('imageUpload').files[0];

            // Check if an image is selected
            if (!file) {
                alert("Please select an image");
                return;
            }

            // Create a FormData object and append the image file to it
            const formData = new FormData();
            formData.append('file', file);

            // Upload the image using fetch
            fetch('https://playchat.live/file', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Once the image is uploaded, get the URL and proceed with the API call
                const imgUrl = data.file_path;

                // Create data object for API call
                const apiData = {
                    "lang": "ENGLISH",
                    "cat": categoryValue,
                    "texts": [slide1Value, "https://playchat.live/file/"+imgUrl],
                    "atemplate": "img"
                };

                // Send POST request to the API
                return fetch('https://playchat.live/storiez/post', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(apiData)
                });
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('API response:', data);
                // Handle API response here
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Handle errors here
            });
        });
    </script>
</body>
</html>


            `,
            status:
            `
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post API Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        textarea,
        select {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px; /* Increase font size */
        }

        button[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button[type="submit"]:hover {
            background-color: #0056b3;
        }

        @media screen and (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 10px;
            }
        }

        .rich-text-input {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            min-height: 100px;
            font-family: Arial, sans-serif;
        }
        /* Loader */
        .loader {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            position: absolute;
            right: 50%;
            margin-right: -15px; /* Adjust to half of the width */
            top: 50%;
            margin-top: -15px; /* Adjust to half of the height */
            display: none; /* Initially hidden */
            z-index: 1;
        }

        /* Adjust button position */
        button[type="submit"] {
            position: relative;
        }

        /* Toast Message */
        .toast {
            visibility: hidden;
            max-width: 200px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 2px;
            padding: 16px;
            position: fixed;
            z-index: 1;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
    <div class="container">

        <form id="postForm">
            <label for="slide1">Slide 1:</label>
            <input type="text" id="slide1" name="slide1">


            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="insight">Insight</option>
                <option value="fact">Fact</option>
                <option value="news">News</option>
            </select>

            <button type="submit">Submit</button>
        </form>
    </div>

    <!-- Loader -->
    <div class="loader" id="loader"></div>

    <!-- Toast Message -->
    <div class="toast" id="toast"></div>

    <script>
        // Function to handle paste event and preserve multiline content
        function handlePaste(event) {
            event.preventDefault();
            var text = (event.originalEvent || event).clipboardData.getData('text/plain');
            document.execCommand('insertText', false, text);
        }

        // Function to pick a random element from the array
        function getRandomElement(arr) {
            const randomIndex = Math.floor(Math.random() * arr.length);
            return arr[randomIndex];
        }

        document.getElementById('postForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Show loader
            document.getElementById('loader').style.display = 'block';

            // Get input values
            var slide1Value = document.getElementById('slide1').value;
            var categoryValue = document.getElementById('category').value;

            var data = {"lang": "ENGLISH", "loc": "INDIA", "cat": categoryValue, "texts": [slide1Value, ''], "template": "slides" };

            // Send POST request
            fetch('https://playchat.live/storiez/post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('API response:', data);

                // Hide loader
                document.getElementById('loader').style.display = 'none';

                // Show toast message
                var toast = document.getElementById('toast');
                toast.innerHTML = 'API call successful!';
                toast.style.visibility = 'visible';

                // Hide toast message after 3 seconds
                setTimeout(function(){
                    toast.style.visibility = 'hidden';
                }, 3000);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Hide loader in case of error
                document.getElementById('loader').style.display = 'none';
                // Handle errors here
            });
        });

    </script>
</body>
</html>

            `
        };

