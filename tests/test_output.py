"""Test module for MFE class output details."""
import pytest

from pymfe.mfe import MFE
from tests.utils import load_xy

GNAME = "mfe-output-details"


class TestErrorsWarnings:
        """TestClass dedicated to test MFE output details."""

        def test_output_lengths_1(self):
            X, y = load_xy(0)
            res = MFE().fit(X=X.values, y=y.values).extract()
            vals, names = res

            assert len(vals) == len(names)

        @pytest.mark.parametrize(
            "dt_id, measure_time",
            [
                (0, "total"),
                (0, "total_summ"),
                (0, "avg"),
                (0, "avg_summ"),
                (2, "total"),
                (2, "total_summ"),
                (2, "avg"),
                (2, "avg_summ"),
            ])
        def test_output_lengths_2(self, dt_id, measure_time):
            X, y = load_xy(dt_id)
            res = MFE(measure_time=measure_time).fit(X=X.values,
                                                     y=y.values).extract()
            vals, names, time = res

            assert len(vals) == len(names) == len(time)

        def test_output_lengths_3(self):
            X, y = load_xy(0)
            res = MFE(summary=None).fit(X=X.values, y=y.values).extract()
            vals, names = res

            assert len(vals) == len(names)

        @pytest.mark.parametrize(
            "dt_id, measure_time",
            [
                (0, "total"),
                (0, "total_summ"),
                (0, "avg"),
                (0, "avg_summ"),
                (2, "total"),
                (2, "total_summ"),
                (2, "avg"),
                (2, "avg_summ"),
            ])
        def test_output_lengths_4(self, dt_id, measure_time):
            X, y = load_xy(dt_id)
            res = MFE(summary=None,
                      measure_time=measure_time).fit(X=X.values,
                                                     y=y.values).extract()
            vals, names, time = res

            assert len(vals) == len(names) == len(time)

        @pytest.mark.parametrize(
            "verbosity, msg_expected",
            [
                (0, False),
                (1, True),
                (2, True),
            ])
        def test_verbosity_1(self, verbosity, msg_expected, capsys):
            MFE._print_verbose_progress(
                cur_progress=0,
                cur_mtf_name="foo",
                verbose=verbosity)

            captured = capsys.readouterr().out

            assert (not msg_expected) or captured

        def test_verbosity_2(self, capsys):
            X, y = load_xy(0)

            MFE().fit(X=X.values,
                      y=y.values).extract(verbose=0)

            captured = capsys.readouterr().out

            assert not captured

        @pytest.mark.parametrize(
            "verbosity, msg_expected",
            [
                (0, False),
                (1, True),
                (2, True),
            ])
        def test_verbosity_3(self, verbosity, msg_expected, capsys):
            X, y = load_xy(0)

            MFE().fit(X=X.values,
                      y=y.values).extract(verbose=verbosity)

            captured = capsys.readouterr().out

            assert (not msg_expected) or captured
