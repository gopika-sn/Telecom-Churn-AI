import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import os
import sys
import csv
from datetime import datetime



# ---------------- PAGE ----------------


st.set_page_config(
    page_title="Telecom Churn AI",
    page_icon="📡",
    layout="wide"
)




# ---------------- PATH ----------------


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



model = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "churn_model.pkl"
    )
)



features = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "feature_names.pkl"
    )
)




sys.path.append(BASE_DIR)

from dashboard.dashboard import show_dashboard






# ---------------- REPORT ----------------


def create_report(
    risk,
    probability,
    reasons,
    recommendations
):

    report = f"""

Telecom Churn AI Report
=======================


Risk Level:
{risk}


Churn Probability:
{probability:.2%}



Reasons:

"""


    for r in reasons:

        report += "\n" + r



    report += "\n\nRecommendations:\n"



    for r in recommendations:

        report += "\n" + r



    return report







# ---------------- HISTORY ----------------


def save_history(
    risk,
    probability,
    contract,
    monthly
):


    file=os.path.join(

        BASE_DIR,

        "database",

        "history.csv"

    )


    os.makedirs(

        os.path.dirname(file),

        exist_ok=True

    )


    with open(

        file,

        "a",

        newline=""

    ) as f:



        writer=csv.writer(f)


        writer.writerow(

        [

        datetime.now(),

        risk,

        f"{probability:.2%}",

        contract,

        monthly

        ]

        )









# ---------------- FEATURE NAMES ----------------


friendly_names={


"SeniorCitizen":
"Senior Citizen",


"tenure":
"Customer Loyalty Period",


"MonthlyCharges":
"Monthly Bill Amount",


"Partner_Yes":
"Has Partner",


"Dependents_Yes":
"Has Dependents",


"InternetService_Fiber optic":
"Fiber Internet",


"InternetService_DSL":
"DSL Internet",


"Contract_One year":
"One Year Contract",


"Contract_Two year":
"Two Year Contract",


"OnlineSecurity_Yes":
"Online Security",


"TechSupport_Yes":
"Technical Support",


"PaymentMethod_Electronic check":
"Electronic Check Payment"


}




display_features=[

friendly_names.get(

x,

x.replace("_"," ").title()

)

for x in features

]








# ---------------- UI ----------------


st.markdown(

"""

<style>


*{

font-family:"Times New Roman",serif;

}



.stApp{


background:

radial-gradient(

circle at top,

#123b66,

#020617 75%

);


}



.block-container{


max-width:1100px;

}




.card{


background:

rgba(15,23,42,0.65);


backdrop-filter:

blur(25px);


padding:

28px;


border-radius:

30px;


margin-bottom:

25px;


border:

1px solid rgba(255,255,255,0.15);


}



h1,h2,h3,p,label{

color:white !important;

}




.stButton button{


width:100%;


height:50px;


border-radius:20px;


background:

linear-gradient(

135deg,

#0284c7,

#2563eb

);


color:white;


font-size:18px;


}



</style>

""",

unsafe_allow_html=True

)









# ---------------- HEADER ----------------


st.markdown(

"""

<div class="card">


<h1>
📡 Telecom Customer Churn AI
</h1>


<p>
Explainable AI Customer Retention Platform
</p>


</div>

""",

unsafe_allow_html=True

)






# ---------------- DASHBOARD ----------------


show_dashboard()



st.divider()







# ---------------- INPUT ----------------


st.markdown(

"""

<div class="card">

<h2>
👤 Customer Details
</h2>

""",

unsafe_allow_html=True

)



col1,col2=st.columns(2)



with col1:


    tenure=st.slider(

        "Customer Tenure (months)",

        0,

        72,

        12

    )


    senior=st.selectbox(

        "Senior Citizen",

        ["No","Yes"]

    )


    partner=st.selectbox(

        "Has Partner",

        ["No","Yes"]

    )


    dependents=st.selectbox(

        "Has Dependents",

        ["No","Yes"]

    )




with col2:


    internet=st.selectbox(

        "Internet Service",

        [

        "DSL",

        "Fiber optic",

        "No"

        ]

    )



    contract=st.selectbox(

        "Contract Type",

        [

        "Month-to-month",

        "One year",

        "Two year"

        ]

    )


    security=st.selectbox(

        "Online Security",

        ["No","Yes"]

    )


    support=st.selectbox(

        "Tech Support",

        ["No","Yes"]

    )




st.markdown(

"</div>",

unsafe_allow_html=True

)






# ---------------- BILLING ----------------


