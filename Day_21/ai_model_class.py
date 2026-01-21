# Day 21: Classes and Objects - AI Architecture
# Building a Blueprint for a Machine Learning Model.

class SimpleAIModel:
    def __init__(self, model_name, learning_rate):
        # Attributes: The 'data' the object holds
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.is_trained = False
        print(f"🤖 Model '{self.model_name}' initialized.")

    def train(self, data_points):
        # Method: An 'action' the object can perform
        print(f"⚙️ Training {self.model_name} on {len(data_points)} samples...")
        self.is_trained = True
        print("✅ Training complete.")

    def predict(self, input_value):
        if not self.is_trained:
            return "❌ Error: Model must be trained before predicting."
        return f"🔮 Prediction for {input_value}: High Confidence"

# --- Using the Class (Creating an Object) ---
# This is an 'instance' of our blueprint
my_brain = SimpleAIModel("NeuralNet_v1", 0.001)

# Performing actions
my_brain.train([1, 2, 3, 4, 5])
result = my_brain.predict("Image_Data_01")

print(result)