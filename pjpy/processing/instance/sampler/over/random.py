# from functools import partial
#
# from imblearn.over_sampling import RandomOverSampler
#
# from pjautoml.config.description.cs.transformercs import TransformerCS
# from pjautoml.config.description.distributions import choice
# from pjautoml.config.description.node import Node
# from pjautoml.config.description.parameter import CatP
# from pjml.tool.data.processing.instance.sampler.resampler import Resampler
#
#
# class OverS(Resampler):
#     def __init__(self, **kwargs):
#         # TODO: Default values should be extracted from CS (via (new) property
#         #  'default'), to appear here in 'self.config'.
#         super().__init__(kwargs, RandomOverSampler)
#
#     @classmethod
#     def _cs_impl(cls, data=None):
#         params = {
#             'sampling_strategy':
#                 CatP(choice, items=['not minority', 'not majority', 'all'])
#         }
#         return TransformerCS(nodes=[Node(params)])
