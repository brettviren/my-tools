def hello() -> str:
    return "Hello from my-tools!"
def main():
    print("""
    The my-tools umbrella.

    $ uv tool install git+https://github.com/brettviren/my-tools

    $ uv tool upgrade my-tools
    """
