# Google Cloud Functions Course

## Main Consoles
You can start a project in two ways. 

[Firebase](https://console.firebase.google.com) 
or
[Google Cloud Platform](https://console.cloud.google.com)

### This is the repo for the [course here](https://github.com/DavidArmendariz/google-cloud-functions-course)

## Run local
    - functions-framework --target hello_world --debug --port 3000
    
## Deploy a function GCP
    - gcloud auth login
    - gcloud config set project [YOUR_PROJECT_ID]
    - gcloud functions deploy hello_world --runtime python37 --trigger-http
    - [HelloWorld link](https://us-central1-cloud-functionss-course.cloudfunctions.net/hello_world)