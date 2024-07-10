from transformers import RobertaTokenizerFast, RobertaForMaskedLM
import torch
from datasets import load_dataset
from transformers import Trainer, TrainingArguments


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset
ds = load_dataset("MohamedSaeed-dev/python-text-to-code")

# Load tokenizer
tokenizer = RobertaTokenizerFast.from_pretrained("microsoft/codebert-base")

# Tokenization function
def tokenize_function(examples):
    return tokenizer(examples['code'], padding=True, truncation=True)

# Tokenize dataset
tokenized_dataset = ds.map(tokenize_function, batched=True)

# Load CodeBERT model
model = RobertaForMaskedLM.from_pretrained("microsoft/codebert-base")

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'], 
    eval_dataset=tokenized_dataset['validation'],
    tokenizer=tokenizer,
)

# Train the model
trainer.train()

# Example inference
code_snippet = """
def add(a, b):
    return a + b
"""

# Tokenize input text
inputs = tokenizer(code_snippet, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Decode predictions
logits = outputs.logits
predictions = torch.argmax(logits, dim=-1)
decoded_predictions = tokenizer.decode(predictions[0])

# Print results
print("Original Code Snippet:")
print(code_snippet)
print("\nDecoded Predictions:")
print(decoded_predictions)
