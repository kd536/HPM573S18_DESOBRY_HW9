import InputData as Settings
import scr.FormatFunctions as F
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import scr.EconEvalClasses as Econ


def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of time to STROKE
    time_to_STROKE_death_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_time_to_STROKE().get_mean(),
        interval=simOutput.get_sumStat_time_to_STROKE().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # print outcomes
    print(therapy_name)
    print("  Estimate of mean survival time and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
    print("  Estimate of mean time to STROKE and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          time_to_STROKE_death_CI_text)
    print("")


def draw_survival_curves_and_histograms(simOutputs_anti, simOutputs_none):
    """ draws the survival curves and the histograms of time until STROKE deaths
    :param simOutputs_anti: output of a cohort simulated under ANTI therapy
    :param simOutputs_none: output of a cohort simulated under NONE therapy
    """

    # get survival curves of both treatments
    survival_curves = [
        simOutputs_anti.get_survival_curve(),
        simOutputs_none.get_survival_curve()
    ]

    # graph survival curve
    PathCls.graph_sample_paths(
        sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step (year)',
        y_label='Number of alive patients',
        legends=['Anticoagulant Therapy', 'None Therapy']
    )

    # histograms of survival times
    set_of_survival_times = [
        simOutputs_anti.get_survival_times(),
        simOutputs_none.get_survival_times()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of patient survival time',
        x_label='Survival time (year)',
        y_label='Counts',
        bin_width=1,
        legend=['Anticoagulant Therapy', 'None Therapy'],
        transparency=0.6
    )
