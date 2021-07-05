"""Main module."""
{% if cookiecutter.freedaa_version >= '0.4.1'}
from typing import List

from freedaa.application import FreedaaApplication
from freedaa.pipeline import Pipeline
{% endif %}

def do_nothing():
    pass

{% if cookiecutter.freedaa_version >= '0.4.1' %}
class MyModelApplication(FreedaaApplication):
    @staticmethod
    def training_dataset_builder():
        """
        Here put the code you're going to use to build your training dataset
        """
        pass

    @staticmethod
    def inference_dataset_builder(input_inference):
        """
        Here put the code you're going to use to build your inference dataset
        """

        pass

    @staticmethod
    def create_pipeline() -> List[Pipeline]:
        """
        Here put the code you're going to use to build your inference dataset
        """

        pass

    def predict(self, df):
        pass
{% endif %}
