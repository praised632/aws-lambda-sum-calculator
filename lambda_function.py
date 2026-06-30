import json

def lambda_handler(event, context):
    
    num1 = event.get("num1")
    num2 = event.get("num2")

    # Validate input
    if num1 is None or num2 is None:
        return {
            "statusCode": 400,
            "body": json.dumps("Please provide num1 and num2.")
        }

    result = num1 + num2

    return {
        "statusCode": 200,
        "body": json.dumps({
            "Number 1": num1,
            "Number 2": num2,
            "Sum": result
        })
    }