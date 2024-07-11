import re

def find_attributes_before_colon(input_string):
    pattern = r'\S+(?=\s*:)'
    matches = re.findall(pattern, input_string)
    return matches

def format_attributes_with_quotes(input_string):
    matches = find_attributes_before_colon(input_string)
    
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