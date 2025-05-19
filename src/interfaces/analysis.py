import streamlit as st

def analysis():
    st.title("Analysis")
    st.write("This is the analysis page.")

    code_col, desc_col = st.columns([3,2])

    with code_col:

        st.code(
            body=
                """
                for i in range(intSize): 

                    # Inner loop to compare adjacent elements
                    for j in range(0, intSize - i - 1):

                        # Compare if adjacent elements are in the correct order
                        if listInput[j] > listInput[j+1]:

                            # Swap if they are not in the correct order 
                            listInput[j], listInput[j+1] = listInput[j+1], listInput[j]

                """,
            language="python", 
            line_numbers=True,)
    
    with desc_col:
        st.markdown("Sobrang cute na **description**")


    

