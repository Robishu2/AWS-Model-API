#!/bin/bash

echo "Building locally..."
zip deployment_package.zip lambda_function.py

echo "Deploying to Lambda..."
aws lambda update-function-code \
  --function-name InitialFunction \
  --zip-file fileb://deployment_package.zip \
  --region us-east-1

echo "Waiting for deployment..."
sleep 5

echo "Testing Lambda..."
aws lambda invoke --function-name InitialFunction --region us-east-1 response.json
cat response.json
echo ""
echo "✅ Deployment complete!"
