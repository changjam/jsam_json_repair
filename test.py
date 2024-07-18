import json
import re

fail_1 = '{"name": "John", "age": 30, "city": "New York}'
fail_2 = '{"fail": fail}'
fail_3 = '{fail: fail}'

def fix_json(json_str):
    # 找到引號不匹配的位置並在適當位置添加引號
    quote_positions = [m.start() for m in re.finditer(r'"', json_str)]
    
    # 如果引號數量是奇數，則嘗試修正
    if len(quote_positions) % 2 != 0:
        last_quote_pos = quote_positions[-1]
        # 在找到的未閉合字符串結尾前添加引號
        next_comma_or_brace = re.search(r'[,\}\]]', json_str[last_quote_pos:])
        if next_comma_or_brace:
            insert_pos = last_quote_pos + next_comma_or_brace.start()
            json_str = json_str[:insert_pos] + '"' + json_str[insert_pos:]

    # 修正鍵沒有引號包裹的情況
    json_str = re.sub(r'(\w+):', r'"\1":', json_str)
    
    # 修正值沒有引號包裹的情況
    json_str = re.sub(r': (\w+)(,|\})', r': "\1"\2', json_str)
    
    return json_str


print(fix_json(fail_2))

try:
    json.loads(fail_3)
except json.JSONDecodeError as e:
    print(e)

