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
    
    def repair(self, json_string: str) -> dict | None:
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
        if self.front_quotation > self.end_quotation :
            self.json_str = self.json_str[:self.error_position] + "}" + self.json_str[self.error_position:]
            try : 
                return json.loads(self.json_str)
            except :
                return None
        elif self.front_list > self.end_list :
            self.json_str = self.json_str[:self.error_position] + "]" + self.json_str[self.error_position:]
            try : 
                return json.loads(self.json_str)
            except :
                return None
        elif "Expecting ',' delimiter" in self.error_msg : 
            self.json_str = self.json_str[:self.error_position] + "," + self.json_str[self.error_position:]
            try : 
                return json.loads(self.json_str)
            except :
                return None
        elif "Expecting value" in self.error_msg:
            self.json_str = re.sub(r'\bnone\b', 'null', self.json_str, flags=re.IGNORECASE)
            pattern = re.compile(r'\b(True|False)\b', re.IGNORECASE)

            def to_lowercase(match):
                return match.group(0).lower()

            self.json_str = pattern.sub(to_lowercase, self.json_str)


            
            try:
                return json.loads(self.json_str)
            except:
                try : 
                    self.json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', self.json_str)
                    return json.loads(self.json_str)
                except :
                    return None
        elif "Expecting property name enclosed in double quotes" in self.error_msg :
            #end_quotation_index = self.json_str.rfind("}")
            copy_json_str = self.json_str
            end_quotation_index = self.json_str.rfind("}") if self.json_str.rfind("}") != -1 else 0

            if end_quotation_index != 0:
                index = end_quotation_index - 1
                while index >= 0 and self.json_str[index] in [" ", "\n", "\t"]:
                    index -= 1

                if index >= 0 and self.json_str[index] == ",":
                    self.json_str = self.json_str[:index] + self.json_str[index+1:] 
                        
            self.json_str = self.format_attributes_with_quotes(self.json_str)
            try : 
                return json.loads(self.json_str)
            except :
                try : 
                    self.json_str = re.sub(r'(\w+):', r'"\1":', copy_json_str)
                    self.json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', self.json_str)
                    return json.loads(self.json_str)
                except :
                    return None
        elif "Unterminated string starting at" in self.error_msg :
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
                return None

def repair_json(input_string: str) -> dict:
    json_parser_instance = json_parser()
    result_json: dict | None = json_parser_instance.repair(input_string)
    if result_json is None:
        raise ValueError("Invalid JSON string")
    return result_json