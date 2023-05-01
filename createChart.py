import matplotlib.pyplot as plt
import pandas as pd
import os

def createChart(cost, majorSalary, college, major, residence):
    # Create dataframe from input data 
    df = pd.DataFrame({'Item': [f'4-Year Cost of Attendance \n({residence})', 'Annual Average Salary'], 'Money': [cost*4, majorSalary]})

    # Set the backend to 'agg'
    plt.switch_backend('agg')

    # Make background of chart transparent
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.set_facecolor((0, 0, 0, 0))

    # Plot the bar chart
    ax.bar(df['Item'], df['Money'].astype(int), color='green')

    # Title
    title = ax.set_title(f"Bachelor's Degree in \n{major} at {college}")
    title.set_fontweight('bold')
    title.set_fontstyle('italic')

    # X-Axis Labels
    for label in ax.get_xticklabels():
        label.set_weight('bold')

    # Y-Axis Labels
    ylabel = ax.set_ylabel("USD ($)")
    ylabel.set_fontweight('bold')

    # Save the image of the bar chart
    file_path='static/bar_chart.png'
    if os.path.exists(file_path):
        os.remove(file_path)
    plt.savefig(file_path)
    plt.clf()

    # Salary ROI Table
    salary_ROI = pd.DataFrame({'Salary %': ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50'], 
                       'Amount ($)': [round(.05*majorSalary), round(.10*majorSalary), round(.15*majorSalary), round(.20*majorSalary), round(.25*majorSalary), round(.30*majorSalary), round(.35*majorSalary), round(.40*majorSalary), round(.45*majorSalary), round(.50*majorSalary)],
                       'ROI (Years)': [round((cost*4)/(.05*majorSalary),2), round((cost*4)/(.10*majorSalary),2), round((cost*4)/(.15*majorSalary),2), round((cost*4)/(.20*majorSalary),2),round((cost*4)/(.25*majorSalary),2), round((cost*4)/(.30*majorSalary),2), round((cost*4)/(.35*majorSalary),2), round((cost*4)/(.40*majorSalary),2), round((cost*4)/(.45*majorSalary),2), round((cost*4)/(.50*majorSalary),2)]
                       })

    # Save Salary ROI table to html file
    html = salary_ROI.to_html(classes=["table table-bordered table-striped table-hover", "text-center"], index=False)
    with open('static/table.html', 'w') as f:
        f.write(html)