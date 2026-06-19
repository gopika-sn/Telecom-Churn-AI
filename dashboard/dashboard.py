import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def show_dashboard():


    st.markdown(
    """
    <div class="card">

    <h2>
    📊 AI Model Dashboard
    </h2>

    <p>
    Telecom customer analytics and model performance overview
    </p>

    </div>

    """,
    unsafe_allow_html=True
    )



    st.write("")



    # ---------------- METRICS ----------------


    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.metric(
            "👥 Total Customers",
            "7043"
        )


    with col2:

        st.metric(
            "⚠️ Churned",
            "1869"
        )


    with col3:

        st.metric(
            "✅ Retained",
            "5174"
        )


    with col4:

        st.metric(
            "📈 Churn Rate",
            "26.5%"
        )





    st.write("")





    # ---------------- DATA GRAPH ----------------



    st.markdown(
    """
    <div class="card">

    <h3>
    Customer Retention Analysis
    </h3>

    </div>
    """,
    unsafe_allow_html=True
    )



    churn_data = pd.DataFrame({

        "Category":
        [
            "Stayed",
            "Churned"
        ],


        "Customers":
        [
            5174,
            1869
        ]

    })



    fig,ax = plt.subplots(
        figsize=(8,4)
    )



    bars=ax.bar(

        churn_data["Category"],

        churn_data["Customers"]

    )



    ax.set_ylabel(
        "Number of Customers"
    )


    ax.set_title(
        "Customer Churn Distribution"
    )



    st.pyplot(fig)







    # ---------------- MODEL PERFORMANCE ----------------



    st.markdown(
    """
    <div class="card">

    <h3>
    🤖 Model Performance
    </h3>


    </div>
    """,

    unsafe_allow_html=True
    )



    col1,col2 = st.columns(2)



    with col1:


        st.metric(
            "Model",
            "XGBoost"
        )


        st.metric(
            "Accuracy",
            "82%"
        )



    with col2:


        st.metric(
            "ROC-AUC Score",
            "0.86"
        )


        st.metric(
            "Prediction Type",
            "Binary Classification"
        )







    # ---------------- FEATURE IMPORTANCE ----------------



    st.markdown(
    """
    <div class="card">

    <h3>
    🔍 Important Churn Factors
    </h3>


    </div>
    """,

    unsafe_allow_html=True
    )



    importance = pd.DataFrame({


        "Feature":[

            "Contract Type",

            "Monthly Charges",

            "Customer Tenure",

            "Payment Method",

            "Internet Service"

        ],



        "Importance":[

            0.32,

            0.25,

            0.18,

            0.15,

            0.10

        ]

    })




    fig,ax = plt.subplots(
        figsize=(8,5)
    )



    ax.barh(

        importance["Feature"],

        importance["Importance"]

    )



    ax.set_xlabel(
        "Impact Score"
    )


    ax.set_title(
        "Top Factors Influencing Churn"
    )


    ax.invert_yaxis()



    st.pyplot(fig)





    # ---------------- INSIGHT ----------------



    st.markdown(

    """

    <div class="card">


    <h3>
    💡 Business Insight
    </h3>


    <p>

    Customers with short contracts,
    higher charges and limited support
    services have a higher probability
    of leaving.

    </p>


    </div>

    """,

    unsafe_allow_html=True

    )