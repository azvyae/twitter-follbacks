#Twitter Follbacks
Twitter Follbacks is a Python console application that allows you to see which of your Twitter followers are not following you back. You can also exclude certain users from the list (for example, official accounts that are clearly not going to follow you back but you don't want to include them in the list). You can also keep track of the accounts you have unfollowed by saving them in a list, so that they don't appear in the list again.

##Preparation
To prepare your accounts, make sure you have a folder with your username in the accounts folder, and place your `following.json`, `follower.json`, `exclude.json` (optional), and `unfollowed.json` (optional) files there. Sample `exclude.json` and `unfollowed.json` files can be found in the `accounts/sample` folder.

To obtain the `following.json` and `follower.json` files, go to your Twitter settings and click on the "Your Twitter data" tab. Then, click the "Request data" button to request your data. You will receive an email when your data is ready to be downloaded. Download the data in JSON format and save the following.js and follower.js files as `following.js` and `follower.js`, respectively, in the `accounts/<username>` folder. Both of the files will automatically converted into json by the application.

##Run the App
To run the application, use the command `python main.py <username>` or `python3 main.py <username>`, or if no username is specified, you will be prompted to enter it before continuing.

Example command:
```shell
python main.py johnsmith
```
I hope this helps! Let me know if you have any questions.