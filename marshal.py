import os
import sys
import time
import marshal as m

logo = """\033[1;35m
███████╗██╗  ██╗    ███╗   ██╗ █████╗ ███████╗██╗     ██╗
██╔══██╗╚██╗██╔╝    ████╗  ██║██╔══██╗██╔════╝██║     ██║
███████╝ ╚███╔╝     ██╔██╗ ██║███████║█████╗  ██║     ██║
██╔══██╗ ██╔██╗     ██║╚██╗██║██╔══██║██╔══╝  ██║██   ██║
██║  ██║██╔╝ ██╗    ██║ ╚████║██║  ██║██║     ██║╚█████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚════╝
\033[1;0m
"""

line =  "\033[1;92m━━━━━━━━━━━━━━━━\033[1;91m ★\033[1;92m ━━━━━━━━━━━━━━━━━━"

def clear():
    """Cross-platform terminal clear (does NOT print logo)."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def obfuscate_with_marshal():
    print('\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('\033[1;32m┃ \033[1;92m[\033[1;91m•\033[1;92m] \033[1;35mOWNER\033[1;32m \t  :  \033[1;35mRX_NAFIJ         \033[1;32m ┃')
    print('\033[1;32m┃ \033[1;92m[\033[1;91m•\033[1;92m] \033[1;35mADMIN\033[1;32m\t  :  \033[1;35mRX_TAHSAN       \033[1;32m  ┃')
    print('\033[1;32m┃ \033[1;92m[\033[1;91m•\033[1;92m] \033[1;35mTOOLS TYPE\033[1;32m  :  \033[1;35mMARSHAL         \033[1;32m  ┃')
    print('\033[1;32m┃ \033[1;92m[\033[1;91m•\033[1;92m] \033[1;35mTELEGRAM\033[1;32m    :  \033[1;35mNAFIJ01      \033[1;32m     ┃')
    print('\033[1;32m┃ \033[1;92m[\033[1;91m•\033[1;92m] \033[1;35mVERSION\033[1;32m     :  \033[1;35m0.1 (FREE)      \033[1;32m  ┃')
    print('\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m')
    print(line)

    src_path = input("\033[1;32mENTER YOUR FILE PATH :\033[1;36m ").strip()
    out_path = input("\033[1;32mENTER OUTPUT FILE :\033[1;36m ").strip()

    if not src_path:
        print("\033[1;31mNo input file provided.")
        return

    if not os.path.isfile(src_path):
        print(f"\033[1;31mFile not found: {src_path}")
        return

    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            source = f.read()
    except Exception as e:
        print("\033[1;31mCould not read source file:", e)
        return

    try:
        # compile source to code object
        code_obj = compile(source, src_path, 'exec')
    except Exception as e:
        print("\033[1;31mCompile error:", e)
        return

    try:
        dumped = m.dumps(code_obj)   # bytes
        # use repr so bytes literal is correctly embedded in output file
        run_code = "import marshal\nexec(marshal.loads({!r}))\n".format(dumped)
    except Exception as e:
        print("\033[1;31mMarshal dump error:", e)
        return

    try:
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(run_code)
    except Exception as e:
        print("\033[1;31mCould not write output file:", e)
        return

    print(line)
    print("\033[1;32mFILE ENCRYPT SUCCESSFULL.....!")
    print("\033[1;32mFILE SAVED IN = \033[1;36m", os.path.abspath(out_path))
    print(line)

if __name__ == "__main__":
    # Clear the terminal first, then print logo and run the program
    clear()
    print(logo)
    obfuscate_with_marshal()