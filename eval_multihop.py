import argparse
import json
from collections import defaultdict

from metrics import Metrics


def load_json(path):
    with open(path, "r") as outfile:
        json_data = json.load(outfile)

    return json_data


def eval(args):
    qrel = load_json(args.path_qrel)
    run = load_json(args.path_run)
    data = load_json(args.path_hotpotqa)

    # group samples by type
    groups = defaultdict(list)
    for sample in data:
        question_id = sample["_id"]
        groups[sample["type"]].append(question_id)

    qrel_bridge = {q: v for q, v in qrel.items() if q in groups["bridge"]}
    run_bridge = {q: v for q, v in run.items() if q in groups["bridge"]}

    qrel_comp = {q: v for q, v in qrel.items() if q in groups["comparison"]}
    run_comp = {q: v for q, v in run.items() if q in groups["comparison"]}

    # additional measures
    metrics = Metrics(args.metrics)

    print("Overall")
    results = metrics.compute_all_metrics(qrel, run)
    agg_metrics = dict()
    for m in args.metrics:
        agg_metrics[m] = metrics.compute_aggragated_metric(m, results)
    print(agg_metrics)

    print("Bridge Questions")
    results = metrics.compute_all_metrics(qrel_bridge, run_bridge)
    agg_metrics = dict()
    for m in args.metrics:
        agg_metrics[m] = metrics.compute_aggragated_metric(m, results)
    print("\t".join([f"{m:.5f}" for m in agg_metrics.values()]))

    print("Comparison Questions")
    results = metrics.compute_all_metrics(qrel_comp, run_comp)
    agg_metrics = dict()
    for m in args.metrics:
        agg_metrics[m] = metrics.compute_aggragated_metric(m, results)

    print("\t".join([f"{m:.5f}" for m in agg_metrics.values()]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_qrel", type=str)
    parser.add_argument("--path_run", type=str)
    parser.add_argument("--path_hotpotqa", type=str)
    parser.add_argument("--metrics", nargs="+", type=str)
    args = parser.parse_args()

    eval(args)

