###########----Necessary-Imports################################3

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, END
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from customtkinter import (
    CTkButton,
    CTkEntry,
)
import time



# theme name
# - cosmo
# cyborg darkly flatly journal litera lumen lux materia minty pulse sandstone simplex slate solar spacelab superhero united yet

#########FONT##########################

FONT = ("consolas", 16)
FONT1 = ("consolas", 10)
FONT2 = ("consolas", 12)

##############FUNCTIONS########################################


###########Animation of meter widget#######################################-start


def animate_meter_loading(meter, start_value, end_value, step=5, delay=0.001):

    # Direction value
    direction = 1 if end_value > start_value else -1

    for value in range(start_value, end_value + direction, step * direction):
        meter.configure(subtext="Calculating!...")
        meter.configure(amountused=value)
        meter.update()
        time.sleep(delay)

    if end_value == 100:
        # creating animation recursion usage
        # animate_meter_loading(meter, 100, 0, step, delay)
        animate_meter_loading(meter, 100, 1, step, delay)
        animate_meter_loading(meter, -50, 50, step, delay)
        animate_meter_loading(meter, -0, 50, step, delay)
        animate_meter_loading(meter, 50, 101, step, delay)
        animate_meter_loading(meter, 100, 0, step, delay)
    elif end_value == 0:
        # Placeholder for displaying the result on the meter
        display_final_value(meter)


def display_final_value(
    meter,
):
    # setting default values

    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    gender_combobox.set("Male")
    race_combobox.set("Asian")
    gender_combobox0.set("Never")
    gender_combobox20.set("Single")
    gender_combobox1011.set("7-")
    gender_combobox89.set("Normal")

    final_value = result
    meter.configure(amountused=final_value)
    meter.configure(subtext="Expected-Age")
    meter.update()
   


###########Animation of meter widget#######################################-end


def save_data_and_generate_report(name, data,deductions,life_expectancy):
    filename = f"{name}_report.txt"
    suggestions = {
        5: "Improving your BMI by maintaining a healthy weight can add years to your life.",
        3: "Reducing stress and improving your diet can significantly impact your health positively.",
        4: "Regular exercise and managing blood pressure are crucial for a longer life."
    }
    with open(filename, 'w') as file:
        file.write(f"Life Expectancy Report for {name}\n")
        file.write("-" * 50 + "\n")
       
        
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write(f"\nEstimated Life Expectancy: {life_expectancy} years\n")
        file.write("Deductions Summary:\n")
        for reason, deduction in deductions.items():
            if deduction:
                file.write(f"{reason}: -{deduction} years\n")
        file.write("\nSuggestions for Improving Life Expectancy:\n")
        for deduction, suggestion in suggestions.items():
            if deduction in deductions.values():
                file.write(f"- {suggestion}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Disclamar This program should taken as a fun learning project and cant tell about expected life of anyone.Death Time is Fixed!\n")
        file.write("-" * 50 + "\n")
        file.write("------------End of report!-------------------")
    messagebox.showinfo("Report Saved", f"Your report has been saved as {filename}")
###########Main-Function####################################################-start


def calculate_and_save(*args):
    name = simpledialog.askstring("Terms", "Enter your name")
    if not name:
        messagebox.showwarning("Terms and conditions", "Enter your name to continue")
        return
        
    calculate_deductions(name)
    


