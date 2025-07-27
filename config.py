
import os

class Config:
    # Flask Configuration
    SECRET_KEY = 'coe_project'  # Change this to a secure key
    GEMINI_API_KEY='your_gemini_api_key'
    GOOGLE_API_KEY='ypur_google_api_key'
    
    # File Upload Configuration
    UPLOAD_FOLDER = 'uploads'
    PROCESSED_FOLDER = 'processed'
    ALLOWED_EXTENSIONS = {'csv'}
    
    # Alert Thresholds
    STOCK_ALERT_THRESHOLD = 5  # Items
    EXPIRY_ALERT_DAYS = 7      # Days