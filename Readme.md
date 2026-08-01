# EmailSwift AI 

A lightweight, fully serverless application built for the AWS Builder Center "Weekend Annoying Task Challenge." 

## What it does
EmailSwift AI acts as your personal communications assistant. Paste an incoming email into the interface, and it automatically drafts a highly professional, context-aware reply in seconds. No more overthinking emails!

## Architecture
This app runs entirely in the AWS Free Tier using:
* **AWS Lambda:** Powers the compute and serves the HTML/JS frontend via a public Lambda Function URL.
* **Amazon Bedrock (Nova Lite):** The generative AI model (`amazon.nova-lite-v1:0`) that reads the email and drafts the perfect professional response.

## Live Demo
Check out the live web app here: [Live App](https://wps5a2uf5ia35yfxvukiji7lz40ekuul.lambda-url.us-east-1.on.aws/)
