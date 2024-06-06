import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], None, None, None, options_metavar='[OPTIONS]', no_args_is_help=False)
