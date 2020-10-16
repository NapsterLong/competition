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
    --block_size=64 \
    --mlm \
    --logging_dir=logs/lm_bert \
    --num_train_epochs=10 \
    --logging_steps=100 \
    --overwrite_output_dir \
    --save_steps=1000
```
{'loss': 0.18425849150680004, 'learning_rate': 4.472049689440994e-06, 'epoch': 2.329192546583851, 'step': 1500}
{'loss': 1.16001953125, 'learning\_rate': 7.970467321083984e-08, 'epoch': 2.9952177196073495, 'total_flos': 6930451777583616, 'step': 11900}
## fine-tune
```bash
python3 actions/bert_action.py \
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
  --num_train_epochs 10.0 \
  --output_dir output/bert \
  --overwrite_output_dir \
  --logging_dir=logs/bert \
  --logging_steps=100 
```
{'eval_loss': 0.3140621852632612, 'eval_acc': 0.893, 'epoch': 3.0, 'step': 1932}
predict_result:0.76506733
{'eval_loss': 0.30129435753822326, 'eval_acc': 0.895, 'epoch': 3.0, 'total_flos': 4850406590538240, 'step': 2574}  
predict_result:0.74494982406 

# bert-wmm
hfl/chinese-bert-wwm-ext
## lm 
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_bert_wwm \
    --model_name_or_path="hfl/chinese-bert-wwm-ext" \
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_bert_wwm \
    --logging_steps=100 \
    --save_steps=1000
```
{'loss': 1.2216015625, 'learning_rate': 7.970467321083984e-08, 'epoch': 2.9952177196073495, 'total_flos': 6920633748857232, 'step': 11900}
## fine-tune
```bash
python3 actions/bert_action.py \
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
eval_loss = 0.314685204744339 eval_acc = 0.894 epoch = 3.0 total_flos = 4850406590538240   
predict_result:0.75612632682

# roberta
clue/roberta_chinese_base
## lm
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_roberta_wwm \
    --model_name_or_path="clue/roberta_chinese_base" \
    --tokenizer_name="roberta-base"
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_roberta_wwm \
    --logging_steps=100 \
    --save_steps=1000
```
## fine-tune
```bash
python3 actions/bert_action.py \
  --model_name_or_path clue/roberta_chinese_base \
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
  --output_dir output/roberta \
  --logging_dir=logs/roberta \
  --logging_steps=100
```

# roberta-wmm
hfl/chinese-roberta-wwm-ext
## lm 
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_roberta_wwm \
    --model_name_or_path="hfl/chinese-roberta-wwm-ext" \
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --block_size=64 \
    --logging_dir=logs/lm_roberta_wwm \
    --logging_steps=100 \
    --overwrite_output_dir \
    --save_steps=1000
```
{'loss': 1.203857421875, 'learning\_rate': 7.970467321083984e-08, 'epoch': 2.9952177196073495, 'total\_flos': 6920633748857232, 'step': 11900}                                       
## fine-tune
```bash
python3 actions/bert_action.py \
  --model_name_or_path output/lm_roberta_wwm \
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
  --output_dir output/roberta_wwm \
  --logging_dir=logs/roberta_wwm \
  --logging_steps=100
```
{'eval\_loss': 0.30405679988861084, 'eval\_acc': 0.899, 'epoch': 3.0, 'total_flos': 4850406590538240, 'step': 2574}                                                                  
predict_result:0.76195453358

# albert
voidful/albert_chinese_base
## lm 
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_albert \
    --model_name_or_path="voidful/albert_chinese_base" \
    --tokenizer_name="albert-base-v2" \
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_albert \
    --logging_steps=100 \
    --save_steps=1000
```
{'loss': 0.5169482421875, 'learning\_rate': 7.970467321083984e-08, 'epoch': 2.9952177196073495, 'total\_flos': 235106405187840, 'step': 11900}
## fine-tune
```bash
python3 actions/bert_action.py \
  --model_name_or_path output/lm_albert \
  --task_name WNLI \
  --do_train \
  --do_eval \
  --do_predict \
  --data_dir datas/real \
  --max_seq_length 128 \
  --per_device_train_batch_size 16 \
  --per_device_eval_batch_size 16 \
  --learning_rate 2e-4 \
  --num_train_epochs 3.0 \
  --output_dir output/albert \
  --overwrite_output_dir \
  --logging_dir=logs/albert \
  --logging_steps=100
```
{'eval\_loss': 0.5372277679443359, 'eval\_acc': 0.761, 'epoch': 3.0, 'total_flos': 554200096596480, 'step': 2574}                                                        

# xlnet
hfl/chinese-xlnet-base
## lm 
```bash
python3 actions/lm_pretrain.py \
    --output_dir=output/lm_xlnet \
    --model_name_or_path="hfl/chinese-xlnet-base" \
    --do_train \
    --per_device_train_batch_size=8 \
    --train_data_file=datas/train/lm_corpus.tsv \
    --mlm \
    --line_by_line \
    --logging_dir=logs/lm_xlnet \
    --logging_steps=100 \
    --save_steps=1000
```
## fine-tune
```bash
python3 actions/bert_action.py \
  --model_name_or_path output/lm_xlnet \
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
  --output_dir output/xlnet \
  --logging_dir=logs/xlnet \
  --logging_steps=100
```
