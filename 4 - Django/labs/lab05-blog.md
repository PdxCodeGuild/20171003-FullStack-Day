
# Lab 5: Blog

Let's create a blog with posts, comments, and a user system. The instructions below should be taken as guidelines. If you feel confident in structuring your application differently, you're welcome to do so. For testing purposes, you can use incognito/private windows to have separate user sessions, or use different browsers.

## Accounts

For the user system, there should be two groups: posters and commenters. Using the admin panel, create these two groups and give them the appropriate permissions. Have a public registration page to allow **commenters** to make accounts. Use the admin panel to create a **poster**, which should be different from the superuser.

#### Pages

Both pages should redirect to the list of blog posts after registering/logging-in.

- register: allow a commenter to make an account
- login: allow commenters and posters to log into their accounts


## Blog

#### Models

- BlogPost
    - user: a many-to-one relationship to the User table
    - title: text of the post's title
    - body: text of the post's body
    - timestamp: when the post was made


- Comment
    - user: a many-to-one relationship to the User table
    - body: text of the comment's body
    - timestamp: when the comment was made

#### Pages

These pages should be protected, meaning the views which serve them should check the permissions of the user attempting to access them.

- Post List: Show only the post title, username, and the timestamp.
- Post Detail: Show the post title, username, and timestamp, as well as the body and the comments. Each comment should show the user, the timestamp, and the comment body. The comment section should also have a text area for users to enter new comments.
- Make Post: Allow **posters** to create new posts.