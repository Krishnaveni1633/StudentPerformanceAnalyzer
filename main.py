from data_loader import load_data
from analyzer import get_student_totals, get_subject_averages, get_topper, get_at_risk_students
from visualizer import plot_subject_averages, plot_grade_distribution, plot_top5_students
from report import print_report

DATA_FILE = "students.csv"

def main():
    print("🚀 Starting Student Performance Analyzer...\n")

    df = load_data(DATA_FILE)
    df = get_student_totals(df)

    averages = get_subject_averages(df)
    topper = get_topper(df)
    at_risk = get_at_risk_students(df)

    print_report(df, averages, topper, at_risk)

    plot_subject_averages(averages)
    plot_grade_distribution(df)
    plot_top5_students(df)

    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()