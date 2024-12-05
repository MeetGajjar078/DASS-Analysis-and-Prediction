#Made By Meet Gajjar
import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt

# Load Feature Columns
def load_feature_columns():
    if os.path.exists("feature_columns.pkl"):
        with open("feature_columns.pkl", "rb") as f:
            return pickle.load(f)
    st.error("Feature columns file not found.")
    return None

# Load Pre-Trained Model
def load_model(model_name):
    file_name = f"{model_name}.pkl"
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    st.error(f"Model file not found: {file_name}")
    return None

# First Page: DASS Information
def dass_information():
    st.title("Depression, Anxiety, and Stress Scales (DASS)")
    st.write("""
The DASS is a set of three self-report scales designed to measure the negative emotional states of depression, anxiety and stress. The DASS was constructed not merely as another set of scales to measure conventionally defined emotional states, but to further the process of defining, understanding, and measuring the ubiquitous and clinically significant emotional states usually described as depression, anxiety and stress. The DASS should thus meet the requirements of both researchers and scientist-professional clinicians.

Each of the three DASS scales contains 14 items, divided into subscales of 2-5 items with similar content. The Depression scale assesses dysphoria, hopelessness, devaluation of life, self-deprecation, lack of interest/involvement, anhedonia, and inertia. The Anxiety scale assesses autonomic arousal, skeletal muscle effects, situational anxiety, and subjective experience of anxious affect. The Stress scale is sensitive to levels of chronic non-specific arousal. It assesses difficulty relaxing, nervous arousal, and being easily upset/agitated, irritable/over-reactive and impatient. Subjects are asked to use 4-point severity/frequency scales to rate the extent to which they have experienced each state over the past week. Scores for Depression, Anxiety and Stress are calculated by summing the scores for the relevant items.

In addition to the basic 42-item questionnaire, a short version, the DASS21, is available with 7 items per scale. Note also that an earlier version of the DASS scales was referred to as the Self-Analysis Questionnaire (SAQ).

As the scales of the DASS have been shown to have high internal consistency and to yield meaningful discriminations in a variety of settings, the scales should meet the needs of both researchers and clinicians who wish to measure current state or change in state over time (e.g., in the course of treatment) on the three dimensions of depression, anxiety and stress.


## Characteristics of high scorers on each DASS scale

Depression scale

self-disparaging
dispirited, gloomy, blue
convinced that life has no meaning or value
pessimistic about the future
unable to experience enjoyment or satisfaction
unable to become interested or involved
slow, lacking in initiative
Anxiety scale

apprehensive, panicky
trembly, shaky
aware of dryness of the mouth, breathing difficulties, pounding of the heart, sweatiness of the palms
worried about performance and possible loss of control
Stress scale

over-aroused, tense
unable to relax
touchy, easily upset
irritable
easily startled
nervy, jumpy, fidgety
intolerant of interruption or delay
## The DASS in research

The DASS may be administered either in groups or individually for research purposes. The capacity to discriminate between the three related states of depression, anxiety and stress should be useful to researchers concerned with the nature, aetiology and mechanisms of emotional disturbance.

As the essential development of the DASS was carried out with non-clinical samples, it is suitable for screening normal adolescents and adults. Given the necessary language proficiency, there seems no compelling case against use of the scales for comparative purposes with children as young as 12 years. It must be borne in mind, however, that the lower age limit of the development samples was 17 years.

## Clinical use of the DASS

The principal value of the DASS in a clinical setting is to clarify the locus of emotional disturbance, as part of the broader task of clinical assessment. The essential function of the DASS is to assess the severity of the core symptoms of depression, anxiety and stress. It must be recognised that clinically depressed, anxious or stressed persons may well manifest additional symptoms that tend to be common to two or all three of the conditions, such as sleep, appetite, and sexual disturbances. These disturbances will be elicited by clinical examination, or by the use of general symptom check lists as required.

The DASS may be administered and scored by non-psychologists, but decisions based on particular score profiles should be made only by experienced clinicians who have carried out an appropriate clinical examination. It should be noted also that none of the DASS items refers to suicidal tendencies because items relating to such tendencies were found not to load on any scale. The experienced clinician will recognise the need to determine the risk of suicide in seriously disturbed persons.

## The DASS and diagnosis

The DASS is based on a dimensional rather than a categorical conception of psychological disorder. The assumption on which the DASS development was based (and which was confirmed by the research data) is that the differences between the depression, the anxiety, and the stress experienced by normal subjects and the clinically disturbed, are essentially differences of degree. The DASS therefore has no direct implications for the allocation of patients to discrete diagnostic categories postulated in classificatory systems such as the DSM and ICD. However, recommended cutoffs for conventional severity labels (normal, moderate, severe) are given in the DASS Manual.
    """)

