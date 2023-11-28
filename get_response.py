import sys
from rich.console import Console

if __name__ == '__main__':
    with open('./codes.txt', 'r', encoding='utf-8') as infile:
        codes = {
            line.split(',')[1]: line.split(',')[2]
            for line in infile.readlines()
        }

    c = Console()
    challenge = c.input('[yellow]Enter challenge: [/yellow]')
    challenges: list[str] = [challenge]
    if len(challenge) == 9:
        challenges.clear()
        for index in range(0, len(challenge) + 1):
            new_challenge = challenge[0:index] + '0' + challenge[index:]
            challenges.append(new_challenge)
    elif len(challenge) != 10:
        c.print('[red]ERROR, challenge should be 9 or 10 characters long![/]')
        sys.exit(1)

    c.print()
    for challenge in challenges:
        response = codes.get(challenge)
        if response:
            c.print(f'\n  [green]{challenge} --> [b]{response}[/b][/green]')
        else:
            c.print(f'  [red]{challenge} --> [b]Unknown[/b][/red]')
