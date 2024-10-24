import re
import sys

def extract_and_format_config_options(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式匹配所有以 CONFIG_ 开头的配置选项，包括注释中的选项
    config_options = re.findall(r'#?\s*(CONFIG_[A-Z0-9_]+)', content)

    # 将每个配置选项用双引号包裹，并在每行末尾添加逗号，最后一行除外
    formatted_options = [f'"{option}",' for option in config_options]
    if formatted_options:
        formatted_options[-1] = formatted_options[-1].rstrip(',')

    # 将处理后的配置选项写入输出文件
    with open(output_file_path, 'w') as file:
        for option in formatted_options:
            file.write(option + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python config_defines.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    extract_and_format_config_options(input_file_path, output_file_path)
