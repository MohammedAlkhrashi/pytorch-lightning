# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pytorch_lightning.loggers.logger import Logger
from pytorch_lightning.utilities.warnings import rank_zero_deprecation


class LightningLoggerBase(Logger):
    """Base class for experiment loggers.

    Args:
        agg_key_funcs:
            Dictionary which maps a metric name to a function, which will
            aggregate the metric values for the same steps.
        agg_default_func:
            Default function to aggregate metric values. If some metric name
            is not presented in the `agg_key_funcs` dictionary, then the
            `agg_default_func` will be used for aggregation.

    Note:
        The `agg_key_funcs` and `agg_default_func` arguments are used only when
        one logs metrics with the :meth:`~LightningLoggerBase.agg_and_log_metrics` method.
    """

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        rank_zero_deprecation(
            "The `pl.loggers.base.LightningLoggerBase` is deprecated. "
            " Please use `pl.loggers.logger.Logger` instead."
        )
        super().__init__(*args, **kwargs)
