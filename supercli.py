import click


@click.command()
@click.option('--name', '-n', help='Name of person', required=True)
def supercli(name):
    print(f'Hello {name}!')
