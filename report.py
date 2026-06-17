def print_report(df, averages, topper, at_risk):
    print("\n" + "="*50)
    print("       STUDENT PERFORMANCE REPORT")
    print("="*50)

    print(f"\n📌 Total Students: {len(df)}")

    print("\n📚 Subject-wise Class Averages:")
    for subject, avg in averages.items():
        print(f"   {subject:<12}: {avg}")

    print(f"\n🏆 Class Topper: {topper['Name']}  (Average: {topper['Average']})")

    print("\n⚠️  At-Risk Students (Average < 50):")
    if at_risk.empty:
        print("   None! Great class performance.")
    else:
        for _, row in at_risk.iterrows():
            print(f"   {row['Name']:<12} — Average: {row['Average']}")

    print("\n📋 Full Student Summary:")
    print(df[['Name', 'Total', 'Average', 'Grade']].to_string(index=False))
    print("\n" + "="*50)