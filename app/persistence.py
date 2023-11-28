from flask import current_app as app

def print_app():
    print(f"app: {app}, app ID: {id(app)}, app Type: {type(app)}")
    print(f"app Config['demo_object']: {app.config.get('demo_object', 'Empty')}")

