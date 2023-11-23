import os


def is_executable(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(4)
        # Windows実行可能ファイルのシグネチャ
        if header[:2] == b'MZ':
            return "EXE"
        # ELF実行可能ファイルのシグネチャ
        elif header[:4] == b'\x7fELF':
            return "ELF"
        else:
            return False


files = os.listdir()
upx_files = []
not_upx_files = []
not_executable_files = []
for file in files:
    with open(file, 'rb') as f:
        binary = f.read()
    # 実行可能ファイルでない場合はスキップ
    file_type = is_executable(file)
    if not file_type:
        not_executable_files.append(file)
        continue
    hex_str = binary.hex()
    # "UPX!"の位置を探す
    upx_pos = hex_str.find("55505821")
    if upx_pos == -1:  # UPX!が見つからなかった場合
        not_upx_files.append(file)
        continue
    # "UPX!"が見つかり、かつその位置が正しい場合
    if file_type == "EXE" and upx_pos == 1984:
        upx_files.append(file)
        continue
    elif file_type == "ELF" and upx_pos == 472:
        upx_files.append(file)
        continue
    # "UPX!"が見つかったが、その位置が正しくない場合
    not_upx_files.append(file)

print("UPX files:")
for file in upx_files:
    print("    " + file)
print()
print("Not UPX files:")
for file in not_upx_files:
    print("    " + file)
print()
print("Not executable files:")
for file in not_executable_files:
    print("    " + file)
