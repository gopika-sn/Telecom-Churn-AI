def create_report(
    risk,
    probability,
    reasons,
    recommendations
):

    report=f"""

Telecom Churn AI Report
=======================


Risk Level:
{risk}


Churn Probability:
{probability:.2%}



Reasons:
"""

    for r in reasons:
        report += "\n"+r


    report += """


Recommendations:
"""


    for rec in recommendations:
        report += "\n"+rec


    return report