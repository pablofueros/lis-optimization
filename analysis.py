import marimo

__generated_with = "0.17.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    from pathlib import Path
    return Path, pd, px


@app.cell
def _(Any, Path, pd):
    def load_hyperfine_results(path: Path, label: str) -> pd.DataFrame:
        """Load hyperfine JSON results into a pandas DataFrame."""
        data: dict[str, Any] = pd.read_json(path).to_dict()
        results: list[dict[str, Any]] = data["results"]
        df = pd.DataFrame(results).T

        # Extract n (for example, from "uv run python/01_lis_naive.py 50")
        df["n"] = df["command"].str.extract(r"(\d+)$").astype(int)
        df["implementation"] = label
        return df[["n", "mean", "stddev", "min", "max", "implementation"]].sort_values("n")
    return (load_hyperfine_results,)


@app.cell
def _(pd, px):
    def plot_results(dfs: list[pd.DataFrame], title: str) -> None:
        """Plot performance comparison between multiple implementations."""
        df_all = pd.concat(dfs, ignore_index=True)

        fig = px.line(
            df_all,
            x="n",
            y="min",
            color="implementation",
            # error_y="stddev",
            markers=True,
            title=title,
            labels={
                "n": "Input size (n)",
                "min": "Min execution time (s)",
                "implementation": "Implementation"
            },
        )

        fig.update_layout(
            template="plotly_dark",
            title_font=dict(size=20, family="Arial", color="white"),
            font=dict(size=14, family="Arial", color="white"),
            plot_bgcolor="rgb(17,17,17)",
            paper_bgcolor="rgb(17,17,17)",
            hovermode="x unified",
            margin=dict(l=60, r=60, t=80, b=60),
            legend=dict(title="", yanchor="top", y=0.99, xanchor="left", x=0.01),
        )

        fig.update_traces(line=dict(width=3), marker=dict(size=8))
        fig.show()
    return (plot_results,)


@app.cell
def _(Path, load_hyperfine_results):
    path_py = Path("results/python_recursive.json")
    path_rs_debug = Path("results/rust_recursive_debug.json")
    path_rs_release = Path("results/rust_recursive_release.json")

    df_py = load_hyperfine_results(path_py, "Python recursive")
    df_rs_debug = load_hyperfine_results(path_rs_debug, "Rust recursive (debug)")
    df_rs_release = load_hyperfine_results(path_rs_release, "Rust recursive (release)")
    return df_py, df_rs_debug, df_rs_release


@app.cell
def _(df_py, plot_results):
    plot_results(
            [df_py],
            "Recursive LIS Implementation Performance Comparison"
        )
    return


@app.cell
def _(df_py, df_rs_debug, plot_results):
    plot_results(
            [df_py, df_rs_debug],
            "Naive LIS Implementation Performance Comparison"
        )
    return


@app.cell
def _(df_py, df_rs_debug, df_rs_release, plot_results):
    plot_results(
            [df_py, df_rs_debug, df_rs_release],
            "Naive LIS Implementation Performance Comparison"
        )
    return


@app.cell
def _(pd, px):
    def barplot_comparation(dfs: list[pd.DataFrame]) -> None:
        """Barplot performance comparison between multiple implementations."""
        df_all = pd.concat(dfs, ignore_index=True)

        fig = px.bar(
            df_all,
            x="implementation",
            y="mean",
            # error_y="Std Dev",
            color="implementation",
            text="mean",
            title="Performance Comparison – LIS Recursive (N=90)",
        )

        fig.update_layout(
            template="plotly_dark",
            title_font=dict(size=20, family="Arial", color="white"),
            font=dict(size=14, family="Arial", color="white"),
            plot_bgcolor="rgb(17,17,17)",
            paper_bgcolor="rgb(17,17,17)",
            hovermode="x unified",
            margin=dict(l=60, r=60, t=80, b=60),
            # title=dict(x=0.5, font=dict(size=22, family="Arial", color="black")),
            xaxis_title=None,
            yaxis_title="Execution Time (seconds)",
            yaxis=dict(showgrid=True, gridcolor="lightgray"),
            showlegend=False,
        )


        fig.update_traces(
            texttemplate="%{text:.3f}s",
            textposition="outside",
            marker_line_width=1.2,
            marker_line_color="black",
        )

        fig.show()
    return (barplot_comparation,)


