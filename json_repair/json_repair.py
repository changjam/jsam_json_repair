import json
import re



class json_parser:
    def __init__(self):
        pass

    @staticmethod
    def add_quotes(match):
        return f'"{match.group(0)}"'
    
    @staticmethod
    def find_attributes_before_colon(input_string):
        pattern = r'\S+(?=\s*:)'
        matches = re.findall(pattern, input_string)
        return matches
    
    def format_attributes_with_quotes(self, input_string):
        matches = self.find_attributes_before_colon(input_string)
    
        filtered_matches = []
        for match in matches:
            if not (match.startswith('"') and match.endswith('"')):
                filtered_matches.append(match)
        
        if filtered_matches:
            formatted_string = input_string
            for match in filtered_matches:
                if not formatted_string.startswith(f'"{match}"') and not formatted_string.startswith(f"'{match}'"):
                    formatted_string = formatted_string.replace(match, f'"{match}"', 1)
            return formatted_string
        else:
            return input_string
    
    def repair(self, json_string: str , recursion_count=0) -> dict | None:
        if recursion_count >= 2:
            return None
        json_str = json_string.replace("'",'"')
        front_quotation = json_str.count("{")
        end_quotation = json_str.count("}")
        front_list = json_str.count("[")
        end_list = json_str.count("]")
        sin_quot = json_str.count("'")
        doub_quot = json_str.count('"')

        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            error_msg = e.msg 
            error_position = e.pos
        
        # fix missing end quotation, (error msg: Expecting ',' delimiter)
        if front_quotation > end_quotation :
            json_str = json_str[:error_position] + "}" + json_str[error_position:]
        
        # fix missing end list 
        elif front_list > end_list :
            json_str = json_str[:error_position] + "]" + json_str[error_position:]
        
        # fix missing comma at the end of value
        elif "Expecting ',' delimiter" in error_msg : 
            json_str = json_str[:error_position] + "," + json_str[error_position:]

        elif "Expecting value" in error_msg:
            # let none to null
            json_str = re.sub(r'\bnone\b', 'null', json_str, flags=re.IGNORECASE)

            # fix booleans
            pattern = re.compile(r'\b(True|False)\b', re.IGNORECASE)

            def to_lowercase(match):
                return match.group(0).lower()

            json_str = pattern.sub(to_lowercase, json_str)

            # fix missing quotes at the value
            value = ''
            pattern2 = r': (\w+)(,|\})'
            matches = re.finditer(pattern2, json_str)
            for match in matches:
                value = match.group(1)
            
            # fix missing quotes at the key
            accept_value = ['null','none','NULL','None','Null',"NONE"]
            if not value.isdecimal() and not value.startswith('"') and not value.endswith('"') and value not in accept_value and value!='':
                json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', json_str)

        elif "Expecting property name enclosed in double quotes" in error_msg :
            # fix missing
            copy_json_str = json_str
            end_quotation_index = json_str.rfind("}")

            # fix missing double quotes
            if end_quotation_index != -1:
                index = end_quotation_index - 1
                while index >= 0 and json_str[index] in [" ", "\n", "\t"]:
                    index -= 1

                if index >= 0 and json_str[index] == ",":
                    json_str = json_str[:index] + json_str[index+1:] 
                        
            json_str = self.format_attributes_with_quotes(json_str)
            
            # fix missing quotes between colon
            value = ''
            value2 = ''
            pattern = r'(\w+):'
            matches = re.finditer(pattern, copy_json_str)
            for match in matches:
                value = match.group(1)
            
            pattern2 = r': (\w+)(,|\})'
            matches = re.finditer(pattern2, copy_json_str)
            for match in matches:
                value2 = match.group(1)

            if not value.startswith('"') and not value.endswith('"') and value!='':
                json_str = re.sub(r'(\w+):', r'"\1":', copy_json_str)
                accept_value = ['null','none','NULL','None','Null',"NONE"]
                if not value2.isdecimal() and not value2.startswith('"') and not value2.endswith('"') and value2 not in accept_value and value2!='':
                    json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', json_str)

        elif "Unterminated string starting at" in error_msg :
            # fix missing end quote with last value
            quote_positions = [m.start() for m in re.finditer(r'"', json_str)]
            
            if len(quote_positions) % 2 != 0:
                last_quote_pos = quote_positions[-1]

                next_comma_or_brace = re.search(r'[,\}\]]', json_str[last_quote_pos:])
                if next_comma_or_brace:
                    insert_pos = last_quote_pos + next_comma_or_brace.start()
                    json_str = json_str[:insert_pos] + '"' + json_str[insert_pos:]


        return self.repair(json_str, recursion_count + 1)


def repair_json(input_string: str) -> dict:
    json_parser_instance = json_parser()
    result_json: dict | None = json_parser_instance.repair(input_string)
    if result_json is None:
        raise ValueError("Invalid JSON string")
    return result_json