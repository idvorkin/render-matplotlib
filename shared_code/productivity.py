def render(plt):
    plt.xkcd()

    (
        fig1,
        ((ax_thought_more_productive, ax_normal_hours), (ax_actually, ax_more_hours)),
    ) = plt.subplots(2, 2)

    height_in_inches = 12
    fig1.set_size_inches(2 * height_in_inches, height_in_inches)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    ax_thought_more_productive.set_title(
        " What I thought would make me \n more productive"
    )
    ax_thought_more_productive.pie(
        [100, 10], labels=["More hours", "More Money"], startangle=200
    )
    ax_thought_more_productive.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.

    labels = ["More hours", "Exercise", "Healthy Eating", "Sleep", "Time Off"]
    sizes = [30, 10, 15, 30, 10]
    explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    ax_actually.pie(sizes, explode=explode, labels=labels, startangle=300)
    ax_actually.set_title("What Actually Does")
    ax_actually.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax_normal_hours.set_title("Time distribution working normal hours")
    ax_normal_hours.barh(y=[""], width=[44], color="red")
    ax_normal_hours.barh(y=[""], width=[36], color="royalblue")
    ax_normal_hours.legend(["Dicking Around", "Working"])
    ax_normal_hours.set_xlim(0, 70)
    ax_more_hours.set_title("Time distribution working more hours")
    ax_more_hours.barh(y=[""], width=[64], color="red")
    ax_more_hours.barh(y=[""], width=[44], color="royalblue")
    ax_more_hours.legend(["Dicking Around", "Working"])
    ax_more_hours.set_xlim(0, 70)
    return plt
