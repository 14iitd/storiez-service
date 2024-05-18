import matplotlib.pyplot as plt

# Data
data = [
    ("England", "inns & 579 runs", "v Australia"),
    ("Australia", "inns & 360 runs", "v South Africa"),
    ("West Indies", "inns & 336 runs", "v India"),
    ("Australia", "inns & 332 runs", "v England"),
    ("Pakistan", "inns & 324 runs", "v New Zealand"),
    ("West Indies", "inns & 322 runs", "v New Zealand"),
    ("West Indies", "inns & 310 runs", "v Bangladesh"),
    ("New Zealand", "inns & 301 runs", "v Zimbabwe"),
    ("New Zealand", "inns & 294 runs", "v Zimbabwe"),
    ("England", "inns & 285 runs", "v India"),
    ("England", "inns & 283 runs", "v West Indies"),
    ("Sri Lanka", "inns & 280 runs", "v Ireland"),
    ("New Zealand", "inns & 276 runs", "v South Africa"),
    ("India", "inns & 272 runs", "v West Indies")
]

# Separate the data into different lists
winners = [f"{item[0]} {item[2]}" for item in data]  # Combine winner and opposition for unique labels
margins = [int(item[1].split('&')[1].split()[0]) for item in data]  # Extract the numeric part of the margin
full_margins = [item[1] for item in data]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data
bars = ax.barh(winners, margins, color='skyblue')

# Add data labels
for bar, full_margin in zip(bars, full_margins):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, full_margin,
            va='center', ha='left', fontsize=9)

# Set titles and labels
ax.set_title('Largest Winning Margins in Test Cricket (by innings)', fontsize=16)
ax.set_xlabel('Margin (innings & runs)', fontsize=12)
ax.set_ylabel('Winner vs Opposition', fontsize=12)
plt.gca().invert_yaxis()  # Invert y-axis to have the largest margin on top

# Save the figure
plt.savefig('largest_winning_margins.png')

# Show the plot
plt.show()
