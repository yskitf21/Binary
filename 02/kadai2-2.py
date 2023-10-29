import subprocess
import re


def get_objdump_output(binary_path):
    # objdumpを使用してアセンブリのダンプを取得
    cmd = ["objdump", "-d", binary_path]
    func_dependencies = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return func_dependencies.stdout


def parse_objdump_output(output):
    lines = output.splitlines()
    address_to_func = {}

    # 開始アドレスをキー、関数名を値とする辞書を作成する
    for line in lines:
        if match := re.match(r"([0-9a-f]+) <(.+)>:", line):
            start_address = match.group(1)
            func_name = match.group(2)
            if func_name.endswith("@plt"):
                func_name = func_name[:-4]
            address_to_func[int(start_address, 16)] = func_name

    # 関数名をキー、call(callq)命令の引数を値とする辞書を作成する
    current_func = ""
    call_args = {}
    for line in lines:
        # 関数の開始を検知する
        if match := re.match(r"([0-9a-f]+) <(.+)>:", line):
            current_func = match.group(2)
            if current_func.endswith("@plt"):
                current_func = current_func[:-4]
            call_args[current_func] = []
        # 関数の開始以外で、アセンブリの行を検出した場合
        elif match := re.match(r" +[0-9a-f]+:", line):
            lst = line.split()
            if "callq" in lst:
                idx = lst.index("callq")
                call_args[current_func].append(lst[idx + 1])
            if "call" in lst:
                idx = lst.index("call")
                call_args[current_func].append(lst[idx + 1])
        # 空行を検出したらその関数は終了したとみなす
        else:
            current_func = ""

    func_dependencies = {}
    # call命令の引数を関数名に変換する
    for func, args in call_args.items():
        if len(args) == 0:
            continue
        # "_"で始まる関数はライブラリ関数と決め打って無視する
        if func.startswith("_"):
            continue
        func_dependencies[func] = set()
        for arg in args:
            # call命令の引数が16進数のアドレスの場合
            if match := re.match(r"([0-9a-f]+)", arg) or re.match(r"0x([0-9a-f]+)", arg):
                address = int(match.group(1), 16)
                # 関数名に変換する
                func_dependencies[func].add(address_to_func[address])
            # call命令の引数が関数名でない場合
            elif not re.match(r"^[a-zA-Z]", arg):
                pass
            # call命令の引数が関数名の場合
            else:
                func_dependencies[func].append(arg)

    return func_dependencies


def main():
    BIN_PATH = "./a.out"
    output = get_objdump_output(BIN_PATH)
    func_dependencies = parse_objdump_output(output)

    for func, dependencies in func_dependencies.items():
        print(f"{func}: {dependencies}")


if __name__ == "__main__":
    main()
