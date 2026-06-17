import matplotlib.pyplot as plt

def plot_subject_averages(averages):
    plt.figure(figsize=(8, 5))
    bars = plt.bar(averages.index, averages.values, color='steelblue', edgecolor='black')
    plt.title('Subject-wise Class Averages', fontsize=14, fontweight='bold')
    plt.xlabel('Subject')
    plt.ylabel('Average Marks')
    plt.ylim(0, 100)
    for bar, val in zip(bars, averages.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 str(val), ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('subject_averages.png')
    plt.show()

def plot_grade_distribution(df):
    grade_counts = df['Grade'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(grade_counts.values, labels=grade_counts.index,
            autopct='%1.1f%%', startangle=140,
            colors=['#4CAF50','#8BC34A','#FFC107','#FF9800','#F44336','#9E9E9E'])
    plt.title('Grade Distribution', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('grade_distribution.png')
    plt.show()

def plot_top5_students(df):
    top5 = df.nlargest(5, 'Average')[['Name', 'Average']]
    plt.figure(figsize=(8, 5))
    plt.barh(top5['Name'], top5['Average'], color='mediumseagreen', edgecolor='black')
    plt.title('Top 5 Students by Average', fontsize=14, fontweight='bold')
    plt.xlabel('Average Marks')
    plt.xlim(0, 100)
    for i, val in enumerate(top5['Average']):
        plt.text(val + 0.5, i, str(val), va='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('top5_students.png')
    plt.show()