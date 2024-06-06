import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_annotation(None, None, None, 1, None, None, None, 20, None, (- 30), None, None, None, None, None, None, None, None, None, None, None, None, None, True, None, None, startarrowsize=None, startstandoff=None, templateitemname=None, text='Annotation 1', textangle=None, valign=None, visible=None, width=None, x=2, xanchor=None, xclick=None, xref=None, xshift=None, y=11, yanchor=None, yclick=None, yref=None, yshift=None, row=None, col=None, secondary_y=None, exclude_empty_subplots=None)
