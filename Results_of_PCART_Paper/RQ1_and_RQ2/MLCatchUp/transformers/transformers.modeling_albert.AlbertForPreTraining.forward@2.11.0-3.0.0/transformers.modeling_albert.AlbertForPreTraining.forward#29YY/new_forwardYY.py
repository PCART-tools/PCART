from transformers import AlbertForPreTraining
import torch
import inspect
model = AlbertForPreTraining.from_pretrained('/home/zhang/albert-base-v2')
input_ids = torch.tensor([[31, 51, 99, 15, 5]])
attention_mask = torch.tensor([[1, 1, 1, 1, 1]])
token_type_ids = torch.tensor([[0, 0, 0, 0, 0]])
position_ids = torch.tensor([[0, 1, 2, 3, 4]])
masked_lm_labels = torch.tensor([[1, 2, 3, 4, 5]])
sentence_order_label = torch.tensor([0])
outputs = model.forward(input_ids, attention_mask, token_type_ids, position_ids, None, None, labels=masked_lm_labels, output_attentions=None, output_hidden_states=None)