def calculate_deductions(name):
    global result
    try:
        # age = meter.amountusedvar.get()
        gender = gender_var.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        # bmi = ((weight / 0.453592)) / ((height * 12) ** 2) * 703
        # meter.configure(amountused=50)
        race = race_var.get()
        smoker = smoker_var.get()
        exercise_level = exercise_var.get()
        diet_Digestion = diet_var.get()
        love_and_marriage = love_marriage_var.get()
        stress_mode_level = stress_var.get()
        sleep_hours = sleep_hours_var.get()
        blood_pressure_level = blood_pressure_var.get()
        major_Disease = major_Disease_var.get()
        Air_quality = Mostly_AQI_Index_var.get()
        Longevity_ancestors_age = Longevity_ancestors_var.get()
        Living_Conditions = Living_Conditions_var.get()
        Average_Temperature = Living_Conditions_var.get()
        Country_Status = Country_Status_var.get()

        deductions = {}
        life_expectancy = 76 if gender == "Male" else 81

        # BMI Calculation
        bmi = ((weight / 0.453592)) / ((height * 12) ** 2) * 703
        if bmi < 18.5 or bmi > 30:
            deductions["bmi"] = 3
        elif 25 < bmi <= 30:
            deductions["bmi"] = 2
        elif 25 < bmi <= 30:
            deductions["bmi"] = 2
        else:
            deductions["bmi"] = 0

        # Race
        if race == "Black":
            deductions["Race"] = 0
        elif race == "White":
            deductions["Race"] = 1
        elif race == "Asian":
            deductions["Race"] = 3
        elif race == "Others":
            deductions["Race"] = 2

        # Smoking adjustment
        if smoker == "Yes":
            deductions["Smoke"] = 5
        elif smoker == "Never":
            deductions["Smoke"] = 0
        elif smoker == "Not-Regular":
            deductions["Smoke"] = 3

        # Exercise adjustment
        if exercise_level == "No-Routine":
            deductions["Exercise"] = 4
        elif exercise_level == "Sometimes a week":
            deductions["Exercise"] = 2
        elif exercise_level == "Moderate":
            deductions["Exercise"] = 1
        elif exercise_level == "Very-Active":
            deductions["Exercise"] = 0

        # Diet adjustment
        if diet_Digestion == "Poor":
            deductions["diet_Digestion"] = 5
        elif diet_Digestion == "Normal":
            deductions["diet_Digestion"] = 2
        elif diet_Digestion == "Good":
            deductions["diet_Digestion"] = 1
        elif diet_Digestion == "Best":
            deductions["diet_Digestion"] = 0

        # marriage
        if love_and_marriage == "None":
            deductions["love_and_marriage"] = 5
        elif love_and_marriage == "Looking-for-partner":
            deductions["love_and_marriage"] = 1
        elif love_and_marriage == "Married":
            deductions["love_and_marriage"] = 0
        elif love_and_marriage == "Single":
            deductions["love_and_marriage"] = 2

        # Stress level adjustment
        if stress_mode_level == "Always-Cool&Happy":
            deductions["stress_mode_lvl"] = 0
        elif stress_mode_level == "Never-take-Stress&Lightmode":
            deductions["stress_mode_lvl"] = 1
        elif stress_mode_level == "High-Stress&high-temper":
            deductions["stress_mode_lvl"] = 4
        elif stress_mode_level == "Normal":
            deductions["stress_mode_lvl"] = 2

        # Blood Pressure
        if blood_pressure_level == "Normal":
            deductions["blood_pressure_level"] = 0
        elif blood_pressure_level == "Low":
            deductions["blood_pressure_level"] = 2
        elif blood_pressure_level == "High":
            deductions["blood_pressure_level"] = 4
        elif blood_pressure_level == "Always-Different":
            deductions["blood_pressure_level"] = 1

        # Sleep quality adjustment
        if sleep_hours == "10+":
            deductions["sleep_hours"] = 0
        elif sleep_hours == "7+":
            deductions["sleep_hours"] = 1
        elif sleep_hours == "7-":
            deductions["sleep_hours"] = 2
        elif sleep_hours == "No-Fixed-time":
            deductions["sleep_hours"] = 3

        # Major Disease
        if major_Disease == "Heart-Issue":
            deductions["major_Disease"] = 5
        elif major_Disease == "Kidneys-Issue":
            deductions["major_Disease"] = 3
        elif major_Disease == "Brain-Issue":
            deductions["major_Disease"] = 2
        elif major_Disease == "None":
            deductions["major_Disease"] = 0

        # Air quality
        if Air_quality == "High":
            deductions["Air_quality"] = 5
        elif Air_quality == "Normal":
            deductions["Air_quality"] = 1
        elif Air_quality == "Low":
            deductions["Air_quality"] = 2
        elif Air_quality == "Better":
            deductions["Air_quality"] = 0

        # Longetivity ancestrors
        if Longevity_ancestors_age == "Grandparents->any 90+":
            deductions["Longevity_ancestors_age"] = 0
        elif Longevity_ancestors_age == "Grandparents->any 80+":
            deductions["Longevity_ancestors_age"] = 1
        elif Longevity_ancestors_age == "Grandparents->any 60+":
            deductions["Longevity_ancestors_age"] = 3
        elif Longevity_ancestors_age == "Grandparents->any>55":
            deductions["Longevity_ancestors_age"] = 5

        # Living condition
        if Living_Conditions == "Urban":
            deductions["Living_Conditions"] = 3
        elif Living_Conditions == "Rural":
            deductions["Living_Conditions"] = 0
        elif Living_Conditions == "Mixed":
            deductions["Living_Conditions"] = 2
        elif Living_Conditions == "None":
            deductions["Living_Conditions"] = 1

        # # Temperature

        # if Average_Temperature == '30':
        #      deductions["Average_Temperature"]  =2
        # elif Average_Temperature == '20':
        #      deductions["Average_Temperature"]  = 1
        # elif Average_Temperature == '10':
        #      deductions["Average_Temperature"]  =0
        # elif Average_Temperature == '<1':
        #      deductions["Average_Temperature"]  =3

        # Country status

        if Country_Status == "Developed!":
            deductions["Country_Status"] = 0
        elif Country_Status == "Under-Developed":
            deductions["Country_Status"] = 2
        elif Country_Status == "Poor":
            deductions["Country_Status"] = 3
        elif Country_Status == "Island":
            deductions["Country_Status"] = 4

        total_deductions = sum(deductions.values())
        print(total_deductions)
        life_expectancy -= total_deductions
        result = life_expectancy
        print(deductions)

        print(life_expectancy)
        root.after(100, animate_meter_loading, meter, 0, 100, 10, 0.0001)
        if messagebox.askyesno("Save Data", "Do you want to save this data?"):
            save_data_and_generate_report(name, locals(),deductions, life_expectancy)

        # meter.configure(amountused=life_expectancy)
        # meter.configure(subtext="Expected-Age")
        result_var.set(f"Estimated life expectancy: {life_expectancy} years.")
        
        

    except ValueError:
        messagebox.showerror(
            "Input Error", "Please ensure all inputs are correctly filled."
        )


