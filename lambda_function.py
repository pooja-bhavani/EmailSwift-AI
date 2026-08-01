import json
import boto3

# Initialize the Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
MODEL_ID = "amazon.nova-lite-v1:0"

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EmailSwift AI</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; color: #333; }
        h1 { color: #0073bb; }
        textarea { width: 100%; height: 200px; margin-bottom: 15px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { padding: 12px 24px; background-color: #0073bb; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; }
        button:hover { background-color: #005a93; }
        #result { margin-top: 30px; white-space: pre-wrap; background: #f9f9f9; padding: 20px; border-radius: 4px; border: 1px solid #eee; display: none; line-height: 1.6; }
    </style>
</head>
<body>
    <h1>EmailSwift AI</h1>
    <p>Stop overthinking your emails. Paste the message you received below, and Nova Lite will instantly draft a professional, concise reply.</p>

    <textarea id="email" placeholder="Paste the email you received here..."></textarea>
    <br>
    <button id="btn" onclick="generateReply()">Draft My Reply</button>

    <div id="result"></div>

    <script>
        async function generateReply() {
            const email = document.getElementById('email').value;
            const resultDiv = document.getElementById('result');
            const btn = document.getElementById('btn');

            if (!email.trim()) {
                alert("Please paste an email first!");
                return;
            }

            resultDiv.style.display = "block";
            resultDiv.innerText = "Drafting your professional reply with Amazon Bedrock...";
            btn.disabled = true;

            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: email })
                });

                const data = await response.json();

                if (response.ok) {
                    resultDiv.innerText = data.reply;
                } else {
                    resultDiv.innerText = "Error: " + (data.error || "Something went wrong.");
                }
            } catch (e) {
                resultDiv.innerText = "Network Error calling the API.";
            } finally {
                btn.disabled = false;
            }
        }
    </script>
</body>
</html>"""

def lambda_handler(event, context):
    method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')

    if method == 'GET':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': HTML_PAGE
        }

    elif method == 'POST':
        try:
            body = json.loads(event.get('body', '{}'))
            email_text = body.get('email', '').strip()

            if not email_text:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({'error': 'No email provided'})
                }

            prompt = (
                "Please read the following email and draft a professional, "
                "polite, and concise reply.\n\n"
                f"Incoming Email:\n{email_text}"
            )

            response = bedrock.converse(
                modelId=MODEL_ID,
                messages=[{
                    "role": "user",
                    "content": [{"text": prompt}]
                }],
                inferenceConfig={"temperature": 0.3}
            )

            # ✅ FIX: content is a list, must index with [0] first
            reply_draft = response['output']['message']['content'][0]['text']

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'reply': reply_draft})
            }

        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': str(e)})
            }
