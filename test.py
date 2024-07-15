import re
import json

input_json = '''
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": None,
        "tags": ["developer", "javascript", "vuejs"]
    }
]
'''

output_json = re.sub(r'\bnone\b', 'null', input_json, flags=re.IGNORECASE)

parsed_json = json.loads(output_json)
print(parsed_json)