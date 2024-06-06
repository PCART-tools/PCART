import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_annotation(None, None, None, 1, None, None, None, 20, None, (- 30), None, None, None, None, None, None, None, None, None, None, None, None, None, True, standoff=None, startarrowhead=None, startarrowsize=None, startstandoff=None, templateitemname=None, text='Annotation 1', textangle=None, valign=None, visible=None, width=None, x=2, xanchor=None, xclick=None, xref=None, exclude_empty_subplots=None)
