
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def check_compliance(text, checklist):
    results = []

    for item in checklist:
        prompt = f"""
You are a compliance checker.

Checklist Item: {item}

Document Content:
{text[:4000]}

Does the document satisfy the checklist item? Answer Yes or No with a short explanation.
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0
            )
            content = response.choices[0].message.content
            if "yes" in content.lower():
                status = "Yes"
            elif "no" in content.lower():
                status = "No"
            else:
                status = "Unknown"

            results.append({
                "Checklist Item": item,
                "Status": status,
                "Notes": content
            })

        except Exception as e:
            results.append({
                "Checklist Item": item,
                "Status": "Error",
                "Notes": str(e)
            })

    return results