st.markdown(

"""

<div class="card">

<h2>
💳 Billing
</h2>


""",

unsafe_allow_html=True

)



monthly=st.number_input(

"Monthly Charges",

0.0,

200.0,

70.0

)



payment=st.selectbox(

"Payment Method",

[

"Electronic check",

"Mailed check",

"Credit card (automatic)",

"Bank transfer (automatic)"

]

)



st.markdown(

"</div>",

unsafe_allow_html=True

)








# ---------------- MODEL ----------------


if st.button(

"🔍 Analyze Customer"

):



    data={}



    for col in features:

        data[col]=0




    data["tenure"]=tenure


    data["MonthlyCharges"]=monthly




    if senior=="Yes":

        data["SeniorCitizen"]=1



    if partner=="Yes":

        data["Partner_Yes"]=1



    if dependents=="Yes":

        data["Dependents_Yes"]=1



    if internet=="DSL":

        data["InternetService_DSL"]=1


    elif internet=="Fiber optic":

        data["InternetService_Fiber optic"]=1




    if contract=="One year":

        data["Contract_One year"]=1


    elif contract=="Two year":

        data["Contract_Two year"]=1




    if security=="Yes":

        data["OnlineSecurity_Yes"]=1



    if support=="Yes":

        data["TechSupport_Yes"]=1




    if payment=="Electronic check":

        data["PaymentMethod_Electronic check"]=1






    input_df=pd.DataFrame(

        [data]

    )[features]




    prediction=model.predict(

        input_df

    )[0]




    probability=model.predict_proba(

        input_df

    )[0][1]





    reasons=[]


    recommendations=[

    "Offer loyalty discounts",

    "Encourage yearly contracts",

    "Improve customer support"

    ]





    if prediction==1:


        risk="HIGH"


        st.error(

        f"""

        🚨 HIGH CHURN RISK


        Probability:

        {probability:.2%}

        """

        )



        if tenure<12:

            reasons.append(
            "New customer with low loyalty"
            )



        if monthly>80:

            reasons.append(
            "High monthly charges"
            )



        if contract=="Month-to-month":

            reasons.append(
            "Month-to-month contract"
            )



        if support=="No":

            reasons.append(
            "No technical support"
            )



    else:


        risk="LOW"



        st.success(

        f"""

        ✅ CUSTOMER LIKELY TO STAY


        Probability:

        {probability:.2%}

        """

        )


        reasons.append(

        "Strong retention signals"

        )







    # SAVE HISTORY


    save_history(

        risk,

        probability,

        contract,

        monthly

    )







    # REPORT


    st.markdown(

    """

    <div class="card">

    <h2>
    📋 AI Retention Report
    </h2>

    </div>

    """,

    unsafe_allow_html=True

    )




    for r in reasons:

        st.write(

        "🟠",

        r

        )




    st.info(

    """

    Recommended Actions:


    ✅ Loyalty offers

    ✅ Contract upgrade benefits

    ✅ Better support


    """

    )






    report=create_report(

        risk,

        probability,

        reasons,

        recommendations

    )



    st.download_button(

    "⬇️ Download AI Report",

    report,

    "churn_report.txt"

    )








    # SHAP


    st.markdown(

    """

    <div class="card">


    <h2>
    🧠 AI Explanation
    </h2>


    </div>

    """,

    unsafe_allow_html=True

    )





    explainer=shap.TreeExplainer(model)



    shap_values=explainer.shap_values(

        input_df

    )




    shap_df=pd.DataFrame({

    "Feature":

    display_features,


    "Impact":

    shap_values[0]

    })




    shap_df=shap_df.sort_values(

    "Impact",

    key=abs,

    ascending=False

    ).head(8)





    fig,ax=plt.subplots(

        figsize=(6,3)

    )



    ax.barh(

        shap_df["Feature"],

        shap_df["Impact"]

    )



    ax.invert_yaxis()



    ax.set_title(

    "Main Factors Affecting Churn"

    )



    st.pyplot(

    fig,

    use_container_width=False

    )









# ---------------- HISTORY VIEW ----------------


st.divider()



st.markdown(

"""

<div class="card">

<h2>
📜 Prediction History
</h2>


</div>

""",

unsafe_allow_html=True

)



history_file=os.path.join(

BASE_DIR,

"database",

"history.csv"

)




if os.path.exists(history_file):


    history=pd.read_csv(

        history_file,

        names=[

        "Time",

        "Risk",

        "Probability",

        "Contract",

        "Monthly Charges"

        ]

    )



    st.dataframe(

        history,

        use_container_width=True

    )



else:


    st.info(

    "No predictions yet"

    )