###########Main-Function####################################################-end


#############UI-Design ########################################################


# flatly white

# root = tb.Window(themename="darkly")

#############---Window-Settings---#########################################################
# cerculean
root = tb.Window(themename="cerculean")
root.title("Life Expectancy Calculator")
root.geometry("780x775+100+100")
root.maxsize(790, 790)
root.minsize(780, 780)


################Variables#########################################################-start

gender_var = tk.StringVar(value="Male")
smoker_var = tk.StringVar(value="No")
exercise_var = tk.StringVar(value="Yes")
diet_var = tk.StringVar(value="Healthy")
alcohol_var = tk.StringVar(value="No")
stress_var = tk.StringVar(value="Low")
love_marriage_var = tk.StringVar(value="Single")
blood_pressure_var = tk.StringVar(value="Normal")
physical_activity_var = tk.StringVar(value="Sedentary")
digestive_health_var = tk.StringVar(value="Good")
sleep_hours_var = tk.StringVar(value="7-")
race_var = tk.StringVar(value="Asian")
major_Disease_var = tk.StringVar(value="None")
Mostly_AQI_Index_var = tk.StringVar(value="Better")
Longevity_ancestors_var = tk.StringVar(value="")
Living_Conditions_var = tk.StringVar(value="Island")
Average_Temperature_var = tk.StringVar(value="20+")
Country_Status_var = tk.StringVar(value="Developed")
result_var = tk.StringVar()
# result label

