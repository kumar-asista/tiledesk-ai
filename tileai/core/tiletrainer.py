from __future__ import annotations
from abc import ABC, abstractmethod

from tileai.core.TileTrainertorch_ff import TileTrainertorchFF
from tileai.core.TileTrainertorch_wbag import TileTrainertorchWBag
from tileai.core.TileTrainertorch_average import TileTrainertorchAverage
from tileai.core.TileTrainerBag import TileTrainertorchBag
from tileai.core.tiletrainer_bert import TileTrainertorchBert


class TileTrainerFactory:
    def create_tiletrainer(self, name, language, pipeline, parameters, model):

        if name =='embeddingwbag':
            return TileTrainertorchWBag(language, pipeline, parameters, model)
        elif name == 'embeddigaverage':
            return TileTrainertorchAverage(language, pipeline, parameters, model)
        elif name == 'textclassifier':
            return TileTrainertorchBag(language, pipeline, parameters, model)
        elif name == 'bertclassifier':
            return TileTrainertorchBert(language, pipeline, parameters, model)
        else:
            return TileTrainertorchFF(language, pipeline, parameters, model)



"""
 "configuration":{
      "language":"it",
      "pipeline":["bertclassifier","dbmdz/bert-base-italian-uncased"]
    },
"""
   