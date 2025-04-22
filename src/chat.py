from colorama import Fore, Style, init
from bot import Bot
import argparse

def get_persona_prompt_and_name(config: dict, persona_key: str) -> tuple[str, str]:
    if persona_key == "none":
        return "", "Bot"

    persona_data = config["personas"].get(persona_key, {})
    parts = []
    name = None

    try:
        for key, value in persona_data.items():
            if key == "name":
                name = value
                parts.append(f"Your name is {name}.")
            elif key == "description":
                parts.append(value)
            elif key == "format":
                parts.append(f"Formatting instructions: {value}")
            else:
                parts.append(f"{key.capitalize()}: {value}")
    except AttributeError as e:
        raise ValueError("Wrong attribute given in config.yml")
    full_prompt = " ".join(parts).strip()
    return full_prompt, name or "Bot"

def display_welcome_message(name: str, model: str, persona: str):
    print(Fore.CYAN + Style.BRIGHT + f"\n{name} is ready!")
    print(Fore.YELLOW + f"Model: {model}")
    print(Fore.MAGENTA + f"Persona: {persona}\n")
    print(Fore.BLUE + "Type your messages below. Use " + Fore.GREEN + "'/bye'" + Fore.BLUE + " to end the chat.\n")

def run_chat_loop(bot: Bot, name: str):
    while True:
        try:
            message = input(Fore.GREEN + "You: " + Style.RESET_ALL)
            if message.strip().lower() == "/bye":
                print(Fore.CYAN + "Goodbye!")
                break
            print(Fore.BLUE + f"\n{name}: ", end='')
            for chunk in bot.ask(message):
                print(Fore.RESET + chunk, end='')
            print("\n")
        except KeyboardInterrupt:
            print(Fore.RED + "\nChat interrupted. Goodbye!")
            break

def chat(args: argparse.Namespace, config: dict):
    init(autoreset=True)

    prompt, name = get_persona_prompt_and_name(config, args.persona)
    bot = Bot(prompt, args.model, config["max_token"])

    display_welcome_message(name, args.model, args.persona)
    run_chat_loop(bot, name)
