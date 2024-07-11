import json

class json_parser:
    def __init__(self):
        pass

    def repair(self, json_string: str) -> dict | None:
        try:
            return json.loads(json_string)
        except:
            return None


def repair_json(input_string: str) -> dict:
    json_parser_instance = json_parser()
    result_json: dict | None = json_parser_instance.repair(input_string)
    if result_json is None:
        raise ValueError("Invalid JSON string")
    return result_json