import streamlit as st

def calculate_gpa(subjects):
    total_grade_points = 0
    total_credits = 0

    for subject in subjects:
        grade = subject['grade']
        credits = subject['credits']

        if grade.upper() == 'O':
            grade_points = 10
        elif grade.upper() == 'A+':
            grade_points = 9
        elif grade.upper() == 'A':
            grade_points = 8
        elif grade.upper() == 'B+':
            grade_points = 7
        elif grade.upper() == 'B+':
            grade_points = 6
        elif grade.upper() == 'C+':
            grade_points = 5
        elif grade.upper() == 'C':
            grade_points = 4
        elif grade.upper() == 'F':
            grade_points = 0

        total_grade_points += grade_points * credits
        total_credits += credits

    gpa = total_grade_points / total_credits
    return gpa

def main():
    st.title('GPA Calculator')

    num_subjects = st.number_input('Enter the number of subjects:', min_value=1, step=1)
    subjects = []

    for i in range(num_subjects):
        credits = st.number_input(f'Enter credits for Subject {i+1}:', min_value=0.5, step=0.5)
        grade = st.text_input(f'Enter grade for Subject {i+1} (O, A+, A, B+, B, C+, C, D+, D or F):')

        subjects.append({'credits': credits, 'grade': grade})

    if st.button('Calculate GPA'):
        gpa = calculate_gpa(subjects)
        st.write(f'Your GPA is: {gpa:.2f}')

if __name__ == '__main__':
    main()