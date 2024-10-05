<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Engagers Extractor</title>
</head>
<body>
    <h1>Extract IDs of Post Engagers</h1>
    <form id="postForm">
        <label for="post_url">Post URL:</label>
        <input type="text" id="post_url" name="post_url" placeholder="Enter the post URL" required>
        <button type="submit">Get Engagers</button>
    </form>

    <h2>Engagers  IDs</h2>
    <ul id="engagersList"></ul>

    <script>
        document.getElementById( postForm ).addEventListener( submit , function(e) {
            e.preventDefault();
            const postUrl = document.getElementById( post_url ).value;

            fetch( /get_engagers , {
                method:  POST ,
                headers: {
                     Content-Type :  application/json ,
                },
                body: JSON.stringify({ post_url: postUrl }),
            })
            .then(response => response.json())
            .then(data => {
                const engagersList = document.getElementById( engagersList );
                engagersList.innerHTML =   ;  // Clear the list first
                
                if (data.error) {
                    engagersList.textContent = data.error;
                } else {
                    data.forEach(id => {
                        const li = document.createElement( li );
                        li.textContent = id;
                        engagersList.appendChild(li);
                    });
                }
            })
            .catch(error => {
                console.error( Error: , error);
            });
        });
    </script>
</body>
</html>
