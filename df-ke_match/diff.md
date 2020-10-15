# bert
bert-base-chinese
## lm 
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_bert \
    --model_name_or_path="bert-base-chinese" \
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_bert \
    --logging_steps=100
```
{'loss': 0.18425849150680004, 'learning_rate': 4.472049689440994e-06, 'epoch': 2.329192546583851, 'step': 1500}
## fine-tune
```bash
python actions/bert_action.py \
  --model_name_or_path output/lm_bert \
  --task_name WNLI \
  --do_train \
  --do_eval \
  --do_predict \
  --data_dir datas/real \
  --max_seq_length 128 \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 16 \
  --learning_rate 2e-5 \
  --num_train_epochs 3.0 \
  --output_dir output/bert \
  --logging_dir=logs/bert \
  --logging_steps=100
```
{'eval_loss': 0.3140621852632612, 'eval_acc': 0.893, 'epoch': 3.0, 'step': 1932}

predict_result:0.76506733

# bert-wmm
hfl/chinese-bert-wwm-ext
## lm 
```bash
python actions/lm_pretrain.py \
    --output_dir=output/lm_bert_wwm \
    --model_name_or_path="hfl/chinese-bert-wwm-ext" \
    --do_train \
    --per_device_train_batch_size=16 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_bert_wwm \
    --logging_steps=100
```
## fine-tune
```bash
python actions/bert_action.py \
  --model_name_or_path output/lm_bert_wwm \
  --task_name WNLI \
  --do_train \
  --do_eval \
  --do_predict \
  --data_dir datas/real \
  --max_seq_length 128 \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 16 \
  --learning_rate 2e-5 \
  --num_train_epochs 3.0 \
  --output_dir output/bert_wwm \
  --logging_dir=logs/bert_wwm \
  --logging_steps=100
```

# roberta
clue/roberta_chinese_base
## lm 
## fine-tune

# roberta-wmm
hfl/chinese-roberta-wwm-ext
## lm 
## fine-tune

# albert
voidful/albert_chinese_base
## lm 
## fine-tune

# xlnet
hfl/chinese-xlnet-base
## lm 
## fine-tune
