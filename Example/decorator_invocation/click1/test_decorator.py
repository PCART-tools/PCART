import click

@click.command()  # Converts a function to a command line command
@click.option('--name', default='World', help='The person to greet.')  # Optional parameter
def hello(name):
    print(1)
    click.echo(f"Hello, {name}!")  # Print to terminal

if __name__ == '__main__':
    # Debug mode
    hello.main(standalone_mode=False)
    #hello()  
