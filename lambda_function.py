import json

def lambda_handler(event, context):
    body = json.loads(event['body'])

    first_num = body['first_num']
    second_num = body['second_num']
    operator = body['operator']

    if operator == '+':
        c = first_num + second_num
    elif operator == '-':
        c = first_num - second_num
    elif operator == '*':
        c = first_num * second_num
    else:
        c = first_num / second_num

    print(f'{first_num} {operator} {second_num} = {c}')

    # TODO implement
    return {
        'statusCode': 200,
        'headers': {"Content-type": "application/json"},
        'body': json.dumps(c)
    }
