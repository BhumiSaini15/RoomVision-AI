import streamlit as st
import google.generativeai as genai
from PIL import Image


# ---------------------------------------
# Load Environment Variables
# ---------------------------------------


GOOGLE_API_KEY = "Your_Key"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")


# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="RoomVision AI: A Multimodal Generative AI-Based Interior Design Assistant",
    page_icon="",
    layout="wide"
)


# ---------------------------------------
# Initialize Session State
# ---------------------------------------
if "classification_result" not in st.session_state:
    st.session_state.classification_result = None

if "room_image" not in st.session_state:
    st.session_state.room_image = None

if "question_answer" not in st.session_state:
    st.session_state.question_answer = None


# ---------------------------------------
# Title
# ---------------------------------------
st.title("RoomVision AI: A Multimodal Generative AI-Based Interior Design Assistant")

st.write(
    "Upload a room image and get room classification "
    "using Gemini 3.6 Flash."
)


# ---------------------------------------
# Image Upload
# ---------------------------------------
uploaded_file = st.file_uploader(
    "Upload a room Image",
    type=["jpg", "jpeg", "png"]
)


# ---------------------------------------
# Process Uploaded Image
# ---------------------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    # Store image in session state
    st.session_state.room_image = image.copy()

    # Display image and button
    col1, col2 = st.columns([1.5, 1])

    with col1:

        display_image = image.copy()
        display_image.thumbnail((300, 300))

        st.image(
            display_image,
            caption="Uploaded Room Image",
            use_container_width=True
        )

    with col2:

        st.subheader("🔍 Classification")

        classify_button = st.button(
            "Classify Room",
            use_container_width=True
        )

        if classify_button:

            with st.spinner("Analyzing image..."):

                prompt = """
                You are an AI Interior Design Assistant specialising in analysing room photographs and generating practical, affordable interior-design recommendations.

                Carefully analyse the uploaded room image.

                IMPORTANT INSTRUCTIONS:
                - Base your analysis primarily on what is visibly present in the image.
                - Clearly distinguish observations from recommendations.
                - Do not assume exact room dimensions unless a reliable reference is visible.
                - Do not claim to know information that cannot be determined from the image.
                - If something is unclear, explicitly state that it cannot be determined reliably.
                - Recommendations should be practical and suitable for an average home.
                - Prioritise improvements that can realistically be implemented without major structural renovation.

                Perform the following analysis:

                1. ROOM IDENTIFICATION
                Identify the apparent type of room, such as:
                - Bedroom
                - Living room
                - Study room
                - Dining room
                - Kitchen
                - Home office
                - Other

                Explain the visual evidence supporting your identification.

                2. EXISTING FURNITURE
                Identify clearly visible furniture and estimate its general placement.

                Examples:
                - Bed
                - Sofa
                - Chair
                - Desk
                - Table
                - Wardrobe
                - Cabinet
                - Bookshelf
                - TV unit
                - Coffee table

                Do not invent furniture that is not visible.

                3. COLOUR ANALYSIS
                Identify:
                - Dominant wall colours
                - Furniture colours
                - Floor colours
                - Curtain colours
                - Accent colours
                - Overall colour scheme

                Explain whether the visible colours appear visually coordinated.

                4. LIGHTING ANALYSIS
                Analyse:
                - Natural light
                - Windows
                - Artificial lighting
                - Brightness
                - Dark areas
                - Potential lighting improvements

                Do not estimate exact brightness measurements.

                5. LAYOUT ANALYSIS
                Analyse:
                - Furniture positioning
                - Available walking space
                - Open areas
                - Potentially crowded areas
                - Balance of furniture
                - Practicality of the current arrangement

                Do not claim exact measurements.

                6. DECORATIVE ELEMENTS
                Identify visible:
                - Plants
                - Paintings
                - Wall art
                - Mirrors
                - Rugs
                - Curtains
                - Cushions
                - Decorative objects
                - Books
                - Other visible décor

                Explain how these elements contribute to the overall appearance.

                7. DESIGN STYLE
                Identify the apparent interior style if reasonably identifiable, such as:
                - Minimalist
                - Modern
                - Traditional
                - Contemporary
                - Scandinavian-inspired
                - Industrial
                - Rustic
                - Eclectic

                If the style cannot be confidently identified, say so.

                8. DESIGN STRENGTHS
                Identify aspects that already work well.

                Consider:
                - Colour coordination
                - Furniture arrangement
                - Lighting
                - Décor
                - Space utilisation
                - Visual balance

                9. AREAS FOR IMPROVEMENT
                Identify practical improvements.

                Prioritise changes according to:
                - High impact
                - Medium impact
                - Optional improvements

                10. FURNITURE ARRANGEMENT
                Suggest a better arrangement of the existing furniture where appropriate.

                Explain:
                - Which items could be moved
                - Where they could potentially be positioned
                - Why the change could improve functionality or appearance

                Do not assume that furniture can be moved if the image suggests it is fixed.

                11. COLOUR RECOMMENDATIONS
                Suggest:
                - Wall colour options
                - Accent colours
                - Curtain colours
                - Cushion colours
                - Rug colours
                - Decorative colour combinations

                Provide combinations that complement the existing room rather than completely redesigning it unless necessary.

                12. LIGHTING RECOMMENDATIONS
                Suggest practical lighting improvements such as:
                - Ceiling lighting
                - Floor lamps
                - Table lamps
                - Wall lighting
                - Task lighting
                - Warmer or cooler lighting where appropriate

                13. SPACE UTILISATION
                Suggest ways to make better use of visible space.

                Examples:
                - Vertical storage
                - Multi-purpose furniture
                - Decluttering
                - Better furniture positioning
                - Wall-mounted storage

                14. DECORATION IDEAS
                Suggest practical decorative additions such as:
                - Plants
                - Artwork
                - Mirrors
                - Rugs
                - Curtains
                - Cushions
                - Shelving

                Do not recommend excessive decoration if the room already appears visually crowded.

                15. BUDGET-FRIENDLY IMPROVEMENTS
                Provide affordable ideas that can create noticeable improvements without replacing all existing furniture.

                Divide them into:

                Low-cost:
                - Small décor changes
                - Cushion covers
                - Plants
                - Organisation
                - Lighting changes

                Medium-cost:
                - Curtains
                - Rugs
                - Paint
                - Storage improvements

                Higher-cost:
                - Furniture replacement
                - Major lighting changes
                - Renovation

                16. PRIORITY ACTION PLAN
                Create a final list of the five most useful improvements.

                Rank them by priority based on:
                - Practicality
                - Expected visual impact
                - Space utilisation
                - Affordability

                Do not provide a numerical design score.

                OUTPUT FORMAT:

                # 🏠 Interior Design Analysis

                ## 1. Room Identification
                **Room Type:**  
                **Confidence:**  
                **Reason:**  

                ## 2. 🛋️ Existing Furniture
                | Furniture | Visible Location | Observation |
                |---|---|---|
                | | | |

                ## 3. 🎨 Colour Analysis
                | Element | Observed Colour |
                |---|---|
                | Walls | |
                | Floor | |
                | Furniture | |
                | Curtains | |
                | Accent Colours | |

                **Overall Colour Scheme:**  

                ## 4. 💡 Lighting Analysis
                **Natural Lighting:**  
                **Artificial Lighting:**  
                **Potential Improvements:**  

                ## 5. 📐 Layout Analysis
                ### What works
                - 

                ### Potential issues
                - 

                ## 6. 🪴 Decorative Elements
                - 

                ## 7. 🎨 Apparent Design Style
                **Style:**  
                **Reason:**  

                ## 8. ✅ Design Strengths
                - 
                - 
                - 

                ## 9. 🔧 Areas for Improvement
                ### High Impact
                - 

                ### Medium Impact
                - 

                ### Optional
                - 

                ## 10. 🛋️ Furniture Arrangement Suggestions
                1. 
                2. 
                3. 

                ## 11. 🎨 Recommended Colour Combinations
                | Area | Suggested Colour |
                |---|---|
                | Walls | |
                | Accent | |
                | Curtains | |
                | Rug | |
                | Cushions/Décor | |

                ## 12. 💡 Lighting Suggestions
                - 
                - 
                - 

                ## 13. 📦 Space Utilisation
                - 
                - 
                - 

                ## 14. 🪴 Decoration Ideas
                - 
                - 
                - 

                ## 15. 💰 Budget-Friendly Improvements

                ### Low Cost
                - 

                ### Medium Cost
                - 

                ### Higher Cost
                - 

                ## 16. 📋 Top 5 Priority Improvements
                1. 
                2. 
                3. 
                4. 
                5. 

                ## ⚠️ Important Limitations
                Explain briefly which recommendations are based on visual inference and what cannot be reliably determined from the image.
                """

                response = model.generate_content(
                    [prompt, st.session_state.room_image]
                )

                # Save result in session state
                st.session_state.classification_result = response.text

                # Clear previous question answer
                st.session_state.question_answer = None


