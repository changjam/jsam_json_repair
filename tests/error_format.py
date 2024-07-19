# Lack of comma
ERROR_FORMAT1 = """
[
    {
        "id": 1
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"]
    }
]
"""
CORRECT_FORMAT1 = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"]
    }
]


# Redundant comma at the end
ERROR_FORMAT2 = """
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags" : ["developer", "javascript", "vuejs"],
    }
]
"""
CORRECT_FORMAT2 = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags" : ["developer", "javascript", "vuejs"]
    }
]


# Missing quotation marks
ERROR_FORMAT3 = """
[
    {
        id: 1,
        name: "Alice",
        age: 30,
        email: "alice@example.com",
        tags: ["developer", "javascript", "vuejs"]
    }
]
"""
CORRECT_FORMAT3 = [
    {
        'id': 1, 
        'name': 'Alice', 
        'age': 30, 
        'email': 'alice@example.com', 
        'tags': ['developer', 'javascript', 'vuejs']
    }
]


# Missing parentheses }
ERROR_FORMAT4 = """
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"]
]
"""
CORRECT_FORMAT4 = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"]
    }
]


# Error Boolean value
ERROR_FORMAT5 = """
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"],
        "active": True
    }
]
"""
CORRECT_FORMAT5 = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"],
        "active": True
    }
]


ERROR_FORMAT6 = """
[
    {
        'id': 1,
        'name': 'Alice',
        'age': 30,
        'email': 'alice@example.com',
        'tags': ['developer', 'javascript', 'vuejs']
    }
]
"""

CORRECT_FORMAT6 = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "tags": ["developer", "javascript", "vuejs"]
    }
]

ERROR_FORMAT7 = """
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": None,
        "tags": ["developer", "javascript", "vuejs"]
    }
]
"""

CORRECT_FORMAT7 = [
    {
        'id': 1, 
        'name': 'Alice', 
        'age': 30, 
        'email': None, 
        'tags': ['developer', 'javascript', 'vuejs']
    }
]

ERROR_FORMAT8 = '{"name": "John", "age": 30, "city": "New York}'
CORRECT_FORMAT8 = {'name': 'John', 'age': 30, 'city': 'New York'}

ERROR_FORMAT9 = '{"fail": fail}'
CORRECT_FORMAT9 = {"fail": "fail"}

ERROR_FORMAT10 = '{fail: fail}'
CORRECT_FORMAT10 = {"fail": "fail"}