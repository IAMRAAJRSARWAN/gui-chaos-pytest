from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv('ENV_PLATFORM')

def get_platform_class():
    if environment == 'MAC':
        return MacPlatform()
    elif environment == 'WIN':
        return WindowsPlatform()
    else:
        raise ValueError(f"Unknown environment: {environment}")


class MacPlatform:
    def run_test(self):
        print("Running tests on MAC")

class WindowsPlatform:
    def run_test(self):
        print("Running tests on Windows")