import click

a = 1

@click.command()
#@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    # Conditional return 
    return click.echo(f"Hello, {name}!") if a==2 else a

if __name__ == '__main__':
    #hello()
    # Debug Mode
    hello.main(standalone_mode=False)

