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
ERROR_FORMAT3_1 = """
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
CORRECT_FORMAT3_1 = [
    {
        'id': 1, 
        'name': 'Alice', 
        'age': 30, 
        'email': 'alice@example.com', 
        'tags': ['developer', 'javascript', 'vuejs']
    }
]
ERROR_FORMAT3_2 = '{"name": "John", "age": 30, "city": "New York}'
CORRECT_FORMAT3_2 = {'name': 'John', 'age': 30, 'city': 'New York'}

ERROR_FORMAT3_3 = '{"fail": fail}'
CORRECT_FORMAT3_3 = {"fail": "fail"}

ERROR_FORMAT3_4 = '{fail: fail}'
CORRECT_FORMAT3_4 = {"fail": "fail"}

ERROR_FORMAT3_5 = '{"fail": "fail, "test": "test"}'
CORRECT_FORMAT3_5 = {"fail": "fail", "test": "test"}

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


# use error apostrophe
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


# use None value, which should be null
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


