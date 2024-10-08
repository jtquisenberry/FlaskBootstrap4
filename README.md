# FlaskBootstrap4

# Style

* Top navigation bar, collapses to hamburger menu when width drops to 992 pixels. This works because the nav bar uses class `.navbar-expand-lg`, which follows this rule:

```
@media (min-width: 992px)
.navbar-expand-lg {
    -ms-flex-flow: row nowrap;
    flex-flow: row nowrap;
    -ms-flex-pack: start;
    justify-content: flex-start;
}
```

* Left side bar, expands and collapses using a floating button. 
* A sticky footer, which displays at the bottom of the page unless there is enough page content to push the footer lower.


# Load Page with Data Synchronously

Template `product_sync.html` demonstrates passing data from Python to a page synchronously. It features CRUD operations that work by passing data into Python functions.

# Manipulate Data with REST

Template `product.html` demonstrates manipulating data with REST. It features CRUD operations that work by calling Javascript functions to pass data using REST requests.

# REST with Vanilla Javascript vs. jQuery

REST requests with vanilla Javascript feature in `chat.js`. 

## Javascript

```Javascript
chatForm.addEventListener('submit', (event) => {
    ...
    fetch('/api/chat', {
        method: 'POST',
        ...
```

## jQuery

```jQuery
function addProduct() {
    ...
    $.ajax({
        url: '/api/product',
        type: 'POST',
```

# Passing Application Data Around Flask

It is possible to work with `app` created by `app = Flask(__name__)` without passing the `app` variable to modules other than the one where it was created. 

In module `app.py`, create an app (`flask.app.Flask`) and then create a context. Add a key-value pair to `app`.
```Python
app = Flask(__name__)
...
app.app_context().push()
demo_object = {"a": 1, "b": 2, "c": 3}
app.config['demo_object'] = demo_object
```

In module `persistence.py`, import `current_app` and interact with it.

```Python
from flask import current_app as app
...
print(f"app Config['demo_object']: {app.config.get('demo_object', 'Empty')}")
```








# 
