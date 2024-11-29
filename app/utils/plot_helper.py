import matplotlib.pyplot as plt

def plot_data(data, x_column, y_column, plot_type="line", title=None, xlabel=None, ylabel=None):
    """
    Generates a plot of the data with customizable options.
    Args:
        data (pd.DataFrame): The data to plot.
        x_column (str): Column name for the x-axis.
        y_column (str): Column name for the y-axis.
        plot_type (str): Type of plot to generate ('line', 'scatter', 'bar').
        title (str, optional): Title of the plot. Defaults to None.
        xlabel (str, optional): Label for the x-axis. Defaults to None.
        ylabel (str, optional): Label for the y-axis. Defaults to None.
    Returns:
        matplotlib.figure.Figure: The generated plot figure.
    """
    try:
        # Validate input columns
        if x_column not in data.columns or y_column not in data.columns:
            raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the data.")
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == "line":
            ax.plot(data[x_column], data[y_column], marker='o', linestyle='-')
        elif plot_type == "scatter":
            ax.scatter(data[x_column], data[y_column])
        elif plot_type == "bar":
            ax.bar(data[x_column], data[y_column])
        else:
            raise ValueError(f"Unsupported plot type: '{plot_type}'. Use 'line', 'scatter', or 'bar'.")
        
        # Customize labels and title
        ax.set_xlabel(xlabel if xlabel else x_column)
        ax.set_ylabel(ylabel if ylabel else y_column)
        ax.set_title(title if title else f"{y_column} vs {x_column}")
        ax.grid(True)

        # Show the plot
        plt.show()
        
        return fig
    except Exception as e:
        print(f"Error plotting data: {e}")
        return None
