from typing import Tuple, Dict, Any

from sklearn.preprocessing import MinMaxScaler

import pjdata.types as t
from pjautoml.cs.cs import CS
from pjautoml.cs.operand.graph.graph import Graph
from pjautoml.cs.operand.graph.node import Node
from pjml.util.distributions import choice
from pjautoml.util.parameter import CatP
from pjpy.algorithm import TSKLAlgorithm


class MinMax(TSKLAlgorithm):
    def __init__(self, feature_range: Tuple[int, int] = (0, 1), enhance: bool = True, model: bool = True):
        super().__init__(
            {'feature_range': feature_range}, MinMaxScaler, deterministic=True,
            sklconfig={'feature_range': feature_range}, enhance=enhance, model=model
        )

    def _enhancer_info(self, data: t.Data) -> Dict[str, Any]:
        return self._info(data)

    def _enhancer_func(self) -> t.Transformation:
        return lambda train: self.predict(train, train)

    def _model_info(self, data: t.Data) -> Dict[str, Any]:
        return self._info(data)

    def _model_func(self, data: t.Data) -> t.Transformation:
        return lambda test: self.predict(data, test)

    def _info(self, data: t.Data) -> Dict[str, Any]:
        sklearn_model = self.algorithm_factory()
        sklearn_model.fit(data.X)
        return {"sklearn_model": sklearn_model}

    def predict(self, train: t.Data, test: t.Data) -> t.Result:
        info = self._info(train)
        return {'X': info["sklearn_model"].transform(test.X)}

    @classmethod
    def _cs_impl(cls) -> CS:
        param = {
            'feature_range': CatP(choice, items=[(-1, 1), (0, 1)])
        }
        return Graph(nodes=[Node(param)])
