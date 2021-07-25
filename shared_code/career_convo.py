
def render(plt):
    plt.xkcd()
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    fig1,  (career_pie, life_pie) = plt.subplots(1, 2)

    # Make the figure bigger to space stuff around
    height_in_inches = 4
    fig1.set_size_inches(3 * height_in_inches, height_in_inches)

    career_pie.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.

    labels = ["Job Title", "Compensation"]
    sizes = [40, 60]
    explode = [0.1, 0]
    career_pie.pie(sizes, explode=explode, labels=labels, startangle=70)
    career_pie.set_title("Normal career\n chat")
    career_pie.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    labels = ["Job Title", "Compensation", "Health", "Hobbies", "Friends and Family"]
    sizes = [20, 15, 10, 10, 10]
    explode = (0.0, 0, 0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    life_pie.set_title("Big picture career\n chat")
    life_pie.pie(sizes, explode=explode, labels=labels, startangle=0)
    return plt
