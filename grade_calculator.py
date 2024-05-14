import streamlit as st

def calculate_grade(test_scores):
    # Define your grading scale here
    grading_scale = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }

    total_score = sum(test_scores)
    average_score = total_score / len(test_scores)

    for grade, (lower_bound, upper_bound) in grading_scale.items():
        if lower_bound <= average_score <= upper_bound:
            return grade

def main():
    st.title('Simple Grade Calculator')

    num_tests = st.number_input('Enter the number of tests:', min_value=1, step=1)
    test_scores = []

    for i in range(num_tests):
        score = st.number_input(f'Enter score for Test {i+1}:', min_value=0, max_value=100, step=1)
        test_scores.append(score)

    if st.button('Calculate Grade'):
        final_grade = calculate_grade(test_scores)
        st.write(f'Your final grade is: {final_grade}')

if __name__ == '__main__':
    main()