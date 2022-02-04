import json

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

from app.command_handler import command_handler

PUBLIC_KEY = None

def lambda_handler(event, context):
    
    print(event)
    
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    
    signature = event['headers']["x-signature-ed25519"] 
    timestamp = event['headers']["x-signature-timestamp"] 
    body = event['body']

    try: 
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        body = json.loads(event['body'])
        if body["type"] == 1:
            to_return = {
             'statusCode': 200, 
             'body': json.dumps({'type': 1})
            }
        else:
             to_return = command_handler(event)
    except (BadSignatureError) as e:
        print(str(e))
        to_return = {
             'statusCode': 401, 
             'body': json.dumps("Bad Signature")
         }
    print(to_return)
    return to_return
