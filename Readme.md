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

## Live Demo
Check out the live web app here: [Live App](https://wps5a2uf5ia35yfxvukiji7lz40ekuul.lambda-url.us-east-1.on.aws/)


