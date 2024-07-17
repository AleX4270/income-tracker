import click
from logic import utilsLogic

@click.group()
def cmd_utils():
    pass

@click.command()
def hello():
    click.echo(utilsLogic.hello())

@click.command()
def ping():
    click.echo(utilsLogic.ping())
    
cmd_utils.add_command(hello)
cmd_utils.add_command(ping)