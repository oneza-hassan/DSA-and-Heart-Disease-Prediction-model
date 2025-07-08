import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import joblib
import os
from datetime import datetime

# Constants
MODEL_FILE = "heart_disease_model.pkl"
DATA_FILE = "heart.csv"
OUTPUT_FILE = "predictions_log.csv"

# These must match the feature names in your training data exactly
FEATURE_NAMES = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
]

class HeartDiseaseClassifier:
    def __init__(self, window):
        self.window = window
        self.window.title("Advanced Heart Disease Classifier")
        self.window.geometry("550x850")
        
        # Initialize output file
        self.initialize_output_file()
        
        # Load or train model
        self.model = self.load_or_train_model()
        
        # Create UI
        self.create_widgets()
        self.add_instructions()
    
    def initialize_output_file(self):
        """Create output file with headers if it doesn't exist"""
        if not os.path.exists(OUTPUT_FILE):
            columns = ["timestamp", "prediction"] + FEATURE_NAMES
            pd.DataFrame(columns=columns).to_csv(OUTPUT_FILE, index=False)
    
    def load_or_train_model(self):
        """Load saved model or train a new one"""
        if os.path.exists(MODEL_FILE):
            try:
                model = joblib.load(MODEL_FILE)
                print("Model loaded with features:", model.feature_names_in_)
                return model
            except Exception as e:
                print("Error loading model:", e)
        
        # Train new model
        try:
            heart_data = pd.read_csv(DATA_FILE)
            
            # Ensure we're using the correct feature names
            if 'target' not in heart_data.columns:
                raise ValueError("Dataset missing 'target' column")
                
            df_train, _ = train_test_split(heart_data, train_size=0.9, test_size=0.1, random_state=100)
            y_train = df_train.pop('target')
            x_train = df_train[FEATURE_NAMES]  # Ensure correct feature order
            
            model = make_pipeline(
                StandardScaler(),
                LogisticRegression(max_iter=1000, class_weight='balanced')
            )
            model.fit(x_train, y_train)
            
            # Save model
            joblib.dump(model, MODEL_FILE)
            print("Model trained with features:", FEATURE_NAMES)
            return model
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to train model: {str(e)}")
            raise
    
    def create_widgets(self):
        """Create input widgets with proper labels"""
        input_frame = tk.LabelFrame(self.window, text="Patient Information", padx=10, pady=10)
        input_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Field configuration: (label_text, field_name, help_text)
        field_config = [
            ("Age", "age", "29-77 years"),
            ("Sex", "sex", "0=Female, 1=Male"),
            ("Chest Pain Type", "cp", "0-3 (3=most severe)"),
            ("Resting BP", "trestbps", "94-200 mmHg"),
            ("Cholesterol", "chol", "126-564 mg/dl"),
            ("Fasting BS", "fbs", "0=Normal, 1=High"),
            ("Resting ECG", "restecg", "0-2 (2=worst)"),
            ("Max Heart Rate", "thalach", "71-202 bpm"),
            ("Exercise Angina", "exang", "0=No, 1=Yes"),
            ("ST Depression", "oldpeak", "0-6.2 mm"),
            ("Slope", "slope", "0-2 (2=worst)"),
            ("Major Vessels", "ca", "0-3 blocked"),
            ("Thalassemia", "thal", "1-3 (3=worst)")
        ]
        
        self.entries = {}
        for label_text, field_name, help_text in field_config:
            frame = tk.Frame(input_frame)
            frame.pack(fill="x", pady=2)
            
            tk.Label(frame, text=f"{label_text}:", width=20, anchor="w").pack(side="left")
            
            entry = tk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.entries[field_name] = entry
            
            tk.Button(frame, text="?", width=2,
                     command=lambda ht=help_text: messagebox.showinfo("Help", ht)).pack(side="left", padx=5)
        
        tk.Button(self.window, text="Analyze Heart Risk", 
                 command=self.analyze_heart_risk, bg="#4CAF50", fg="white").pack(pady=15)
    
    def add_instructions(self):
        """Add instructions to the window"""
        instructions = """
        Please enter all patient information carefully.
        Click ? buttons for help with each field.
        Clinical warnings will override model predictions when critical signs are detected.
        Results are saved to predictions_log.csv automatically.
        """
        tk.Label(self.window, text=instructions, justify="left").pack(pady=10)
    
    def clinical_safety_check(self, input_data):
        """Check for clinically dangerous values"""
        warnings = []
        
        # Critical ST depression
        if input_data['oldpeak'] > 2:
            warnings.append(f"Critical ST depression ({input_data['oldpeak']} > 2)")
        
        # Dangerous cholesterol
        if input_data['chol'] > 250 and input_data['age'] < 40:
            warnings.append(f"Extreme cholesterol {input_data['chol']} for age {input_data['age']}")
        
        # Severe hypertension
        if input_data['trestbps'] > 160:
            warnings.append(f"Severe hypertension ({input_data['trestbps']})")
            
        # Multiple vessel disease
        if input_data['ca'] >= 2:
            warnings.append(f"Multiple vessels affected ({input_data['ca']})")
            
        return warnings
    
    def analyze_heart_risk(self):
        """Handle the complete risk analysis"""
        try:
            # Collect and validate inputs
            input_data = {}
            for feature in FEATURE_NAMES:
                value = self.entries[feature].get()
                if not value:
                    raise ValueError(f"Please fill in the {feature} field")
                
                # Convert to appropriate type
                if feature == 'oldpeak':
                    input_data[feature] = float(value)
                else:
                    input_data[feature] = int(value)
            
            # Check clinical safety rules
            clinical_warnings = self.clinical_safety_check(input_data)
            
            # Prepare DataFrame with EXACT feature names and order
            input_df = pd.DataFrame([input_data])[FEATURE_NAMES]
            
            # Get prediction
            prob = self.model.predict_proba(input_df)[0][1]
            model_pred = "has heart disease" if prob > 0.5 else "does not have heart disease"
            
            # Generate result message
            result_msg = []
            if clinical_warnings:
                result_msg.append("⚠️ CLINICAL WARNINGS ⚠️")
                result_msg.extend(clinical_warnings)
                result_msg.append("\nModel prediction may underestimate risk!")
            
            result_msg.append(f"\nModel assessment: {model_pred}")
            result_msg.append(f"Risk probability: {prob:.1%}")
            
            # Show results
            self.show_result("\n".join(result_msg), input_data, prob > 0.5)
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Analysis failed: {str(e)}")
    
    def show_result(self, message, input_data, prediction):
        """Show detailed result window"""
        result_window = tk.Toplevel(self.window)
        result_window.title("Heart Disease Risk Report")
        result_window.geometry("500x300")
        
        tk.Label(result_window, text="Heart Disease Risk Analysis", 
                font=("Arial", 12, "bold")).pack(pady=5)
        
        text_frame = tk.Frame(result_window)
        text_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        result_text = tk.Text(text_frame, wrap="word", yscrollcommand=scrollbar.set)
        result_text.insert("end", message)
        result_text.pack(fill="both", expand=True)
        scrollbar.config(command=result_text.yview)
        
        tk.Button(result_window, text="Save Results", 
                command=lambda: self.save_results(input_data, prediction)).pack(pady=5)
        tk.Button(result_window, text="Close", command=result_window.destroy).pack(pady=5)
    
    def save_results(self, input_data, prediction):
        """Save results to output file"""
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prediction": int(prediction),
            **input_data
        }
        
        df = pd.DataFrame([record])
        df.to_csv(OUTPUT_FILE, mode='a', header=not os.path.exists(OUTPUT_FILE), index=False)
        messagebox.showinfo("Saved", f"Results saved to:\n{os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDiseaseClassifier(root)
    root.mainloop()