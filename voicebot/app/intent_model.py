import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

class IntentClassifier:
    def __init__(self, model_path="models/intent_model"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.labels = self.model.config.id2label

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probs, dim=1)

        return {
            "intent": self.labels[predicted_class.item()],
            "confidence": confidence.item()
        }

