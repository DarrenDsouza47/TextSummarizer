from TextSummarizer.config.configuration import ModelTrainerConfig
from transformers import DataCollatorForSeq2Seq,AutoTokenizer
from transformers import TrainingArguments,Trainer,AutoModelForSeq2SeqLM
import torch,os
from datasets import load_from_disk
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig) -> None:
        self.config=config
    
    def trainer(self):
        device="cuda" if torch.cuda.isavailable() else "cpu"
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seqDataCollator=DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model)

        dataset_samsum_pt=load_from_disk(self.config.data_path)
        train_params=TrainingArguments(output_dir=self.config.root_dir,
                                       num_train_epochs=self.config.num_train_epochs,
                                       warmup_steps=self.config.warmup_steps,
                                       per_device_train_batch_size=self.config.per_device_train_batch_size,
                                       per_gpu_eval_batch_size=self.config.per_device_eval_batch_size,
                                       weight_decay=self.config.weight_decay,
                                       logging_steps=self.config.logging_steps,
                                       evaluation_strategy=self.config.evaluation_strategy,
                                       eval_steps=self.config.eval_steps,
                                       save_steps=self.config.save_steps,
                                       gradient_accumulation_steps=self.config.gradient_accumulation_steps, 
                                       )

        trainer=Trainer(model=model,args=train_params,tokenizer=tokenizer,data_collator=seq2seqDataCollator,train_dataset=dataset_samsum_pt["test"],
                    eval_dataset=dataset_samsum_pt["validation"])

        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir,"model_pegasus"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"model_tokenizer"))


