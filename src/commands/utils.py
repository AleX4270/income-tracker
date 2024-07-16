import click

@click.group()
def cli_utils():
    pass

@click.command()
def hello():
    click.echo("Hi, user!")
    
cli_utils.add_command(hello)