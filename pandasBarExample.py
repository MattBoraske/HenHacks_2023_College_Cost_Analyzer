import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def create_sliding_bar_chart(data, x_column, y_column, xlabel='', ylabel='', slider_label='', moving_bar_index=0):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data[x_column])), data[y_column])
    slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])  # Position of the slider
    slider = Slider(slider_ax, slider_label, 0, 1, valinit=0, valstep=0.1)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    def update(val):
        for i, bar in enumerate(bars):
            if i == moving_bar_index:
                bar.set_height(data[y_column][i] + val)
            else:
                bar.set_height(data[y_column][i])
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

# Example usage:
data = {'x_column': [1, 2, 3, 4, 5],
        'y_column': [10, 15, 7, 12, 8]}
create_sliding_bar_chart(data, x_column='x_column', y_column='y_column', xlabel='X-axis', ylabel='Y-axis', slider_label='Adjustment', moving_bar_index=0)
