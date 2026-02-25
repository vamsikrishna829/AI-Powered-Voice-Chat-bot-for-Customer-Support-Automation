from jiwer import wer

ground_truth = "I want to check my order status"
prediction = "I want check my order status"

print("WER:", wer(ground_truth, prediction))

