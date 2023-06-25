import jwt
import datetime

def is_token_expired(token, secret_key):
    try:
        decoded_token = jwt.decode(token, secret_key,  algorithms=["HS256"])
        exp_timestamp = decoded_token.get('extimestamp')
        current_timestamp = datetime.datetime.utcnow().timestamp()
        return current_timestamp >= exp_timestamp
    except jwt.InvalidTokenError:
        # Handle invalid token
        return True

def decode_token(token, secret_key):
    is_expired = is_token_expired(token,secret_key)

    if is_expired == True:
        print("token expired")
        return None
    else:
        try:
            payload = jwt.decode(token, secret_key)
            return payload
        except jwt.InvalidTokenError:
        # Handle invalid token
            return None