class ResponseGenerator:

    def __init__(self):
        self.responses = {
            "order_status": "Please provide your order ID to check the status.",
            "cancel_order": "Your order can be cancelled within 24 hours.",
            "refund_request": "Refunds are processed within 5 business days.",
            "subscription_issue": "Let me check your subscription details.",
            "technical_support": "Please describe the technical issue.",
            "billing_issue": "I will connect you to billing support.",
            "change_address": "Your address can be updated from account settings.",
            "product_info": "Please specify the product name.",
            "complaint": "We apologize for the inconvenience.",
            "greeting": "Hello! How can I assist you today?"
        }

    def generate(self, intent):
        return self.responses.get(intent, 
            "I'm sorry, I didn't understand your request.")

