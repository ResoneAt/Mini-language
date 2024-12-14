def log(message, level="INFO"):
    levels = {"INFO": "ℹ️", "WARN": "⚠️", "ERROR": "❌"}
    print(f"{levels.get(level, 'ℹ️')} {message}")

def validate_token(token, expected_type):
    if token["type"] != expected_type:
        raise TypeError(f"Expected token of type {expected_type}, got {token['type']}")
