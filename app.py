import streamlit as st

# Placeholder functions for risk algorithms (using general guidelines for stratification)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    return "High" if risk_score > 15 else "Moderate" if risk_score > 10 else "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02) + (hba1c * 0.1)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 15 else "Low"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1) + (exacerbations_last_year * 5)
    return "High" if risk_score > 25 else "Moderate" if risk_score > 15 else "Low"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    risk_score = (frequency_of_symptoms * 2) + (nighttime_symptoms * 3) + (inhaler_use * 1.5) - (fev1 * 0.1) + (eosinophil_count * 0.2)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 10 else "Low"

# Enhanced AI Assistant response with MDT support and references
def ai_assistant_response(query, results):
    response = ""
    high_risk_conditions = [condition for condition, risk in results.items() if risk == "High"]
    moderate_risk_conditions = [condition for condition, risk in results.items() if risk == "Moderate"]

    if high_risk_conditions or moderate_risk_conditions:
        response += "Here’s a detailed, multidisciplinary care plan based on current evidence:\n\n"

        for condition, risk in results.items():
            if risk == "High":
                response += f"**{condition} (High Risk):**\n"
                if condition == "Cardiovascular":
                    response += "- **Primary Care Physician**: Immediate review of medication, adjust therapy, and consider frequent specialist referrals.\n"
                    response += "- **Nurse**: Weekly patient check-ins to monitor adherence and symptoms.\n"
                    response += "- **Dietitian**: Design a personalized nutrition plan that supports condition management.\n"
                    response += "- **References**: AHA/ACC 2024 Guidelines for Heart Disease Management.\n\n"
                elif condition == "Diabetes":
                    response += "- **Endocrinologist**: Intensive insulin therapy and continuous glucose monitoring.\n"
                    response += "- **Nurse**: Monthly visits to monitor HbA1c and blood glucose levels.\n"
                    response += "- **Dietitian**: Develop a comprehensive dietary plan.\n"
                    response += "- **References**: ADA Standards of Medical Care in Diabetes 2024.\n\n"
                elif condition == "COPD":
                    response += "- **Respiratory Therapist**: Implement pulmonary rehabilitation, monitor inhaler techniques.\n"
                    response += "- **Nurse**: Weekly assessments to track symptoms and medication adherence.\n"
                    response += "- **References**: GOLD 2024 Guidelines for COPD Management.\n\n"
                elif condition == "Asthma":
                    response += "- **Pulmonologist**: Evaluate and adjust asthma medications based on symptom control.\n"
                    response += "- **Nurse**: Frequent monitoring of asthma action plans.\n"
                    response += "- **References**: GINA 2024 Guidelines for Asthma Management.\n\n"
            elif risk == "Moderate":
                response += f"**{condition} (Moderate Risk):**\n"
                if condition == "Cardiovascular":
                    response += "- **Primary Care Physician**: Monthly reviews of patient status and lifestyle modifications.\n"
                    response += "- **Nurse**: Educate on symptom tracking, quarterly visits to reinforce care plan.\n"
                    response += "- **References**: AHA/ACC 2024 Guidelines for Heart Disease Management.\n\n"
                elif condition == "Diabetes":
                    response += "- **Endocrinologist**: Focus on lifestyle changes and regular blood glucose monitoring.\n"
                    response += "- **Nurse**: Quarterly follow-ups to assess treatment efficacy.\n"
                    response += "- **References**: ADA Standards of Medical Care in Diabetes 2024.\n\n"
                elif condition == "COPD":
                    response += "- **Respiratory Therapist**: Reinforce inhaler technique and symptom tracking.\n"
                    response += "- **Nurse**: Monthly check-ins to assess lung function and medication adherence.\n"
                    response += "- **References**: GOLD 2024 Guidelines for COPD Management.\n\n"
                elif condition == "Asthma":
                    response += "- **Pulmonologist**: Regular assessment of medication effectiveness and symptom control.\n"
                    response += "- **Nurse**: Ensure proper technique with inhalers and adherence to medication.\n"
                    response += "- **References**: GINA 2024 Guidelines for Asthma Management.\n\n"

        response += "\nPlease consult specific guidelines for detailed recommendations."

    return response

# Initialize session state to store results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Streamlit App Layout
st.title("Comprehensive Multi-Condition Risk Stratification, Care Plan, and AI Assistant")
st.write("This app assesses risk for chronic conditions, provides a unified care plan for multiple conditions, and includes an AI assistant for personalized queries.")

