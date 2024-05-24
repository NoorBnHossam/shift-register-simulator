import streamlit as st
import time

st.set_page_config(
   page_title=" Computer Architecture",
)


def right_shift_register(initial_value, input_value, num_shifts, animation_placeholder, show_history):
    steps = []
    register = initial_value
    steps.append(register)
    for _ in range(num_shifts):
        register = input_value + register[:-1]
        steps.append(register)
        animation_placeholder.write(f" {input_value} ➡️  "+ register)
        time.sleep(0.9)  
    if show_history:
        st.write("History of shifts:")
        st.write(steps)
    st.markdown(f"Done 🥳 & the final output is ✨ {register} ✨")
    reset()
    
    return steps

def left_shift_register(initial_value, input_value, num_shifts, animation_placeholder, show_history):
    steps = []
    register = initial_value
    steps.append(register)
    for _ in range(num_shifts):
        register = register[1:] + input_value
        steps.append(register)
        animation_placeholder.write(register + f" ⬅️ {input_value}")
        time.sleep(0.9) 
    if show_history:
        st.write("History of shifts:")
        st.write(steps)
    st.markdown(f"Done 🥳 & the final output is ✨ {register} ✨")
    reset()
    
    return steps

def right_circular_shift(initial_value, num_shifts, animation_placeholder, show_history):
    steps = []
    register = initial_value
    steps.append(register)
    for _ in range(num_shifts):
        last_bit = register[-1]
        register = last_bit + register[:-1]
        steps.append(register)
        animation_placeholder.write(f"🔁 {register} 🔁")
        time.sleep(0.9)  
    if show_history:
        st.write("History of shifts:")
        st.write(steps)
    st.markdown(f"Done 🥳 & the final output is ✨ {register} ✨")
    reset()

def left_circular_shift(initial_value, num_shifts, animation_placeholder, show_history):
    steps = []
    register = initial_value
    steps.append(register)
    for _ in range(num_shifts):
        first_bit = register[0]
        register = register[1:] + first_bit
        steps.append(register)
        animation_placeholder.write(f"🔁 {register} 🔁")
        time.sleep(0.9)  
    if show_history:
        st.write("History of shifts:")
        st.write(steps)
    st.markdown(f"Done 🥳 & the final output is ✨ {register} ✨")

    reset()

def reset():
    
    if st.button("Reset 🗑️"):
        st.experimental_rerun()
        
        



def main():
    st.title("Shift Register 🤹")
       
    
    tab1,tab2,tab3 = st.tabs(["Right Shift" , "Left Shift "," Shift circulate" ])

    with tab1:
        st.header("Right Shift ➡️")
        initial_value = st.text_input("Enter the initial value of the register (binary):", key="right_initial")
        input_value = st.radio("Enter the input value (0 or 1) to shift the register:", ('0', '1'), key="right_input")
        num_shifts = st.slider("Enter the number of shifts:", min_value=1, max_value=10, value=5, key="right_shifts")
        show_history = st.checkbox("Show History", key="right_history")
        calc_button = st.button("Calculate 🧮", key="right_calculate")
        animation_placeholder1 = st.empty()

        if calc_button:
            if not all(bit in ['0', '1'] for bit in initial_value.strip()):
                st.error("Please enter a valid initial value (binary sequence of 0s and 1s) for the register.")
            else:
                right_shift_register(initial_value, input_value, num_shifts, animation_placeholder1, show_history)



    with tab2:
        st.header("Left Shift ⬅️")
        initial_value = st.text_input("Enter the initial value of the register (binary):", key="left_initial")
        input_value = st.radio("Enter the input value (0 or 1) to shift the register:", ('0', '1'), key="left_input")
        num_shifts = st.slider("Enter the number of shifts:", min_value=1, max_value=10, value=5, key="left_shifts")
        show_history = st.checkbox("Show History", key="left_history")
        calc_button = st.button("Calculate 🧮", key="left_calculate")
        animation_placeholder2 = st.empty()

        if calc_button:
            if not all(bit in ['0', '1'] for bit in initial_value.strip()):
                st.error("Please enter a valid initial value (binary sequence of 0s and 1s) for the register.")
            else:
                left_shift_register(initial_value, input_value, num_shifts, animation_placeholder2, show_history)


    with tab3:

        st.header("Shift circulate 🔁")

        initial_value = st.text_input("Enter initial value of the register (binary):")
        display_option = st.selectbox("Choose Type", ["Right", "Left"])
        num_shifts = st.number_input("Enter number of shifts:", min_value=1, step=1)
        show_history = st.checkbox("Show History")
        animation_placeholder = st.empty()


        if st.button("Shift"):
            if not all(bit in ['0', '1'] for bit in initial_value.strip()):
                st.error("Please enter a valid initial value (binary sequence of 0s and 1s) for the register.")

            else:
                animation_placeholder.text("")
                if display_option == "Right":
                    right_circular_shift(initial_value, num_shifts, animation_placeholder, show_history)
                else:
                    left_circular_shift(initial_value, num_shifts, animation_placeholder, show_history)



            
if __name__ == "__main__":
    main()
