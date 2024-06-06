import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, None, None, None, None, resilient_parsing=False, allow_extra_args=None, allow_interspersed_args=None, ignore_unknown_options=None, show_default=None)
