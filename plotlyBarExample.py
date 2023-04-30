import plotly.graph_objects as go

# Create data for the bar chart
x_data = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
y_data = [10, 15, 7, 12, 8]

# Create figure
fig = go.Figure()

# Add initial bar chart trace
bar_trace = go.Bar(x=x_data, y=y_data)
fig.add_trace(bar_trace)

# Create slider steps
slider_steps = []
for i in range(len(y_data)):
    slider_steps.append({
        'args': [[{'y': [[val if idx != i else val + i/10 for idx, val in enumerate(y_data)]]}], 
                 {'frame': {'duration': 300, 'redraw': False}, 'mode': 'immediate'}],
        'label': f'{i+1}',
        'method': 'animate'
    })

# Create slider
slider = {'active': 0, 'steps': slider_steps}

# Update layout with slider
fig.update_layout(sliders=[slider], height=600, showlegend=False, title_text="Sliding Bar Chart")

# Set animation properties
frames = []
for i in range(len(y_data)):
    frame = go.Frame(data=[go.Bar(x=x_data, y=[val if idx != i else val + i/10 for idx, val in enumerate(y_data)])])
    frames.append(frame)

# Animate the bar chart
fig.frames = frames
fig.update_layout(updatemenus=[{'type': 'buttons', 'buttons': [{'label': 'Play', 'method': 'animate', 'args': [None]}]}])

# Show the figure
fig.show()
