import logging
import azure.functions as func
import matplotlib as g_mpl
import matplotlib.pyplot as g_plt
import numpy as np
import io


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        g_mpl.use('SVG') 
        g_plt.ioff()
        g_plt.clf()
        p = render(g_plt)
        buf = io.BytesIO()
        p.savefig(buf, format='svg',bbox_inches="tight")
        buf.seek(0)
        return func.HttpResponse(buf.read(), mimetype='image/svg+xml')
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
    return


def render(plt):
    plt.xkcd()


    fig1, (
        (ax_thought_more_productive, ax_normal_hours),
        (ax_actually, ax_more_hours),
    ) = plt.subplots(2, 2)

    height_in_inches = 12
    fig1.set_size_in_inches("figure", figsize=(2 * height_in_inches, height_in_inches))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    ax_thought_more_productive.set_title(" What I thought would make me \n more productive")
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
    ax_actually.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

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



def render_entr(plt):
    plt.xkcd()
    start_year = 2002
    end_year = 2018
    interest_shift_year = 2014

    years = np.linspace(start_year, end_year)
    interest_entrepener = 2 + 98.0 / (1 + np.exp(0.6 * (interest_shift_year - years)))
    interest_technologist = np.maximum(
        (100 - interest_entrepener), 50 + 10 * (np.sin(50 * years))
    )
    interest_entrepener = np.minimum(interest_entrepener, 70 + 10 * (np.sin(40 * years)))

    plt.plot(years, interest_entrepener, "-b", label="Entrepreneur")
    plt.plot(years, interest_technologist, "-r", label="Technologist")
    plt.ylabel("Identity")
    plt.xlabel("Year")

    plt.xlim(start_year, end_year)
    plt.legend(loc="best")
    return plt

