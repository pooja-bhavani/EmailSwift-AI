# EmailSwift AI 

<img width="939" height="439" alt="image" src="https://github.com/user-attachments/assets/8b324aca-95f8-4144-9170-50fab9c13059" />

A lightweight, fully serverless application built for the AWS Builder Center "Weekend Annoying Task Challenge." 

*Like many professionals in the fast-paced tech industry, one of the most annoying, tedious parts of my week is managing my overflowing email inbox. Reading an email takes only a few seconds, but overthinking the reply—ensuring it sounds professional, polite, and concise—often takes five to ten minutes per message. Over an entire week, this mundane task consumes hours of valuable time that could be spent actually building and coding.*


## What it does
EmailSwift AI acts as your personal communications assistant. Paste an incoming email into the interface, and it automatically drafts a highly professional, context-aware reply in seconds. No more overthinking emails!

<img width="768" height="530" alt="Screenshot 2026-08-01 at 5 00 39 PM" src="https://github.com/user-attachments/assets/cd7f7e85-2e5c-4645-a690-82cc210f5711" />


## Architecture
This app runs entirely in the AWS Free Tier using:
* **AWS Lambda:** Powers the compute and serves the HTML/JS frontend via a public Lambda Function URL.
* **Amazon Bedrock (Nova Lite):** The generative AI model (`amazon.nova-lite-v1:0`) that reads the email and drafts the perfect professional response.

<img width="1376" height="768" alt="image" src="https://github.com/user-attachments/assets/3639bd77-05db-40fa-a162-ce2bd22930d9" />

## Prerequisites
An AWS Account: You need an active Amazon Web Services account. If you have a new account, you can leverage up to $200 in Free Tier credits that cover the services used in this project
- Amazon Bedrock Access: Access to the amazon.nova-lite-v1:0 model must be enabled in your account
- AWS Lambda: Used for the serverless compute engine and to host the frontend web interface
- AWS IAM (Identity and Access Management): To grant your Lambda function the proper security permissions to talk to the AI model.

## How to Create & Configure the Environment
1. Create the AWS Lambda Function
- Where: In the AWS Console, search for AWS Lambda
- How: Click Create function and choose "Author from scratch". Name it EmailSwiftAI and select Python 3.12 as the runtime.

2. Generate the Public Web URL
- Where: Inside your new Lambda function's Configuration tab
- How: Click Function URL on the left menu and click "Create function URL". Crucially, set the Auth type to NONE. This generates the live, public web address (like the one you deployed: https://wps5a2uf...lambda-url.us-east-1.on.aws) that allows anyone to view your app without needing an AWS login

3. Grant IAM Security Permissions
- Where: Still in the Lambda Configuration tab, click Permissions, then click the execution Role Name to open the IAM console.
- How: You must attach an inline JSON policy that grants the bedrock:InvokeModel permission. Without this step, your Python code using boto3 will be blocked from sending the email text to the Bedrock AI model.

## Amazon Bedrock's **Nova Lite** model
Amazon Nova Lite (amazon.nova-lite-v1:0) is a generative AI model accessed through Amazon Bedrock. In your EmailSwift AI architecture, it acts as the core "AI Engine" that receives raw input text and intelligently transforms it into structured, professional output.
Based on our setup and the success of other builders in the challenge, here is an overview of its key features and why it is the perfect "sweet spot" model for this project:

- Exceptional at Text Extraction and Formatting: Nova Lite excels at taking messy, unstructured context—like chaotic meeting notes or hasty emails—and extracting the core intent to generate polished summaries, formatted action items, and ready-to-send replies

- Highly Cost-Effective (Free Tier Eligible): It is a lightweight model that qualifies for use within the AWS Free Tier (which provides up to $200 in credits for new accounts). This makes it ideal for running fully serverless weekend projects without accruing unexpected costs

- High-Speed Generation: Because it is a "Lite" model, it is incredibly fast. It is capable of reading context and generating professional, context-aware email replies or weekly digests in just a matter of seconds

- Seamless Serverless Integration: It integrates natively with AWS Lambda using the boto3 SDK's Converse API. As we learned during debugging, it returns its generated content in a highly structured list array format, making it easy to extract the exact text blocks you need for your web frontend.


## Live Demo
Check out the live web app here: [Live App](https://wps5a2uf5ia35yfxvukiji7lz40ekuul.lambda-url.us-east-1.on.aws/)

## Blog Link
Check out the Article here: [Article Link](https://builder.aws.com/content/3HJwDmIQ25xw2hn8C5bJXAqv5JV/weekend-annoying-task-challenge-emailswift-ai)
