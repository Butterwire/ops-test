import click
import structlog
import pandas as pd
import numpy as np

log = structlog.get_logger()


@click.command()
@click.argument("src")
@click.argument("dest")
def main(src, dest):
    """
    Temperature analysis

    Consumes data from the SRC uri, aggregates temperature across countries and outputs the min, max and average
    and outputs to the DEST uri
    """

    # Load data into pandas
    log.info("Loading temperature CSV", uri=src)
    df_input = pd.read_csv(src).fillna(0)
    log.info("CSV data parsed", rows=len(df_input))

    # Calculate country level information
    df_result = (
        df_input.groupby(["iso2"])
        .agg(
            mean=("max_temp", np.mean),
            max=("max_temp", np.max),
            min=("max_temp", np.min),
            cities=("city", np.count_nonzero),
        )
        .sort_values(["max", "iso2"])
    )
    log.info("Calculated temperature for countries", total=len(df_result))

    # Validate that we have a difference between the min, max & average when
    # we have data for multiple cities. If no difference, source data is suspect
    df_suspect = df_result[
        (df_result["cities"] > 1) & (df_result["max"] == df_result["min"])
    ]
    if len(df_suspect) > 0:
        log.error("Suspect temperatures found", dataset=df_suspect)
        raise Exception("Suspect temperatures found in input data set")

    # Save CSV output
    log.info("Temperatures validated, writing output", uri=dest)
    df_result.to_csv(dest)
    log.info("Task completed successfully")


if __name__ == "__main__":
    main()
