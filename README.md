# Overview

In this project we set up Azure App Services to deploy a falsk app and integrate it with Azure Pipelines in order to implement Continuous Delivery.

## Project Plan

Trello Board -> [https://trello.com/b/aPBwTDFY/building-a-ci-cd-pipeline](https://trello.com/b/aPBwTDFY/building-a-ci-cd-pipeline)

Porject Sheet ->[[Project management - Google Sheets](https://docs.google.com/spreadsheets/d/1NncFmA4vzYH5yNf06xwX3eAY33LBwLrNu3RNU1POZI8/edit#gid=489099311)](https://docs.google.com/spreadsheets/d/1NncFmA4vzYH5yNf06xwX3eAY33LBwLrNu3RNU1POZI8/edit?usp=sharing)

## Instructions


 ## Architectural Diagram

![image](https://user-images.githubusercontent.com/95375151/205433504-26092f88-30b1-42fa-8bec-e829f3ece8fa.png)


![image](https://user-images.githubusercontent.com/95375151/205130650-19f481e2-f0b2-49aa-bb15-e805d6143c34.png)
                                

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

### Step 1: Launch Cloud Shell:

Go to the Azure Console and launch a bash shell.

![image](https://user-images.githubusercontent.com/95375151/205315252-6ca944a6-3507-404a-9722-68f2d4837b82.png)

### Step 2: Set Up Your GitHub Repo 
Make a new repository for the project with the files in the Project  [ ahshaaban/CI-CD-project](https://github.com/ahshaaban/CI-CD-project)

![image](https://user-images.githubusercontent.com/95375151/205316206-260e951c-d4c4-43e7-acd3-03c599514c58.png)

### Step 3: Clone the Repo and Create virtual Environment:

  1. Setup virtual environement

![image](https://user-images.githubusercontent.com/95375151/205317504-101e4fee-0686-4eda-80be-21435b3e4d61.png)

   2. run ```make install```

   3. Create an app service and initially deploy your app in Cloud Shell:
    ```az webapp up -n <your-appservice>```

   4. Verify the deployed application works by browsing to the deployed url
      ![image](https://user-images.githubusercontent.com/95375151/205319243-cce34bc1-3b7a-4da8-a531-7a088f8e14ff.png)
      
### Step 4: Perform Prediction

Change the line in make_predict_azure_app.sh to match the deployed prediction:

-X POST https://<yourappname>.azurewebsites.net:$PORT/predict

![image](https://user-images.githubusercontent.com/95375151/205319601-faf8cc6e-0093-4901-a91d-b796ac0f42eb.png)
  
  ### Step 5: Create an Azure DevOps project
    1. Create new project and name it
     ![image](https://user-images.githubusercontent.com/95375151/205320259-e4902b5e-24fd-4c20-8d2a-c1f95223cd27.png)
  
    2. Set up a new service connection via Azure Resource Manager and Pipeline
      ![image](https://user-images.githubusercontent.com/95375151/205320453-f15c3012-6dcd-428a-ac9d-2ed2bc868614.png)
      ![image](https://user-images.githubusercontent.com/95375151/205320620-c1d4d152-bf71-4127-b67f-d9e87f279fae.png)


   3.  create a Pipeline
  ![image](https://user-images.githubusercontent.com/95375151/205320874-0a131af3-bd1e-4401-806d-46661fc99752.png)

   4. Integrate with GitHub:
   ![image](https://user-images.githubusercontent.com/95375151/205321116-6de14c25-6b88-4ac6-9cd0-0282e481785f.png)

   5. Configure Python to Linux Web App on Azure and choose your webapp name:
  
  ![image](https://user-images.githubusercontent.com/95375151/205321300-8abfcfa6-3392-49cb-96b7-0370f7a66143.png)



### Step 6 Output of a test run

![image](https://user-images.githubusercontent.com/95375151/205322409-57c25531-764f-4877-8d95-3ab0a71b1a7a.png)





