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
        self.json_str = json_string.replace("'",'"')
        self.front_quotation = self.json_str.count("{")
        self.end_quotation = self.json_str.count("}")
        self.front_list = self.json_str.count("[")
        self.end_list = self.json_str.count("]")
        self.sin_quot = self.json_str.count("'")
        self.doub_quot = self.json_str.count('"')
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            self.error_msg = e.msg 
            self.error_position = e.pos
        
        # fix missing end quotation
        if self.front_quotation > self.end_quotation :
            self.json_str = self.json_str[:self.error_position] + "}" + self.json_str[self.error_position:]
        
        # fix missing end list 
        elif self.front_list > self.end_list :
            self.json_str = self.json_str[:self.error_position] + "]" + self.json_str[self.error_position:]
        
        # fix missing comma at the end of value
        elif "Expecting ',' delimiter" in self.error_msg : 
            self.json_str = self.json_str[:self.error_position] + "," + self.json_str[self.error_position:]

        elif "Expecting value" in self.error_msg:
            # let none to null
            self.json_str = re.sub(r'\bnone\b', 'null', self.json_str, flags=re.IGNORECASE)

            # fix booleans
            pattern = re.compile(r'\b(True|False)\b', re.IGNORECASE)

            def to_lowercase(match):
                return match.group(0).lower()

            self.json_str = pattern.sub(to_lowercase, self.json_str)

            # fix missing quotes at the value
            value = ''
            pattern2 = r': (\w+)(,|\})'
            matches = re.finditer(pattern2, self.json_str)
            for match in matches:
                value = match.group(1)
            
            # fix missing quotes at the key
            accept_value = ['null','none','NULL','None','Null',"NONE"]
            if not value.isdecimal() and not value.startswith('"') and not value.endswith('"') and value not in accept_value and value!='':
                self.json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', self.json_str)

        elif "Expecting property name enclosed in double quotes" in self.error_msg :
            # fix missing
            copy_json_str = self.json_str
            end_quotation_index = self.json_str.rfind("}")

            # fix missing double quotes
            if end_quotation_index != -1:
                index = end_quotation_index - 1
                while index >= 0 and self.json_str[index] in [" ", "\n", "\t"]:
                    index -= 1

                if index >= 0 and self.json_str[index] == ",":
                    self.json_str = self.json_str[:index] + self.json_str[index+1:] 
                        
            self.json_str = self.format_attributes_with_quotes(self.json_str)
            
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
                self.json_str = re.sub(r'(\w+):', r'"\1":', copy_json_str)
                accept_value = ['null','none','NULL','None','Null',"NONE"]
                if not value2.isdecimal() and not value2.startswith('"') and not value2.endswith('"') and value2 not in accept_value and value2!='':
                    self.json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', self.json_str)

        elif "Unterminated string starting at" in self.error_msg :
            # fix missing end quote with last value
            quote_positions = [m.start() for m in re.finditer(r'"', self.json_str)]
            
            if len(quote_positions) % 2 != 0:
                last_quote_pos = quote_positions[-1]

                next_comma_or_brace = re.search(r'[,\}\]]', self.json_str[last_quote_pos:])
                if next_comma_or_brace:
                    insert_pos = last_quote_pos + next_comma_or_brace.start()
                    self.json_str = self.json_str[:insert_pos] + '"' + self.json_str[insert_pos:]
        try : 
            return json.loads(self.json_str)
        except :
            return self.repair(self.json_str,recursion_count + 1)

def repair_json(input_string: str) -> dict:
    json_parser_instance = json_parser()
    result_json: dict | None = json_parser_instance.repair(input_string)
    if result_json is None:
        raise ValueError("Invalid JSON string")
    return result_json