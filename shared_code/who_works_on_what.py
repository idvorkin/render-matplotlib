def render(plt):
    plt.xkcd()
    from matplotlib_venn import venn2, venn3, venn3_unweighted

    plt.xkcd()
    plt.title("Allocate Resources by \n Maximizing Overlap")
    out = venn3(
        subsets=(10, 10, 10, 10, 9, 4, 3),
        set_labels=("Personal Preference", "Business Need", "Probability Of Success"),
        alpha=0.5,
    )
    # out = venn3_unweighted(subsets = (20, 10, 12, 10, 9, 4, 3), set_labels = ("Personal Preference", "Business Need", "Likely To Succeed"), alpha = 0.5);

    for idx, subset in enumerate(out.subset_labels):
        out.subset_labels[idx].set_visible(False)
    return plt
