
import matplotlib.pyplot as plt

# Data for the chart
models = ['Model I', 'Model II', 'Projected Model III']
accuracy = [15, 50, 90]


# Updating the chart to make it cleaner and more professional
fig, ax = plt.subplots(figsize=(10, 5))

# Redefine color scheme for a more professional look
bars = ax.barh(models, accuracy, color=['#4E79A7', '#F28E2B', '#76B7B2'])

# Customize the axes and labels
ax.set_xlabel('Accuracy (%)', fontsize=14)
ax.set_title('Model Performance Over Time', fontsize=18, fontweight='bold', pad=20)
ax.set_xlim(0, 100)
ax.grid(axis='x', linestyle='-', alpha=0.3, color='gray')

# Remove spines for a minimalist look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust tick parameters for a cleaner aesthetic
ax.tick_params(axis='x', colors='gray', length=5, labelsize=12)
ax.tick_params(axis='y', colors='black', length=0, labelsize=14)

# Adding text labels to each bar with consistent positioning
for bar, acc in zip(bars, accuracy):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'{acc}%', va='center', fontsize=13, color='#333')

# Display the chart with tight layout for better spacing
plt.tight_layout()
plt.show()