@app.cell
def _(Path, barplot_comparation, load_hyperfine_results):
    path_py_rec_90 = Path("results/python_recursive_90.json")
    df_py_rec_90 = load_hyperfine_results(path_py_rec_90, "Python Recursive")

    path_rs_rec_deb_90 = Path("results/rust_recursive_debug_90.json")
    df_rs_rec_deb_90 = load_hyperfine_results(path_rs_rec_deb_90, "Rust Recursive Debug")

    path_rs_rec_rel_90 = Path("results/rust_recursive_release_90.json")
    df_rs_rec_rel_90 = load_hyperfine_results(path_rs_rec_rel_90, "Rust Recursive Release")

    dfs_1 = [df_py_rec_90, df_rs_rec_deb_90, df_rs_rec_rel_90]

    barplot_comparation(dfs_1)
    return df_py_rec_90, df_rs_rec_deb_90, df_rs_rec_rel_90


@app.cell
def _(
    Path,
    barplot_comparation,
    df_py_rec_90,
    df_rs_rec_deb_90,
    df_rs_rec_rel_90,
    load_hyperfine_results,
):
    path_py_rec_314_90 = Path("results/python_recursive_314_90.json")
    df_py_rec_314_90 = load_hyperfine_results(path_py_rec_314_90, "Python Recursive 3.14")

    dfs_2 = [df_py_rec_90, df_py_rec_314_90, df_rs_rec_deb_90, df_rs_rec_rel_90]

    barplot_comparation(dfs_2)
    return (df_py_rec_314_90,)


@app.cell
def _(
    Path,
    barplot_comparation,
    df_py_rec_314_90,
    df_py_rec_90,
    df_rs_rec_deb_90,
    df_rs_rec_rel_90,
    load_hyperfine_results,
):
    path_py_rec_pypy_90 = Path("results/python_recursive_pypy_90.json")
    df_py_rec_pypy_90 = load_hyperfine_results(path_py_rec_pypy_90, "Python Recursive PyPy")

    dfs_3 = [df_py_rec_90, df_py_rec_314_90, df_py_rec_pypy_90, df_rs_rec_deb_90, df_rs_rec_rel_90]

    barplot_comparation(dfs_3)
    return (df_py_rec_pypy_90,)


@app.cell
def _(
    Path,
    barplot_comparation,
    df_py_rec_314_90,
    df_py_rec_90,
    df_py_rec_pypy_90,
    df_rs_rec_deb_90,
    df_rs_rec_rel_90,
    load_hyperfine_results,
):
    path_py_rec_opt_90 = Path("results/python_recursive_opt_90.json")
    df_py_rec_opt_90 = load_hyperfine_results(path_py_rec_opt_90, "Python Recursive Opt")

    dfs_4 = [df_py_rec_90, df_py_rec_314_90, df_py_rec_pypy_90, df_py_rec_opt_90, df_rs_rec_deb_90, df_rs_rec_rel_90]

    barplot_comparation(dfs_4)
    return (df_py_rec_opt_90,)


@app.cell
def _(
    Path,
    barplot_comparation,
    df_py_rec_314_90,
    df_py_rec_90,
    df_py_rec_opt_90,
    df_py_rec_pypy_90,
    df_rs_rec_deb_90,
    df_rs_rec_rel_90,
    load_hyperfine_results,
):
    path_py_rec_np_90 = Path("results/python_recursive_np_90.json")
    df_py_rec_np_90 = load_hyperfine_results(path_py_rec_np_90, "Python Recursive Numpy")

    dfs_5 = [df_py_rec_90, df_py_rec_314_90, df_py_rec_pypy_90, df_py_rec_opt_90, df_py_rec_np_90, df_rs_rec_deb_90, df_rs_rec_rel_90]

    barplot_comparation(dfs_5)
    return


if __name__ == "__main__":
    app.run()
