import pandas as pd
import matplotlib.pyplot as plt

# Recreating the summary DataFrame from the previous step
data = {
    'severity_label': ['Low', 'Medium', 'High'], 
    'finding_count': [142, 45, 8]  # Example finding counts
}
severity_summary = pd.DataFrame(data)

# 1. Initialize the canvas (width: 8 inches, height: 6 inches)
plt.figure(figsize=(8, 6))

# 2. Define semantic colors (Green for Low, Orange for Medium, Red for High)
colors = ['#2ca02c', '#ff7f0e', '#d62728']

# 3. Create the bar plot
bars = plt.bar(
    severity_summary['severity_label'], 
    severity_summary['finding_count'], 
    color=colors,
    width=0.6
)

# 4. Add data labels on top of each bar for instant readability
for bar in bars:
    yval = bar.get_height()
    # Position the text horizontally centered and slightly above the bar
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# 5. Add titles and axis labels
plt.title('AWS GuardDuty Findings by Severity', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Severity Level', fontsize=12, labelpad=10)
plt.ylabel('Total Findings', fontsize=12, labelpad=10)

# 6. Clean up the aesthetics (remove top and right borders)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 7. Render the chart
plt.tight_layout() # Ensures labels don't get cut off
plt.show()