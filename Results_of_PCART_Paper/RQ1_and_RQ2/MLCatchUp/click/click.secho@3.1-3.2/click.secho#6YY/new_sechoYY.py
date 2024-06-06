import click
text = 'Hello, Click!'
file = None
nl = True
styles = {'fg': 'green', 'bg': 'blue', 'bold': True, 'dim': False, 'underline': True, 'blink': False, 'reverse': True, 'reset': True}
click.secho(text, file, nl, err=False)
