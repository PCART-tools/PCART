import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], no_args_is_help=False)
