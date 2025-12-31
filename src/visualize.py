import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Create output directory for plots
OUTPUT_DIR = "plots"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_timestamp():
    """Generate timestamp for filenames"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def plot_price_trends(price_df):
    """Plot stock price trends and save to file"""
    plt.figure(figsize=(12, 6))
    price_df.plot(figsize=(12, 6))
    plt.title("Stock Price Trends", fontsize=16, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price ($)", fontsize=12)
    plt.legend(title="Stocks", loc="best")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    filename = os.path.join(OUTPUT_DIR, f"price_trends_{get_timestamp()}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"   💾 Price trends plot saved to: {filename}")
    
    # Display the plot
    plt.show()

def plot_correlation_heatmap(corr_matrix):
    """Plot correlation heatmap and save to file"""
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0, 
                square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                vmin=-1, vmax=1, fmt='.2f')
    plt.title("Stock Correlation Heatmap", fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    # Save the plot
    filename = os.path.join(OUTPUT_DIR, f"correlation_heatmap_{get_timestamp()}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"   💾 Correlation heatmap saved to: {filename}")
    
    # Display the plot
    plt.show()

def plot_returns_distribution(returns_df):
    """Plot returns distribution for each stock"""
    fig, axes = plt.subplots(1, len(returns_df.columns), figsize=(14, 4))
    
    if len(returns_df.columns) == 1:
        axes = [axes]
    
    for idx, stock in enumerate(returns_df.columns):
        axes[idx].hist(returns_df[stock], bins=50, alpha=0.7, edgecolor='black')
        axes[idx].set_title(f"{stock} Returns Distribution")
        axes[idx].set_xlabel("Daily Returns")
        axes[idx].set_ylabel("Frequency")
        axes[idx].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    filename = os.path.join(OUTPUT_DIR, f"returns_distribution_{get_timestamp()}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"   💾 Returns distribution plot saved to: {filename}")
    
    # Display the plot
