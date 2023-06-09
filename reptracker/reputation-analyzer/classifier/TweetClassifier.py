import json

from torch import nn
from transformers import BertModel, BertTokenizer

with open("reputation-analyzer/config.json") as json_file:
    config =json.load(json_file)

class TweetClassifier(nn.Module):
  def __init__(self):
    super(TweetClassifier, self).__init__()
    self.bert = BertModel.from_pretrained(config["PRE_TRAINED_MODEL_NAME"])
    self.drop = nn.Dropout(p = config["DROPOUT_RATE"])
    self.out = nn.Linear(self.bert.config.hidden_size, len(config["CLASSES"]))
    

  def forward(self, input_ids, attention_mask):
    # Coloca entrada no modelo BERT
    _, output = self.bert(input_ids, attention_mask, return_dict = False)

    # Coloca saída do BERT na entrada da Dropout
    output = self.drop(output)

    # Retorna a saída da camada Linear usando a saída da Dropout como entrada
    return self.out(output)