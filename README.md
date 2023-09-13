### FastApi on Lambda

This repo shows how to get a FastApi app running on AWS Lambda.

We use Mangum so that Lambda can find the handler can call the correct endpoints.

To get Lambda to have access to the external dependencies, we need to create a zip to include all the files
Run these commands from the project directory in terminal:
* pip3 install -t lib -r requirements.txt
* (cd lib; zip ../lambda_artifact.zip -r .)

* zip lambda_artifact.zip -u main.py
* zip lambda_artifact.zip -u emailAutoGen.py
* zip lambda_artifact.zip -u prompt.txt
* zip lambda_artifact.zip -u .env