# Define tabs for each condition and the AI Assistant
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan", "AI Assistant"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)
    smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker"])

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.6)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1_copd = st.number_input("FEV1 (%) - COPD", min_value=20, max_value=100, value=80)
    exacerbations_last_year = st.number_input("Number of COPD Exacerbations in Last Year", min_value=0, max_value=10, value=0)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1_copd, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Asthma Symptoms (0-7 days/week)", 0, 7, 2)
    nighttime_symptoms = st.slider("Nighttime Symptoms (0-7 days/week)", 0, 7, 1)
    inhaler_use = st.slider("Inhaler Use (0-7 days/week)", 0, 7, 2)
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80)
    eosinophil_count = st.number_input("Eosinophil Count (cells/μL)", min_value=0, max_value=1000, value=300)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        for condition, risk in st.session_state['results'].items():
            st.write(f"### {condition} - {risk} Risk")
            if risk == "High":
                st.write(f"- **{condition} - High Risk**: Intensive care plan with evidence-based guidelines:")
                if condition == "Cardiovascular":
                    st.write("- **Self-Management Support**: Medication adherence, regular exercise, and dietary changes as per AHA.\n"
                             "- **Decision Support**: Schedule monthly follow-ups, focus on lifestyle modifications.\n"
                             "- **Delivery System Design**: Regular monitoring of vital signs and medication adjustments.\n"
                             "- **Community Resources**: Refer to local support groups and educational workshops.")
                elif condition == "Diabetes":
                    st.write("- **Self-Management Support**: Encourage daily blood glucose monitoring and dietary adjustments as per ADA.\n"
                             "- **Decision Support**: Quarterly follow-ups for HbA1c monitoring and adjustment of treatment.\n"
                             "- **Delivery System Design**: Ensure access to diabetes education programs.\n"
                             "- **Community Resources**: Connect to local diabetes associations for support.")
                elif condition == "COPD":
                    st.write("- **Self-Management Support**: Implement daily symptom tracking and proper inhaler use as per GOLD.\n"
                             "- **Decision Support**: Schedule follow-ups every month to adjust medication.\n"
                             "- **Delivery System Design**: Facilitate access to pulmonary rehabilitation.\n"
                             "- **Community Resources**: Local COPD support groups and educational resources.")
                elif condition == "Asthma":
                    st.write("- **Self-Management Support**: Monitor symptoms daily and utilize an asthma action plan as per GINA.\n"
                             "- **Decision Support**: Regular follow-ups every three months for medication adjustment.\n"
                             "- **Delivery System Design**: Access to allergen avoidance strategies and trigger management.\n"
                             "- **Community Resources**: Local asthma education and support services.")
            elif risk == "Moderate":
                st.write(f"- **{condition} - Moderate Risk**: Intermediate care plan with CCM recommendations:")
                if condition == "Cardiovascular":
                    st.write("- **Self-Management Support**: Encourage lifestyle changes, provide tools for tracking symptoms, and set achievable health goals.\n"
                             "- **Decision Support**: Schedule quarterly check-ups with a focus on preventive care.\n"
                             "- **Delivery System Design**: Semi-annual follow-up visits, proactive medication adjustments, and referral as needed.\n"
                             "- **Community Resources**: Connect with local health education resources.")
                elif condition == "Diabetes":
                    st.write("- **Self-Management Support**: Encourage lifestyle changes, provide tools for tracking symptoms, and set achievable health goals.\n"
                             "- **Decision Support**: Schedule quarterly check-ups with a focus on preventive care.\n"
                             "- **Delivery System Design**: Semi-annual follow-up visits, proactive medication adjustments, and referral as needed.\n"
                             "- **Community Resources**: Connect with local health education resources.")
                elif condition == "COPD":
                    st.write("- **Self-Management Support**: Encourage lifestyle changes, provide tools for tracking symptoms, and set achievable health goals.\n"
                             "- **Decision Support**: Schedule quarterly check-ups with a focus on preventive care.\n"
                             "- **Delivery System Design**: Semi-annual follow-up visits, proactive medication adjustments, and referral as needed.\n"
                             "- **Community Resources**: Connect with local health education resources.")
                elif condition == "Asthma":
                    st.write("- **Self-Management Support**: Encourage lifestyle changes, provide tools for tracking symptoms, and set achievable health goals.\n"
                             "- **Decision Support**: Schedule quarterly check-ups with a focus on preventive care.\n"
                             "- **Delivery System Design**: Semi-annual follow-up visits, proactive medication adjustments, and referral as needed.\n"
                             "- **Community Resources**: Connect with local health education resources.")
            else:
                st.write(f"- **{condition} - Low Risk**: Preventive and maintenance plan based on CCM recommendations.")
                if condition == "Cardiovascular":
                    st.write("- **Self-Management Support**: Encourage regular health checks and adherence to preventive lifestyle practices.\n"
                             "- **Decision Support**: Annual review of patient health status.\n"
                             "- **Delivery System Design**: Ensure primary care check-ups annually or biannually.\n"
                             "- **Community Resources**: Provide information on health maintenance resources.")
                elif condition == "Diabetes":
                    st.write("- **Self-Management Support**: Encourage regular health checks and adherence to preventive lifestyle practices.\n"
                             "- **Decision Support**: Annual review of patient health status.\n"
                             "- **Delivery System Design**: Ensure primary care check-ups annually or biannually.\n"
                             "- **Community Resources**: Provide information on health maintenance resources.")
                elif condition == "COPD":
                    st.write("- **Self-Management Support**: Encourage regular health checks and adherence to preventive lifestyle practices.\n"
                             "- **Decision Support**: Annual review of patient health status.\n"
                             "- **Delivery System Design**: Ensure primary care check-ups annually or biannually.\n"
                             "- **Community Resources**: Provide information on health maintenance resources.")
                elif condition == "Asthma":
                    st.write("- **Self-Management Support**: Encourage regular health checks and adherence to preventive lifestyle practices.\n"
                             "- **Decision Support**: Annual review of patient health status.\n"
                             "- **Delivery System Design**: Ensure primary care check-ups annually or biannually.\n"
                             "- **Community Resources**: Provide information on health maintenance resources.")

# AI Assistant Tab
with tab6:
    st.header("AI Assistant (Multidisciplinary Team) for Healthcare Provider Guidance")
    query = st.text_input("Ask the AI Assistant about risk management, personalized care, or guidelines:")
    if st.button("Get AI Assistance"):
        if st.session_state['results']:
            ai_response = ai_assistant_response(query, st.session_state['results'])
            st.write(ai_response)
        else:
            st.write("Please complete risk assessments in previous tabs first.")
