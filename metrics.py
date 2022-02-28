import pytrec_eval


class Metrics(object):

    def __init__(self, additional_measures):
        measures = set()
        for m in pytrec_eval.supported_measures:
            measures.add(m)
        for m in additional_measures:
            measures.add(m)

        self.measures = measures

    def compute_all_metrics(self, qrel, run):
        evaluator = pytrec_eval.RelevanceEvaluator(qrel, self.measures)
        results = evaluator.evaluate(run)

        return results

    def print_line(self, measure, scope, value):
        print('{:25s}{:8s}{:.4f}'.format(measure, scope, value))

    def print_measure(self, measure, results):
        self.print_line(measure, 'all', pytrec_eval.compute_aggregated_measure(measure, [query_measures[measure] for
                                                                                         query_measures in
                                                                                         results.values()]))

    def compute_aggragated_metric(self, measure, results):
        return pytrec_eval.compute_aggregated_measure(measure,
                                                      [query_measures[measure] for query_measures in results.values()])