# Second Page: Prediction Panel
def prediction_panel():
    st.title("Prediction Panel")
    st.subheader("Please provide your responses to the questionnaire:")

    # Placeholder for questions
    user_data = {f"Q{i}A": st.slider(f"Question {i}", 0, 3, 1) for i in range(1, 43)}  # Replace "Question {i}" with actual questions
    user_df = pd.DataFrame([user_data])

    # Align columns with the saved feature names
    feature_columns = load_feature_columns()
    if feature_columns is not None and len(feature_columns) > 0:
        user_df = user_df.reindex(columns=feature_columns, fill_value=0)
    else:
        st.error("Feature columns are missing or invalid. Please train the models.")
        return

    if st.button("Submit"):
        depression_model = load_model("Depression")
        anxiety_model = load_model("Anxiety")
        stress_model = load_model("Stress")

        if depression_model and anxiety_model and stress_model:
            depression_prediction = depression_model.predict(user_df)[0]
            anxiety_prediction = anxiety_model.predict(user_df)[0]
            stress_prediction = stress_model.predict(user_df)[0]

            st.write("### Prediction Results")
            st.write(f"**Depression Condition:** {depression_prediction}")
            st.write(f"**Anxiety Condition:** {anxiety_prediction}")
            st.write(f"**Stress Condition:** {stress_prediction}")
        else:
            st.error("One or more models are not loaded. Please train all models.")

# Third Page: Information Gathering
def information_gathering():
    st.title("Information Gathering Panel")
    st.subheader("Please provide the following details:")

    fields = {
        "Education Level": st.selectbox("Education Level", ["High School", "Undergraduate", "Graduate", "Postgraduate"]),
        "Urban or Rural": st.selectbox("Location Type", ["Urban", "Rural"]),
        "Gender": st.selectbox("Gender", ["Male", "Female", "Other"]),
        "Age": st.number_input("Age", min_value=10, max_value=100, value=25),
        "Screen Size (in inches)": st.number_input("Screen Size", min_value=0, max_value=100, value=15),
        "Hand Dominance": st.selectbox("Dominant Hand", ["Right", "Left"]),
        "Religion": st.text_input("Religion"),
        "Family Size": st.number_input("Family Size", min_value=1, max_value=20, value=4),
        "Major": st.text_input("Major"),
    }

    if st.button("Submit Information"):
        st.success("Information Saved Successfully!")
        st.write("### Submitted Information:")
        st.write(fields)

# Fourth Page: Dynamic Visualizations
def visualizations():
    st.title("Dynamic Visualizations")
    st.subheader("Visualize Information")

    # Sample Data
    data = pd.DataFrame({
        "Category": ["Education", "Gender", "Age Group", "Location"],
        "Count": [50, 40, 35, 25],
    })

    # Pie Chart
    st.subheader("Pie Chart")
    fig1, ax1 = plt.subplots()
    ax1.pie(data["Count"], labels=data["Category"], autopct='%1.1f%%', startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    # Bar Chart
    st.subheader("Bar Chart")
    fig2, ax2 = plt.subplots()
    ax2.bar(data["Category"], data["Count"], color="skyblue")
    ax2.set_title("Category Distribution")
    ax2.set_ylabel("Count")
    st.pyplot(fig2)

# Main App
def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio(
        "Choose a section:",
        ["DASS Information", "Prediction Panel", "Information Gathering", "Visualizations"]
    )

    if options == "DASS Information":
        dass_information()
    elif options == "Prediction Panel":
        prediction_panel()
    elif options == "Information Gathering":
        information_gathering()
    elif options == "Visualizations":
        visualizations()

if __name__ == "__main__":
    main()