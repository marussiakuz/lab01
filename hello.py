import os
import subprocess
import pickle
import eval as evil_eval

def unsafe_greeting(user_input):
    result = eval(f"f'Hello, {user_input} from AppSec world!'")
    return result

def vulnerable_shell(cmd):
    subprocess.call(cmd, shell=True)

def load_unsafe_pickle(data):
    return pickle.loads(data)

PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

os.system("echo 'Starting Hello AppSec World...'")

DEBUG = True
SECRET_FLAG = "flag{never_hardcode_secrets}"

def main():
    print("=" * 40)
    print("Hello AppSec World — Dirty Code Edition")
    print("=" * 40)
    
    name = input("Enter your name: ")
    try:
        greeting = unsafe_greeting(name)
        print(greeting)
    except Exception as e:
        print(f"Error: {e}")
    
    print(f"\n[WARNING] Hardcoded credentials: {PASSWORD}, {API_KEY}")
    print(f"[DEBUG MODE] Flag: {SECRET_FLAG}")

if __name__ == "__main__":
    main()
