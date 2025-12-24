import streamlit as st
from langchain.llms import OpenAI

st.set_page_config(page_title="Ad Copy Generator")

st.title("Brand-Aware Ad Copy Generator")

st.markdown(
    """
Generate short ad copy variations while keeping brand tone
and competitive context in mind.
"""
)

brand_tone = st.text_area(
    "Brand Tone / Guidelines",
    height=150,
    placeholder="Example: Friendly, minimal, performance-focused..."
)

product_details = st.text_area(
    "Product Description",
    height=150,
    placeholder="What is the product? Key features?"
)

competitor_context = st.text_area(
    "Competitor Messaging (optional)",
    height=150,
    placeholder="How competitors describe similar products"
)

def generate_ad_copy(brand, product, competitor):
    llm = OpenAI(temperature=0.7)

    prompt = f"""
You are writing ad copy for a D2C brand.

Brand tone:
{brand}

Product details:
{product}

Competitor messaging:
{competitor}

Generate 3 short ad copy options (1–2 lines each).
Focus on clarity and differentiation.
"""

    return llm(prompt)

if st.button("Generate Copy"):
    if not brand_tone or not product_details:
        st.warning("Brand tone and product details are required.")
    else:
        with st.spinner("Generating ad copy..."):
            output = generate_ad_copy(
                brand_tone,
                product_details,
                competitor_context
            )

        st.subheader("Generated Ad Copy")
        st.write(output)
