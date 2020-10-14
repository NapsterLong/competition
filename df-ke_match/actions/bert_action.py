from config.bert_config import BertConfig
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S",
                    level=logging.INFO)


class BertAction:

    def fine_tune(self):
        pass

    def predict(self):
        pass