################---Variables---#########################################################-end

###########---Other-widgets---######################################################
top = tk.Label(
    text="Results",
    font=("consolas", 12),
    fg="pink",
)
res_info_frame = ttk.LabelFrame(root, padding=(20, 10), labelwidget=top)
res_info_frame.grid(row=0, column=0, padx=10, pady=2, sticky="ew", columnspan=2)
# res_info_frame.place(x=0,y=0)
meter = tb.Meter(
    res_info_frame,
    subtextstyle=(SUCCESS),
    metertype=FULL,
    bootstyle=(SUCCESS),
    amountused=0,
    interactive=False,
    subtext="Calculate-e-Age!",
    subtextfont=FONT2,
    metersize=180,
    amounttotal=120,
)
# meter.place(x=50,y=0)
meter.grid(row=0, column=1, padx=100, ipadx=10, pady=2)
# LabelFrames
top1 = tk.Label(text="Basic Information", font=("consolas", 14))

basic_info_frame = ttk.LabelFrame(
    root, text="Basic Information", labelwidget=top1, padding=(20, 10)
)
basic_info_frame.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

top2 = tk.Label(text="Lifestyle Choices", font=("consolas", 14))

lifestyle_choices_frame = ttk.LabelFrame(
    root, text="Lifestyle Choices", labelwidget=top2, padding=(20, 10)
)
lifestyle_choices_frame.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

top3 = tk.Label(text="Health Factors", font=("consolas", 14))

health_factors_frame = ttk.LabelFrame(
    root, text="Health Factors", labelwidget=top3, padding=(20, 10)
)
health_factors_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

top4 = tk.Label(text="Environmental Factors", font=("consolas", 14))

