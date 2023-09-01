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
```cp service.WD.cred-template service.WA.cred```
- Open the created file by running:
```vim service.WD.cred```

<img src="./images/WD1.png" width="50%" alt="setup" />

### 1.2 Fill "apikey" rows
- Go to [IBM Cloud](https://cloud.ibm.com/login)
- Login with your IBMid.

<img src="./images/WD2.png" width="80%" alt="setup" />

- Change workspace to DEMO shared folder. In my case "2546406".

<img src="./images/WD3.png" width="80%" alt="setup" />

- Go to "Resources"
- Click on "AI / Machine Learning"
- Click on "Watson Discovery" service.

<img src="./images/WD4.png" width="80%" alt="setup" />

- 

## 2. Preparing service.WX.cred file

## 3. Preparing settings.env file

