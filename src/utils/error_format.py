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