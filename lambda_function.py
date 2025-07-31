def lambda_handler(event, context):
    p_message = event.get("queryStringParameters", {}).get("p_message", "no message provided")
    message = f"<h1>The saved string is {p_message}</h1>"
    print(message)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": message
    }
