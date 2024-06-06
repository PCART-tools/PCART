import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_annotation(arg=None, align=None, arrowcolor=None, arrowhead=1, arrowside=None, arrowsize=None, arrowwidth=None, ax=20, axref=None, ay=(- 30), ayref=None, bgcolor=None, bordercolor=None, borderpad=None, borderwidth=None, captureevents=None, clicktoshow=None, font=None, height=None, hoverlabel=None, hovertext=None, name=None, opacity=None, showarrow=True, standoff=None, startarrowhead=None, startarrowsize=None, startstandoff=None, templateitemname=None, text='Annotation 1', textangle=None, valign=None, visible=None, width=None, x=2, xanchor=None, xclick=None, xref=None, xshift=None, y=11, yanchor=None, yclick=None, yref=None, yshift=None, row=None, col=None, secondary_y=None, exclude_empty_subplots=None)
