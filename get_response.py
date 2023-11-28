from rich.console import Console

if __name__ == '__main__':
    with open('./codes.txt', 'r', encoding='utf-8') as infile:
        codes = {
            line.split(',')[1]: line.split(',')[2]
            for line in infile.readlines()
        }

    c = Console()
    challenge = c.input('[yellow]Enter challenge: [/yellow]')
    response = codes.get(challenge)
    if response:
        c.print(f'[green]Response:        [b]{response}[/b][/green]')
    else:
        c.print('[red]Unknown challenge![/red]')
