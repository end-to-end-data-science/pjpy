# from functools import partial
#
# from sklearn.preprocessing import MinMaxScaler
#
# from pjautoml.config.description.cs.transformercs import TransformerCS
# from pjautoml.config.description.distributions import choice
# from pjautoml.config.description.node import Node
# from pjautoml.config.description.parameter import CatP
# from pjml.tool.data.processing.feature.scaler.scaler import Scaler
#
#
# class MinMax(Scaler):
#     def __init__(self, **sklconfig):
#         super().__init__(sklconfig, MinMaxScaler, deterministic=True)
#
#     @classmethod
#     def _cs_impl(cls):
#         params = {
#             'feature_range': CatP(choice, items=[(-1, 1), (0, 1)])
#         }
#         return TransformerCS(nodes=[Node(params=params)])
