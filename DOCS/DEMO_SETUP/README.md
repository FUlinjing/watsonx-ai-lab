# Preparation of credential files for DEMO watsonx

## 1. Befor you begin

Before preparing the credential files, we need to check the current status of the requirements for our demo.
To check if we meet the requirements to run our demo, after cloning the demo repository (techxchange-watsonx), run the ```_veryfy.sh``` script from the main repository folder (./%your folder path%/techxchange-watsonx).

Assuming you have installed the appropriate tools, you should receive the following message:

<img src="./images/byb1.png" width="80%" alt="setup" />

As you can see there are three files missing. The purpose of this document is to show how to prepare these files.

## 1. Preparing service.WD.cred file

### 1.1 Copy service.WD.cred file

- Go to techxchange-watsonx/API folder.
- Create a copy of ```service.WD.cred-template``` by runing:
```cp service.WD.cred-template service.WD.cred```
- Open the created file by running:
```vim service.WD.cred```

<img src="./images/WD1.png" width="50%" alt="setup" />

- Keep the terminal open on this file.

### 1.2 Fill "apikey", "iam_apikey_description", "iam_apikey_name", "iam_role_crn", "iam_serviceid_crn" and "url" rows

- Go to [IBM Cloud](https://cloud.ibm.com/login)
- Login with your IBMid.

<img src="./images/WD2.png" width="80%" alt="setup" />

- Change workspace to DEMO shared folder. In my case "2546406".

<img src="./images/WD3.png" width="80%" alt="setup" />

- Go to "Resources".
- Click on "AI / Machine Learning".
- Click on "Watson Discovery" service.

<img src="./images/WD4.png" width="80%" alt="setup" />

- In Watson Discovery service page go to "Service credentials".
- Click "New Credential +".

<img src="./images/WD5.png" width="80%" alt="setup" />

- Fill out the form with following information:
    Name:  "initials"_WD_"DayMonth"
    Role:  Writer
- Click "Add".

<img src="./images/WD6.png" width="80%" alt="setup" />

- Expand created credential.
- Copy apikey (without " ") - Mark the text --> right-click --> copy
- Go back to the terminal and click ```i``` to enable INSERT mode (now you can type).
- Go to  second " in the "apikey" line (using keyboard arrows).

<img src="./images/WD7.png" width="80%" alt="setup" />

- Paste the "apikey" - right-click --> Paste
- Repeat the copy and paste operation for "iam_apikey_description", "iam_apikey_name", "iam_role_crn", "iam_serviceid_crn" and "url"

<img src="./images/WD8.png" width="40%" alt="setup" />

- Keep the terminal open on this file.

### 1.3 Fill "projectid" row

- In Watson Discovery service page go to "Manage".
- Click "Launch Watson Discovery".

<img src="./images/WD9.png" width="80%" alt="setup" />

- Find "watsonx technical enablement" project and click on it.

<img src="./images/WD10.png" width="80%" alt="setup" />

- Go to the hamburger menu and click "Integrate and deploy".

<img src="./images/WD11.png" width="80%" alt="setup" />

- Go to "API Information" tab. See the Project ID.
- Repeat the copy and paste operation for "projectid" in terminal.
- You should have all rows filled. To save the file: click "esc" (to exit INSERT mode) --> click ":" --> enter ```wq``` --> click "enter"
- Done! Good job!

## 2. Preparing service.WX.cred file

- Go to the terminal. You should be in techxchange-watsonx/API folder.
- Create a copy of ```service.WX.cred-template``` by runing:
```cp service.WX.cred-template service.WX.cred```
- Open the created file by running:
```vim service.WX.cred```

## 3. Preparing settings.env file

