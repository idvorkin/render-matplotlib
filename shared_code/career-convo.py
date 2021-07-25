
def render(plt):
    plt.xkcd()
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    fig1,  (career_pie, life_pie) = plt.subplots(1, 2)

    career_pie.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.

    labels = ["Job Title", "Compensation"]
    sizes = [40, 60]
    explode = [0.1, 0]
    career_pie.pie(sizes, explode=explode, labels=labels, startangle=0)
    career_pie.set_title("Career Discussions\nDeafult")
    career_pie.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    labels = ["Job Title", "Compensation", "Health", "Hobbies", "Friends and Family"]
    sizes = [20, 15, 10, 10, 10]
    explode = (0.0, 0, 0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    life_pie.set_title("Career Discussions\nWith the big picture")
    life_pie.pie(sizes, explode=explode, labels=labels, startangle=300)
    return plt
