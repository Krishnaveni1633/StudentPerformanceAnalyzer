def get_subject_averages(df):
    subjects = df.select_dtypes(include='number').columns
    averages = df[subjects].mean().round(2)
    return averages

def get_student_totals(df):
    subjects = df.select_dtypes(include='number').columns
    df = df.copy()
    df['Total'] = df[subjects].sum(axis=1)
    df['Average'] = df[subjects].mean(axis=1).round(2)
    df['Grade'] = df['Average'].apply(assign_grade)
    return df

def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def get_topper(df):
    return df.loc[df['Average'].idxmax()]

def get_at_risk_students(df, threshold=50):
    return df[df['Average'] < threshold]