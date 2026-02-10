# Dev Setup Instructions

## Dev Tools
### Download and install Visual Studio Code
https://code.visualstudio.com/

### Download and install python
https://www.python.org/downloads/

### Setup XCode (For Mac)
Open terminal and run 
```
python3
```
If XCode is not well installed, there will be a prompt for you to continue with XCode installation, follow that.

Once XCode is installed, running `python3`, you will see it brings you into a python prompt where you can type python code and execute.

### Download and install Github Desktop
https://desktop.github.com/download/

### Clone this repository to your Computer
https://github.com/LegendSlayerX-YT/RateMyTeacher.git

In this step, you may need to register a github account. Then
1. Use Github Desktop to Log in your github account.
2. Select: Clone Repository
3. In the repository URL copy and paste the above link.

<img width="540" height="314" alt="Screenshot 2026-02-08 at 11 35 58 AM" src="https://github.com/user-attachments/assets/e7a36c84-d8e9-4a12-b1d4-6deb1c1518b7" />

This essentially helps sync the code in this github repository with a local folder on your computer.


## Database

### Download and Install PostgreSQL
https://www.postgresql.org/download/macosx/

1. Just follow the Interactive installer by EDB.
Follow all default options. For DB login password, let's use `abc123`.
This is just for dev simplicity. For prod deployment, we will definitely use a more sophisicated password.
2. No need to install ApplicationStack stuff.
3. Start PostgreSQL Database Service on your local machine
```
sudo -i -u postgres

/Library/PostgreSQL/18/bin/pg_ctl start -D /Library/PostgreSQL/18/data
```

## React.js
1. Install nvm and node.js
https://nodejs.org/en/download

2. 
In the folder that you want to make the react app:
```
npm create vite@latest my-react-app -- --template react
```

3. 
In the react app folder
```
npm run dev
```

## Dev Dependencies
### Flask Python Libray
We will use Flask library to build our backend library.
```
pip3 install Flask
```


This library provides the interface to call PostgreSQL DB.
```
pip3 install psycopg2-binary
```