environmental_factors_frame = ttk.LabelFrame(
    root, text="Environmental Factors", labelwidget=top4, padding=(20, 10)
)
environmental_factors_frame.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Basic Information Widgets
gender_label = ttk.Label(basic_info_frame, text="Gender", font=FONT1)
gender_label.grid(row=0, column=0, sticky="w")
gender_combobox = ttk.Combobox(
    basic_info_frame,
    values=["Male", "Female"],
    textvariable=gender_var,
    state="readonly",
    font=FONT1,
)
gender_combobox.grid(row=0, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox.set("Male")  # Default value

age_label = ttk.Label(basic_info_frame, text="Race", font=FONT1)
age_label.grid(row=1, column=0, sticky="w")
race_combobox = ttk.Combobox(
    basic_info_frame,
    values=["Black", "Asian", "White", "Others"],
    textvariable=race_var,
    state="readonly",
    font=FONT1,
)
race_combobox.grid(row=1, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
race_combobox.set("Asian")  # Default value

age_label1 = ttk.Label(basic_info_frame, text="Height(feet)", font=FONT1)

age_label1.grid(row=3, column=0, sticky="w")

height_entry = CTkEntry(
    basic_info_frame,
    font=FONT2,
    placeholder_text="Height(feet)",
    placeholder_text_color="gray10",
    fg_color="lightblue"
)
height_entry.grid(row=3, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)

age_label2 = ttk.Label(basic_info_frame, text="Weight(kg)", font=FONT1)

age_label2.grid(row=4, column=0, sticky="w")

weight_entry = CTkEntry(
    basic_info_frame,
    font=FONT2,
    placeholder_text="Weight(kg)",
    placeholder_text_color="gray10",
    fg_color="lightblue"
)
weight_entry.grid(row=4, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)


# Lifestyle Choices Widgets

gender_label = ttk.Label(lifestyle_choices_frame, text="Smoking", font=FONT1)
gender_label.grid(row=0, column=0, sticky="w")
gender_combobox0 = ttk.Combobox(
    lifestyle_choices_frame,
    values=["Yes", "Never", "Not-Regular"],
    textvariable=smoker_var,
    state="readonly",
    font=FONT1,
)
gender_combobox0.grid(row=0, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox0.set("Never")

age_label = ttk.Label(lifestyle_choices_frame, text="Exercies", font=FONT1)
age_label.grid(row=1, column=0, sticky="w")
gender_combobox11 = ttk.Combobox(
    lifestyle_choices_frame,
    font=FONT1,
    textvariable=exercise_var,
    values=["Very-Active", "Moderate", "Sometimes a week", "No-Routine"],
    state="readonly",
)
gender_combobox11.grid(row=1, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox11.set("Moderate")  # Default value

age_label1 = ttk.Label(lifestyle_choices_frame, text="Diet-Digestion", font=FONT1)
age_label1.grid(row=3, column=0, sticky="w")
gender_combobox10 = ttk.Combobox(
    lifestyle_choices_frame,
    values=["Best", "Good", "Normal", "Poor"],
    textvariable=diet_var,
    state="readonly",
    font=FONT1,
)
gender_combobox10.grid(row=3, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox10.set("Normal")  # Default value

age_label2 = ttk.Label(lifestyle_choices_frame, text="Love-Marriage", font=FONT1)
age_label2.grid(row=4, column=0, sticky="w")
gender_combobox20 = ttk.Combobox(
    lifestyle_choices_frame,
    values=["Single", "Married", "Looking-for-partner", "None"],
    textvariable=love_marriage_var,
    state="readonly",
    font=FONT1,
)
gender_combobox20.grid(row=4, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox20.set("Single")

# Health Factors Widgets

gender_label = ttk.Label(health_factors_frame, text="Stress-Mode", font=FONT1)
gender_label.grid(row=0, column=0, sticky="w")
gender_combobox89 = ttk.Combobox(
    health_factors_frame,
    textvariable=stress_var,
    values=[
        "Always-Cool&Happy",
        "Never-take-Stress&Lightmode",
        "High-Stress&high-temper",
        "Normal",
    ],
    state="readonly",
    font=FONT1,
)
gender_combobox89.grid(row=0, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox89.set("Normal")

age_label = ttk.Label(health_factors_frame, text="Blood-Pressure", font=FONT1)
age_label.grid(row=1, column=0, sticky="w")
gender_combobox3 = ttk.Combobox(
    health_factors_frame,
    values=["Normal", "High", "Low", "Always-Different"],
    textvariable=blood_pressure_var,
    state="readonly",
    font=FONT1,
)
gender_combobox3.grid(row=1, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox3.set("Normal")  # Default value

age_label1 = ttk.Label(health_factors_frame, text="Sleep-Hours", font=FONT1)
age_label1.grid(row=3, column=0, sticky="w")
gender_combobox1011 = ttk.Combobox(
    health_factors_frame,
    values=["10+", "7+", "7-", "No-Fixed-time"],
    textvariable=sleep_hours_var,
    state="readonly",
    font=FONT1,
)
gender_combobox1011.grid(row=3, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox1011.set("7-")

age_label2 = ttk.Label(health_factors_frame, text="Major-Disease", font=FONT1)
age_label2.grid(row=4, column=0, sticky="w")
gender_combobox2 = ttk.Combobox(
    health_factors_frame,
    values=["Heart-Issue", "Kidneys-Issue", "Brain-Issue", "None"],
    textvariable=major_Disease_var,
    state="readonly",
    font=FONT1,
)
gender_combobox2.grid(row=4, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox2.set("None")  # Default value
# Environmental Factors Widgets
race_label = ttk.Label(environmental_factors_frame, text="Mostly-AQI-Index", font=FONT1)
race_label.grid(row=0, column=0, sticky="w")
gender_combobox21 = ttk.Combobox(
    environmental_factors_frame,
    values=["High", "Normal", "Low", "Better"],
    textvariable=Mostly_AQI_Index_var,
    state="readonly",
    font=FONT1,
)
gender_combobox21.grid(row=0, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox21.set("Normal")  # Default value

longevity_label = ttk.Label(
    environmental_factors_frame, text="Longevity (ancestors' age):", font=FONT1
)
longevity_label.grid(row=1, column=0, sticky="w")
gender_combobox3 = ttk.Combobox(
    environmental_factors_frame,
    textvariable=Longevity_ancestors_var,
    values=[
        "Grandparents->any 90+ ",
        "Grandparents->any 80+",
        "Grandparents->any 60+",
        "Grandparents->any>55",
    ],
    state="readonly",
    font=FONT1,
)
gender_combobox3.grid(row=1, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2)
gender_combobox3.set("Grandparents->any 80+")  # Default value

living_conditions_label = ttk.Label(
    environmental_factors_frame, text="Living-Conditions:", font=FONT1
)
living_conditions_label.grid(row=3, column=0, sticky="w")
living_conditions_combobox111 = ttk.Combobox(
    environmental_factors_frame,
    textvariable=Living_Conditions_var,
    values=["Urban", "Rural", "Mixed", "None"],
    state="readonly",
    font=FONT1,
)
living_conditions_combobox111.grid(
    row=3, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2
)
living_conditions_combobox111.set("Urban")  # Default value

# living_conditions_label00 = ttk.Label(environmental_factors_frame, text="Average-Temperature(Celcius)",font=FONT1)
# living_conditions_label00.grid(row=4, column=0, sticky="w")
# living_conditions_combobox00 = ttk.Combobox(environmental_factors_frame,textvariable=Average_Temperature_var, values=["30+", "20+","10+","<1"], state="readonly",font=FONT1)
# living_conditions_combobox00.grid(row=4, column=1, sticky="ew",padx=5,ipadx=2,pady=5,ipady=2)
# living_conditions_combobox00.set("20+")  # Default value

living_conditions_label99 = ttk.Label(
    environmental_factors_frame, text="Country-Status", font=FONT1
)
living_conditions_label99.grid(row=4, column=0, sticky="w")
living_conditions_combobox101 = ttk.Combobox(
    environmental_factors_frame,
    font=FONT1,
    textvariable=Country_Status_var,
    values=["Developed!", "Under-Developed", "Poor", "Island"],
    state="readonly",
)
living_conditions_combobox101.grid(
    row=4, column=1, sticky="ew", padx=5, ipadx=2, pady=5, ipady=2
)
living_conditions_combobox101.set("Developed!")  # Default value


# Calculate button
# btn_img=CTkImage(Image.open("1.jpg"),
#    size=(80,60))
def on_enter(e):
    calculate_btn.configure(fg_color="#81b214", border_color="#3ddc97", border_width=4)


def on_leave(e):
    calculate_btn.configure(fg_color="206a5d", border_color="206a5d", border_width=0)


calculate_btn = CTkButton(
    res_info_frame,
    text_color="#3ddc97",
    bg_color="#bfdcae",
    border_spacing=3,
    corner_radius=5,
    fg_color="#206a5d",
    cursor="hand2",
    text="Calculate Expectancy",
    font=FONT,
    command=calculate_and_save,
    hover_color="#81b214",
    border_color="#3ddc97",
)
# calculate_btn = CTkSegmentedButton(res_info_frame,text_color="#3ddc97",bg_color="#bfdcae",corner_radius=5,fg_color="#206a5d", values={"Calculate_Expectancy"},font=FONT, command=calculate_and_save)
calculate_btn.grid(row=0, column=2, padx=10)
# switch_1 =CTkSwitch(res_info_frame, text="darkmode", command=lambda:tb.Window(themename="minty" if switch_1.get() == 1 else "darkly"))
# switch_1.grid()

#########---Key-Bindings###############################


calculate_btn.bind("<Return>", calculate_and_save)
root.bind("<Return>", calculate_and_save)

###########---Main---Loop#######################################
root.mainloop()


##########----Disclamar############################################

###This app is just made an intention of a fun project its cannot predect final age in any way 
### This is a basic implementation feel free to expand!!!
