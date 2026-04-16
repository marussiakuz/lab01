import os
import subprocess
import pickle

def unsafe_greeting(name):
    result = eval(f"f'Hello appsec world from @{name}!'")
    return result

def vulnerable_shell(cmd):
    subprocess.call(cmd, shell=True)

def load_unsafe_pickle(data):
    return pickle.loads(data)

PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

os.system("echo 'Starting Hello AppSec World application...'")

DEBUG = True
SECRET_FLAG = "flag{never_hardcode_secrets}"

def main():
    print("=" * 45)
    print("Hello AppSec World — Dirty Code Edition")
    print("=" * 45)
    
    name = input("Enter your name: ")

    try:
        greeting = unsafe_greeting(name)
        print(f"\n{greeting}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"\nHello appsec world from @{name}!")
    
    print(f"\n[WARNING] Hardcoded credentials found: {PASSWORD}, {API_KEY}")
    print(f"[DEBUG MODE] Secret flag: {SECRET_FLAG}")

if __name__ == "__main__":
    main()
