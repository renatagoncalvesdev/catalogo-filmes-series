from sys import exit
from cli import PromptInterface


def main():
    prompt_interface = PromptInterface()
    prompt_interface.show_main_menu()


if __name__ == '__main__':
    main()
    exit()