# ---------------------------------------
# Display Classification Result
# ---------------------------------------
if st.session_state.classification_result:

    st.divider()

    st.subheader("📊 Analysis Result")

    st.markdown(
        st.session_state.classification_result
    )


# ---------------------------------------
# Follow-up Question Section
# ---------------------------------------
if st.session_state.room_image is not None:

    st.divider()

    st.subheader("💬 Ask About This Image")

    st.write(
        "Not satisfied with the classification? "
        "Ask one question about the uploaded room image."
    )

    # Form prevents execution while typing
    with st.form("question_form"):

        user_question = st.text_input(
            "Your Question",
            placeholder="Example: Is this a good room?"
        )

        ask_button = st.form_submit_button(
            "🤖 Ask Gemini",
            use_container_width=True
        )

    # ---------------------------------------
    # Process Follow-up Question
    # ---------------------------------------
    if ask_button:

        if user_question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is thinking..."):

                question_prompt = f"""
                You are an AI Room Image Assistant.

                Look carefully at the uploaded room image.

                Answer the user's question based on what is
                visibly present in the image.

                User Question:
                {user_question}

                Give a clear, simple and useful answer.

                If the question asks whether the room is
                good or bad, explain whether it appears to be
                generally cleaner from a
                general room-quality.

                Do not invent information that cannot be
                determined from the image.

                Clearly mention uncertainty when appropriate.
                """

                question_response = model.generate_content(
                    [
                        question_prompt,
                        st.session_state.room_image
                    ]
                )

                # Store answer
                st.session_state.question_answer = (
                    question_response.text
                )


# ---------------------------------------
# Display Gemini Answer
# ---------------------------------------
if st.session_state.question_answer:

    st.subheader("🤖 Gemini's Answer")

    st.markdown(
        st.session_state.question_answer
    )