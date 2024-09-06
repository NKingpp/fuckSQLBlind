import re

# 模拟返回查询结果的函数，根据SQL查询的结果返回True或False
def query_result(sql):
    # 这里你需要根据实际查询情况修改返回逻辑，True表示条件满足，False则不满足
    return True if ">" in sql else False

# 处理SQL语句，提取字符的索引位置和比较的ASCII值
def extract_ascii(sql):
    # 提取字符位置和比较值，字符位置在 MID 函数的第三个参数
    # 比较的ASCII值在 ORD 函数之后的 `>` 符号后面
    mid_match = re.search(r"MID\(.*?,(\d+),1\)", sql)
    ord_match = re.search(r"ORD.*?>\s*(\d+)", sql)

    if mid_match and ord_match:
        char_position = int(mid_match.group(1))  # 提取字符位置
        ascii_value = int(ord_match.group(1))    # 提取ASCII比较值
        return char_position, ascii_value
    return None, None

# 用于存储每个位置的ASCII值
ascii_dict = {}

# 读取1.txt中的SQL查询语句
with open('su.txt', 'r', encoding='utf-8') as file:
    sql_queries = file.readlines()

# 处理每个查询
for sql in sql_queries:
    position, compare_value = extract_ascii(sql.strip())  # 去掉每行的空白字符
    if position and compare_value:
        # 调用查询函数，判断结果
        if query_result(sql.strip()):
            if position not in ascii_dict:
                ascii_dict[position] = compare_value + 1  # 如果条件满足，说明ASCII值比比较值大1
            else:
                ascii_dict[position] = max(ascii_dict[position], compare_value + 1)

# 输出盲注计算出的ASCII值
print("盲注计算出的ASCII值:", ascii_dict)

# 还原出盲注结果的字符串
result = ''.join([chr(ascii_dict[pos]) for pos in sorted(ascii_dict.keys())])
print("盲注得出的字符串:", result)
