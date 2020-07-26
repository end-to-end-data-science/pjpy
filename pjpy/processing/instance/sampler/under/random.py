#
# from functools import partial
#
# from imblearn.under_sampling import RandomUnderSampler
#
# from pjautoml.config.description.cs.transformercs import TransformerCS
# from pjautoml.config.description.distributions import choice
# from pjautoml.config.description.node import Node
# from pjautoml.config.description.parameter import CatP
# from pjml.tool.data.processing.instance.sampler.resampler import Resampler
#
#
# class UnderS(Resampler):
#     def __init__(self, **kwargs):
#         super().__init__(kwargs, RandomUnderSampler)
#
#     @classmethod
#     def _cs_impl(cls, data=None):
#         params = {
#             'sampling_strategy':
#                 CatP(choice, items=['not minority', 'not majority', 'all'])
#         }
#         return TransformerCS(nodes=[Node(params=params)])
